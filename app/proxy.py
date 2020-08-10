import os
import requests
from bs4 import BeautifulSoup, Comment
from bs4.element import NavigableString
from flask import Flask, request, Response
import andaluh
import json

from cachetools import cached, LRUCache, TTLCache

ROOT_DOMAIN = "https://es.wikipedia.org/"
WKP_CT_SUMMARY_API = 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.4.2"'
WKP_CT_HTML = 'text/html; charset=UTF-8'
WKP_SUMMARY_API_KEYS_2_TRANSC = ["title", "displaytitle", "description", "extract", "extract_html"]
NOT_TRANSCRIBABLE_ELEMENTS = ["style", "script"]

# Adjust your Google Analytics ID with GA_TRACK_UA environment variable
GA_TRACKING_HEADER = '''
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACK_UA}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '{GA_TRACK_UA}');
</script>
'''

flask_app = Flask(__name__)

cache = TTLCache(maxsize=500, ttl=60)


@cached(cache)
def transcribe(text, vaf='ç', vvf='h'):
    """
    Transcribe input text.
    :param text: input text
    :param vaf: vaf configuration for andaluh-py
    :param vvf: vvf configuration for andaluh-py
    :return:
    """
    try:
        transcription = andaluh.epa(text, vaf=vaf, vvf=vvf)
    except Exception as e:
        transcription = str(text)
        print(f"Error in andaluh package when trying to transcript text {text}: {repr(e)}")
    return transcription


def transcribe_elem_text(elem, vaf, vvf):
    """

    :param elem: BS4 element to transcribe
    :param vaf: vaf configuration for andaluh-py
    :param vvf: vvf configuration for andaluh-py
    :return:
    """
    if elem.name in NOT_TRANSCRIBABLE_ELEMENTS:
        return

    if isinstance(elem, NavigableString) and hasattr(elem, "string") and not isinstance(elem.string, Comment) \
            and elem.string is not "\n":
        elem.string.replaceWith(transcribe(elem.string, vaf=vaf, vvf=vvf))

    if hasattr(elem, "children"):
        for ch in elem.children:
            if not isinstance(ch, Comment):
                transcribe_elem_text(ch, vaf, vvf)


@cached(cache)
def transcribe_html(html_content, vaf="ç", vvf="h"):
    """
    Transcribe a whole html page
    :param html_content: html content
    :param vaf: vaf configuration for andaluh-py
    :param vvf: vvf configuration for andaluh-py
    :return:
    """
    soup = BeautifulSoup(html_content, "lxml")

    # Appending Google Analytics tracking ID (if present) as last head element
    if os.getenv('GA_TRACK_UA'):
        ga_ua_html = GA_TRACKING_HEADER.replace("{GA_TRACK_UA}", os.getenv('GA_TRACK_UA'))
        ga_ua_tag = BeautifulSoup(ga_ua_html)
        soup.head.insert(len(soup.head.contents), ga_ua_tag)

    transcribe_elem_text(soup.head.title, vaf=vaf, vvf=vvf)
    transcribe_elem_text(soup.body, vaf=vaf, vvf=vvf)

    return str(soup)


def prepare_content(resp):
    """
    Transcribe the content of any response from Spanish Wikipedia
    :param resp: response to process
    :return: transcribed content
    """
    if resp.headers.get("Content-Type") == WKP_CT_SUMMARY_API:
        content_dict = json.loads(resp.content)

        for key in WKP_SUMMARY_API_KEYS_2_TRANSC:
            if key in content_dict:
                content_dict[key] = transcribe(content_dict[key])

        content = json.dumps(content_dict, ensure_ascii=False).encode("utf-8")
    elif resp.headers.get("Content-Type") == WKP_CT_HTML:
        content = transcribe_html(resp.content.decode("utf-8")).encode("utf-8")
    else:
        content = resp.content

    return content


@flask_app.route('/', defaults={'url_path': ''})
@flask_app.route('/<path:url_path>', methods=["GET", "POST"])
def get_request(url_path):
    """
    Base request to manage all the request to the site

    :param url_path:
    :return:
    """
    target_url = ROOT_DOMAIN + url_path
    http_method = requests.post if request.method == 'POST' else requests.get

    if request.query_string:
        query_string_decoded = request.query_string.decode("utf-8")
        target_url = f"{target_url}?{query_string_decoded}"
        resp = http_method(target_url)
    elif request.json:
        data = request.json
        resp = http_method(target_url, json=data)

    elif request.form:
        data = request.form.to_dict()
        resp = http_method(target_url, data=data)
    else:
        resp = http_method(target_url)

    content = prepare_content(resp)
    return Response(content, content_type=resp.headers.get("Content-Type"))


if __name__ == '__main__':
    flask_app.run(debug=False, host="0.0.0.0", port=5000)

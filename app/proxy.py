import os
import requests
from bs4 import BeautifulSoup, Comment
from bs4.element import NavigableString
from flask import Flask, request, Response
import andaluh
import json
import re

from cachetools import cached, TTLCache

from app.templates import HEAD, BODY, GA_TRACKING_HEADER, WP_ES_LINK

ROOT_DOMAIN = "https://es.wikipedia.org/"
WKP_CT_SUMMARY_API = r'application\/json; charset=utf-8; profile="https:\/\/www\.mediawiki\.org\/wiki\/Specs\/Summary\/\d+(?:\.\d+)+"'
WKP_CT_HTML = 'text/html; charset=UTF-8'
WKP_SUMMARY_API_KEYS_2_TRANSC = ["title", "displaytitle", "description", "extract", "extract_html"]
NOT_TRANSCRIBABLE_ELEMENTS = ["style", "script"]


flask_app = Flask(__name__,static_folder=None)

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
        transcription = andaluh.epa(text, vaf=vaf, vvf=vvf, escape_links=True)
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
def transcribe_html(html_content, url_path, vaf="ç", vvf="h"):
    """
    Transcribe a whole html page
    :param html_content: html content
    :param vaf: vaf configuration for andaluh-py
    :param vvf: vvf configuration for andaluh-py
    :return:
    """
    soup = BeautifulSoup(html_content, "lxml")

    head_tag = BeautifulSoup(HEAD, "html.parser")
    soup.head.insert(len(soup.head.contents), head_tag)

    # Appending Google Analytics tracking ID (if present) as last head element
    if os.getenv('GA_TRACK_UA'):
        ga_ua_html = GA_TRACKING_HEADER.replace("{GA_TRACK_UA}", os.getenv('GA_TRACK_UA'))
        ga_ua_tag = BeautifulSoup(ga_ua_html)
        soup.head.insert(len(soup.head.contents), ga_ua_tag)

    transcribe_elem_text(soup.head.title, vaf=vaf, vvf=vvf)
    transcribe_elem_text(soup.body, vaf=vaf, vvf=vvf)

    body_tag = BeautifulSoup(BODY, "html.parser")
    soup.body.insert(len(soup.body.contents), body_tag)

    list_lang_links = soup.select_one("nav#p-lang ul.vector-menu-content-list")
    if list_lang_links is not None:
        wp_es_link_filled = WP_ES_LINK.replace("[ARTICLE_PATH]", url_path)
        wp_es_link_tag = BeautifulSoup(wp_es_link_filled, "html.parser")
        list_lang_links.insert(0, wp_es_link_tag)

    return str(soup)


def prepare_content(resp, url_path):
    """
    Transcribe the content of any response from Spanish Wikipedia
    :param resp: response to process
    :return: transcribed content
    """
    if re.match(WKP_CT_SUMMARY_API, resp.headers.get("Content-Type")):
        content_dict = json.loads(resp.content)

        for key in WKP_SUMMARY_API_KEYS_2_TRANSC:
            if key in content_dict:
                content_dict[key] = transcribe(content_dict[key])

        content = json.dumps(content_dict, ensure_ascii=False).encode("utf-8")
    elif resp.headers.get("Content-Type") == WKP_CT_HTML:
        content = transcribe_html(resp.content.decode("utf-8"), url_path).encode("utf-8")
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

    user_agent = request.headers.get("User-Agent")

    if request.query_string:
        query_string_decoded = request.query_string.decode("utf-8")
        target_url = f"{target_url}?{query_string_decoded}"
        resp = http_method(target_url, headers={"User-Agent": user_agent})
    elif request.json:
        data = request.json
        resp = http_method(target_url, json=data, headers={"User-Agent": user_agent})

    elif request.form:
        data = request.form.to_dict()
        resp = http_method(target_url, data=data, headers={"User-Agent": user_agent})
    else:
        resp = http_method(target_url, headers={"User-Agent": user_agent})

    content = prepare_content(resp, url_path)
    return Response(content, content_type=resp.headers.get("Content-Type"), headers={"User-Agent": user_agent})


if __name__ == '__main__':
    flask_app.run(debug=False, host="0.0.0.0", port=5000)

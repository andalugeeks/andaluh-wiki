# CSS. Reusing Pure-CSS-Floating-Action and SharingButtons (legal notices inside)
HEAD = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.8.1/css/all.min.css'>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<!-- Following css style block is Copyright (c) 2020 by Jones  Joseph (https://codepen.io/jo_Geek/pen/gyrZWW) -->
<style>
* {
  box-sizing: border-box;
}

.fab-wrapper {
  position: fixed;
  bottom: 3rem;
  right: 3rem;
}
.fab-checkbox {
  display: none;
}
.fab {
  position: absolute;
  bottom: -1rem;
  right: -1rem;
  width: 4rem;
  height: 4rem;
  background: blue;
  border-radius: 50%;
  background: #5FBB46;
  box-shadow: 0px 5px 20px #026632;
  transition: all 0.3s ease;
  z-index: 1;
  border-bottom-right-radius: 6px;
  border: 1px solid #8CC63E;
  cursor: pointer;
}

.fab:before {
  content: "";
  position: absolute;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.1);
}
.fab-checkbox:checked ~ .fab:before {
  width: 90%;
  height: 90%;
  left: 5%;
  top: 5%;
  background-color: rgba(255, 255, 255, 0.2);
}
.fab:hover {
  background: #026632;
  box-shadow: 0px 5px 20px 5px #81a4f1;
}

.fab-dots {
  position: absolute;
  height: 8px;
  width: 8px;
  background-color: white;
  border-radius: 50%;
  top: 50%;
  transform: translateX(0%) translateY(-50%) rotate(0deg);
  opacity: 1;
  animation: blink 3s ease infinite;
  transition: all 0.3s ease;
}

.fab-dots-1 {
  left: 15px;
  animation-delay: 0s;
}
.fab-dots-2 {
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  animation-delay: 0.4s;
}
.fab-dots-3 {
  right: 15px;
  animation-delay: 0.8s;
}

.fab-checkbox:checked ~ .fab .fab-dots {
  height: 6px;
}

.fab .fab-dots-2 {
  transform: translateX(-50%) translateY(-50%) rotate(0deg);
}

.fab-checkbox:checked ~ .fab .fab-dots-1 {
  width: 32px;
  border-radius: 10px;
  left: 50%;
  transform: translateX(-50%) translateY(-50%) rotate(45deg);
}
.fab-checkbox:checked ~ .fab .fab-dots-3 {
  width: 32px;
  border-radius: 10px;
  right: 50%;
  transform: translateX(50%) translateY(-50%) rotate(-45deg);
}

@keyframes blink {
  50% {
    opacity: 0.25;
  }
}

.fab-checkbox:checked ~ .fab .fab-dots {
  animation: none;
}

.fab-wheel {
  position: absolute;
  bottom: 0;
  right: 0;
  border: 1px solid #;
  width: 10rem;
  height: 10rem;
  transition: all 0.3s ease;
  transform-origin: bottom right;
  transform: scale(0);
}

.fab-checkbox:checked ~ .fab-wheel {
  transform: scale(1);
}
.fab-action {
  position: absolute;
  background: #8CC63E;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: White;
  box-shadow: 0 0.1rem 1rem rgba(24, 66, 154, 0.82);
  transition: all 1s ease;

  opacity: 0;
}

.fab-checkbox:checked ~ .fab-wheel .fab-action {
  opacity: 1;
}

.fab-action:hover {
  background-color: #8CC63E;
}

.fab-wheel .fab-action-1 {
  right: -1rem;
  top: 0;
}

.fab-wheel .fab-action-2 {
  right: 3.4rem;
  top: 0.5rem;
}
.fab-wheel .fab-action-3 {
  left: 0.5rem;
  bottom: 3.4rem;
}
.fab-wheel .fab-action-4 {
  left: 0;
  bottom: -1rem;
}

.resp-sharing-button__link,
.resp-sharing-button__icon {
  display: inline-block
}
</style>

<!-- Following style block is https://sharingbuttons.io/ (MIT license) -->
<style>
.resp-sharing-button__link {
  text-decoration: none;
  color: #fff;
  margin: 0.5em
}

.resp-sharing-button {
  border-radius: 5px;
  transition: 25ms ease-out;
  padding: 0.5em 0.75em;
  font-family: Helvetica Neue,Helvetica,Arial,sans-serif
}

.resp-sharing-button__icon svg {
  width: 1em;
  height: 1em;
  margin-right: 0.4em;
  vertical-align: top
}

.resp-sharing-button--small svg {
  margin: 0;
  vertical-align: middle
}

/* Non solid icons get a stroke */
.resp-sharing-button__icon {
  stroke: #fff;
  fill: none
}

/* Solid icons get a fill */
.resp-sharing-button__icon--solid,
.resp-sharing-button__icon--solidcircle {
  fill: #fff;
  stroke: none
}

.resp-sharing-button--twitter {
  background-color: #55acee
}

.resp-sharing-button--twitter:hover {
  background-color: #2795e9
}

.resp-sharing-button--pinterest {
  background-color: #bd081c
}

.resp-sharing-button--pinterest:hover {
  background-color: #8c0615
}

.resp-sharing-button--facebook {
  background-color: #3b5998
}

.resp-sharing-button--facebook:hover {
  background-color: #2d4373
}

.resp-sharing-button--tumblr {
  background-color: #35465C
}

.resp-sharing-button--tumblr:hover {
  background-color: #222d3c
}

.resp-sharing-button--reddit {
  background-color: #5f99cf
}

.resp-sharing-button--reddit:hover {
  background-color: #3a80c1
}

.resp-sharing-button--google {
  background-color: #dd4b39
}

.resp-sharing-button--google:hover {
  background-color: #c23321
}

.resp-sharing-button--linkedin {
  background-color: #0077b5
}

.resp-sharing-button--linkedin:hover {
  background-color: #046293
}

.resp-sharing-button--email {
  background-color: #777
}

.resp-sharing-button--email:hover {
  background-color: #5e5e5e
}

.resp-sharing-button--xing {
  background-color: #1a7576
}

.resp-sharing-button--xing:hover {
  background-color: #114c4c
}

.resp-sharing-button--whatsapp {
  background-color: #25D366
}

.resp-sharing-button--whatsapp:hover {
  background-color: #1da851
}

.resp-sharing-button--hackernews {
background-color: #FF6600
}
.resp-sharing-button--hackernews:hover, .resp-sharing-button--hackernews:focus {   background-color: #FB6200 }

.resp-sharing-button--vk {
  background-color: #507299
}

.resp-sharing-button--vk:hover {
  background-color: #43648c
}

.resp-sharing-button--facebook {
  background-color: #3b5998;
  border-color: #3b5998;
}

.resp-sharing-button--facebook:hover,
.resp-sharing-button--facebook:active {
  background-color: #2d4373;
  border-color: #2d4373;
}

.resp-sharing-button--twitter {
  background-color: #55acee;
  border-color: #55acee;
}

.resp-sharing-button--twitter:hover,
.resp-sharing-button--twitter:active {
  background-color: #2795e9;
  border-color: #2795e9;
}

.resp-sharing-button--whatsapp {
  background-color: #25D366;
  border-color: #25D366;
}

.resp-sharing-button--whatsapp:hover,
.resp-sharing-button--whatsapp:active {
  background-color: #1DA851;
  border-color: #1DA851;
}

.resp-sharing-button--telegram {
  background-color: #54A9EB;
}

.resp-sharing-button--telegram:hover {
  background-color: #4B97D1;}
</style>
'''

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

# Contains the flating action button + disclaimer modal (bootstrap).
BODY = '''
<div id="andalugeeksModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="andalugeeksModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="andalugeeksModalTitle"><strong>🇳🇬 AndaluWiki 🇳🇬</strong></h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
        </div>
        <div class="modal-body">
            <p>
                Bienvenida/o a AndaluWiki, una aplicación de <a href="https://andaluh.es" target="_blank">AndaluGeeks</a> que <strong>transcribe 
                Wikipedia a <a href="https://andaluhepa.wordpress.com/acerca-de/" target="_blank">Andalûh EPA</a> en tiempo real</strong>. 
                Es un proyecto independiente de Wikipedia. Reutilizamos sus contenidos gracias a <a href="https://es.wikipedia.org/wiki/Wikipedia:Texto_de_la_Licencia_Creative_Commons_Atribuci%C3%B3n-CompartirIgual_3.0_Unported" target="_blank">su licencia Creative Commons</a>.</p>
            <p>ℹ️ Haz clic para conocer más sobre <a href="https://andaluh.es/wikipedia-andaluz" target="_blank"AndaluWiki.</a></p>
            <p>ℹ️ Visita el resto de proyectos de <a href="https://andaluh.es" target="_blank">AndaluGeeks</a>.</p>

            <p><strong>¡Comparte este link en tus redes sociales!</strong>.</p>
            <div align="center">
                <!-- Sharingbutton Facebook -->
                <a id="smsharing-fb" class="resp-sharing-button__link" href="https://facebook.com/sharer/sharer.php?u=" target="_blank" rel="noopener" aria-label="">
                <div class="resp-sharing-button resp-sharing-button--facebook resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18.77 7.46H14.5v-1.9c0-.9.6-1.1 1-1.1h3V.5h-4.33C10.24.5 9.5 3.44 9.5 5.32v2.15h-3v4h3v12h5v-12h3.85l.42-4z"/></svg>
                    </div>
                </div>
                </a>

                <!-- Sharingbutton Twitter -->
                <a id="smsharing-tw" class="resp-sharing-button__link" href="https://twitter.com/intent/tweet/?url=" target="_blank" rel="noopener" aria-label="">
                <div class="resp-sharing-button resp-sharing-button--twitter resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M23.44 4.83c-.8.37-1.5.38-2.22.02.93-.56.98-.96 1.32-2.02-.88.52-1.86.9-2.9 1.1-.82-.88-2-1.43-3.3-1.43-2.5 0-4.55 2.04-4.55 4.54 0 .36.03.7.1 1.04-3.77-.2-7.12-2-9.36-4.75-.4.67-.6 1.45-.6 2.3 0 1.56.8 2.95 2 3.77-.74-.03-1.44-.23-2.05-.57v.06c0 2.2 1.56 4.03 3.64 4.44-.67.2-1.37.2-2.06.08.58 1.8 2.26 3.12 4.25 3.16C5.78 18.1 3.37 18.74 1 18.46c2 1.3 4.4 2.04 6.97 2.04 8.35 0 12.92-6.92 12.92-12.93 0-.2 0-.4-.02-.6.9-.63 1.96-1.22 2.56-2.14z"/></svg>
                    </div>
                </div>
                </a>

                <!-- Sharingbutton WhatsApp -->
                <a id="smsharing-wa" class="resp-sharing-button__link" href="whatsapp://send?text=" target="_blank" rel="noopener" aria-label="">
                <div class="resp-sharing-button resp-sharing-button--whatsapp resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20.1 3.9C17.9 1.7 15 .5 12 .5 5.8.5.7 5.6.7 11.9c0 2 .5 3.9 1.5 5.6L.6 23.4l6-1.6c1.6.9 3.5 1.3 5.4 1.3 6.3 0 11.4-5.1 11.4-11.4-.1-2.8-1.2-5.7-3.3-7.8zM12 21.4c-1.7 0-3.3-.5-4.8-1.3l-.4-.2-3.5 1 1-3.4L4 17c-1-1.5-1.4-3.2-1.4-5.1 0-5.2 4.2-9.4 9.4-9.4 2.5 0 4.9 1 6.7 2.8 1.8 1.8 2.8 4.2 2.8 6.7-.1 5.2-4.3 9.4-9.5 9.4zm5.1-7.1c-.3-.1-1.7-.9-1.9-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.1-.2.2-.3.2-.6.1s-1.2-.5-2.3-1.4c-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6s.3-.3.4-.5c.2-.1.3-.3.4-.5.1-.2 0-.4 0-.5C10 9 9.3 7.6 9 7c-.1-.4-.4-.3-.5-.3h-.6s-.4.1-.7.3c-.3.3-1 1-1 2.4s1 2.8 1.1 3c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.3.2-.7.2-1.2.2-1.3-.1-.3-.3-.4-.6-.5z"/></svg>
                    </div>
                </div>
                </a>

                <!-- Sharingbutton Telegram -->
                <a id="smsharing-tg" class="resp-sharing-button__link" href="https://telegram.me/share/url?url=" target="_blank" rel="noopener" aria-label="">
                <div class="resp-sharing-button resp-sharing-button--telegram resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solid">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M.707 8.475C.275 8.64 0 9.508 0 9.508s.284.867.718 1.03l5.09 1.897 1.986 6.38a1.102 1.102 0 0 0 1.75.527l2.96-2.41a.405.405 0 0 1 .494-.013l5.34 3.87a1.1 1.1 0 0 0 1.046.135 1.1 1.1 0 0 0 .682-.803l3.91-18.795A1.102 1.102 0 0 0 22.5.075L.706 8.475z"/></svg>
                    </div>
                </div>
                </a>
            </div>

        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
        </div>
        </div>
    </div>
</div>


<div class="fab-wrapper">
    <input id="fabCheckbox" class="fab-checkbox" data-toggle="modal" data-target="#andalugeeksModal"/>
  <label class="fab" for="fabCheckbox">
    <span class="fab-dots fab-dots-1"></span>
    <span class="fab-dots fab-dots-2"></span>
    <span class="fab-dots fab-dots-3"></span>
  </label>
</div>

<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?always=1&privacyPage=https%3A%2F%2Fandaluh.es%2Fpolitica-privacidad%2F"></script>
<script>
    var x = window.location.href;
    document.getElementById("smsharing-fb").href += x;
    document.getElementById("smsharing-tw").href += x;
    document.getElementById("smsharing-wa").href += x;
    document.getElementById("smsharing-tg").href += x;
</script>
'''

WP_ES_LINK = '''
<li class="interlanguage-link interwiki-es"><a class="interlanguage-link-target" href="https://es.wikipedia.org/[ARTICLE_PATH]" hreflang="es" title="êppañôh" lang="es">Êppañôh</a></li>
'''

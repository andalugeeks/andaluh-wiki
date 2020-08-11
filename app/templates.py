HEAD = '''
<!--Import Google Icon Font-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<!--Let browser know website is optimized for mobile-->
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
'''

# Adjust your Google Analytics ID with GA_TRACK_UA environment variable
GA_TRACKING_HEADER='''
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_TRACK_UA}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '{GA_TRACK_UA}');
</script>
'''

BODY='''
<div id="andalugeeksModal" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="andalugeeksModalTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="andalugeeksModalTitle">Biembenío/a a <strong>Wikipedia Andalûh 🇳🇬</strong></h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
            </button>
        </div>
        <div class="modal-body">
            <p>
                Wikipedia Andalûh es una aplicación de <a href="https://andaluh.es" target="_blank">AndaluGeeks</a> que <strong>transcribe 
                Wikipedia a <a href="https://andaluh.es/epa" target="_blank">Andalûh EPA</a> en tiempo real</strong>. 
                No contamos con el apoyo de Wikipedia ni mantenemos ninguna relación con ellos para este proyecto.</p>
            <p>ℹ️ Haz clic para conocer más sobre <a href="https://andaluh.es/wikipedia-andaluh" target="_blank"> Wikipedia Andalûh.</a></p>
            <p>ℹ️ Visita el resto de proyectos de <a href="https://andaluh.es" target="_blank">AndaluGeeks</a>.</p>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
        </div>
        </div>
    </div>
    </div>

    <div class="fixed-action-btn" data-toggle="modal" data-target="#andalugeeksModal">
    <a class="btn-floating btn-large green">
        <i class="large material-icons">info</i>
    </a>
</div>

<!-- Compiled and minified JavaScript -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
'''
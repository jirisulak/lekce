from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "stranka/index.html")

from datetime import datetime

def ziskej_denni_dobu():
    aktualni_cas = datetime.now()
    hodina = aktualni_cas.hour

    if 5 <= hodina < 12:
        return 'ráno'
    elif 12 <= hodina < 18:
        return 'odpoledne'
    else:
        return 'večer'
    


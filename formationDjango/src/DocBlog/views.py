from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


#  Pour renvoyer une vue, on créé une fonction prennant en paramètre la requête du navigateur
def index(request):

    date = datetime.today()

    return render(request, "index.html", context={"surnom": "Ryu", "date": date})
    # return HttpResponse("<h1>Bonjour, bienvenue sur mon site</h1>") pour renvoyer de l'HTML basique

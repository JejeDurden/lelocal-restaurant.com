from django.shortcuts import render
from django.conf import settings
from .models import Entrée, Plat, Dessert


def index(request):
    return render(request, 'app/index.html')

def carte(request):
    entree = Entrée.objects.all()
    plat = Plat.objects.all()
    dessert = Dessert.objects.all()
    context = {'entree': entree, 'plat': plat, 'dessert': dessert}
    return render(request, 'app/carte.html', context)

def contact(request):
    return render(request, 'app/contact.html')

def edito(request):
    return render(request, 'app/edito.html')

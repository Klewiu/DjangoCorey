from django.shortcuts import render
from django.http import HttpResponse

def home(request): #definiujemy funkcje home która będzie domyslnie otwierana na stronie
    return HttpResponse('<h1> Blog Home </h1>')

def about(request): #definiujemy funkcje about
    return HttpResponse('<h1> Blog About </h1>')


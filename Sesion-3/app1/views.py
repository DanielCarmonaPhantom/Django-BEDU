from django.shortcuts import render

# Create your views here.

def index(request):
    """ Muestra las canciones"""
    return render(request, 'app1/index.html')

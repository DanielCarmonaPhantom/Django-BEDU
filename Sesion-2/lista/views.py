from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

lista_compras = {
    # "mamá": ["piña", "leche"],
    # "papá": []
}

def mostrar_listas(request):
    '''
    Mostrar lisas disponibles 
    '''    
    context = {'listas': lista_compras.keys()}
    return  render(request, 'mostrar_listas.html', context)
    # return HttpResponse("Hola Mundo")

def crear_lista(request):
    '''
    Crear una nueva lista vacía
    '''
    context = {}

    if request.method == 'POST':
        nombre = request.POST['name']
        elementos = request.POST['elementos']
        if nombre in lista_compras:
            context['error'] = 'Ya existe esta lista'
        else:
            lista_compras[nombre] = elementos.split()
            return redirect("lista:mostrar_listas")

    return render(request, 'crear_lista.html',context)

def mostrar_lista(request, nombre):
    '''
    Mostrar contenido lista 
    '''
    context = {
        'name': nombre,
        'datos': lista_compras[nombre]
    }

    return render(request, "mostrar_lista.html", context) 
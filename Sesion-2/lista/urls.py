from django.contrib import admin
from django.urls import path, include

from .import views

app_name='lista'

urlpatterns = [
    path("mostrar/", views.mostrar_listas, name="mostrar_listas"),
    path("crear/", views.crear_lista, name="crear_lista"),
    path("mostrar/<str:nombre>", views.mostrar_lista, name="mostrar_lista")
]

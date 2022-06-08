"""Music app url config"""

from django.contrib import admin
from django.urls import path

from .views import index

app_name = 'app1'
urlpatterns = [
    path('', index, name='index'),
]

# map/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('forest/', views.forest_view, name='forest'),
    path('rando/', views.rando_view, name='rando')
]
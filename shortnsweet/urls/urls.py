from django.urls import path

from . import views

appname = "shortnsweet"

urlpattens = [
    path('', views.home_view, name='home')

]
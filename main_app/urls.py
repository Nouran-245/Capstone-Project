from django.urls import path
from . import views

urlpatterns = [
    # '' means root url and any things wriiten in means this is the path for this page that i have to write after localhost:8000/ to reach the page
    # views.home => this home refers to the function home in views.py
    # name='home' => this is used to refer this url in html files using {% url 'home' %}

    
    path('', views.base , name='base'),
    # path('home/', views.home , name='home'),
]
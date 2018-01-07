from django.urls import path

from . import views

urlpatterns = [
    path('', views.vote, name='vote'),

]
#this is to define the path

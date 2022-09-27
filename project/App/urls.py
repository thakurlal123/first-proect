from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("", views.index, name='index'),
    path("link.html", views.link, name='link'),
    path("Meetings.html", views.Meetings, name='Meetings'),
  
]
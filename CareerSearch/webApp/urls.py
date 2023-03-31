from django.contrib import admin
from django.urls import path
from webApp import views
urlpatterns = [
    path("", views.index, name='home'),
    path("occupations", views.occupations, name='occupations'),
    path("softwareEngineer", views.softwareEngineer, name='softwareEngineer'),
    path("doctor", views.doctor, name='doctor'),
    path("actuary", views.actuary, name='actuary'),
    path("mediaAnalyst", views.mediaAnalyst, name='mediaAnalyst'),
]
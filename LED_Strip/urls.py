from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('updatergb', views.updatergb),
    path('updatepower', views.updatepower),
    path('senddata', views.senddata),
]

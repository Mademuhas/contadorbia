from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contador', views.PrincipalView.as_view(), name='contador'),
]
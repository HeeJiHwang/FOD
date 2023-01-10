from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkin_before),
    path('success/', views.checkin_suc),
    path('boardingpass/' , views.boardingpass),
    path('checkin/', views.checkin),
]
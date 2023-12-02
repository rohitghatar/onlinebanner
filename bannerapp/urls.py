from django.contrib import admin
from django.urls import path
from bannerapp import views

urlpatterns = [
    path('',views.index),
]

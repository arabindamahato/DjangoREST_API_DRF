from django.contrib import admin
from django.urls import path, include
from .views import TestApiView
from . import views

urlpatterns = [
    path('apiview/', TestApiView.as_view()),

]

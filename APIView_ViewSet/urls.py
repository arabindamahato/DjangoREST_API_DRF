from django.contrib import admin
from django.urls import path, include
from .views import TestApiView
from . import views

urlpatterns = [
    path('test-api-view/', TestApiView.as_view()),

]

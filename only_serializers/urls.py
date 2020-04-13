from django.urls import path
from .views import EmployeeCRUDCBV
from . import views


urlpatterns = [
    path('only_serializers/', views.EmployeeCRUDCBV.as_view()),

]

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Teacher
from .serializers import TeacherSerializer

# Pagination For Locally
from .pagination import (
							MyPagination, 
							MyPagination2, 
							MyPagination3,
						)

# Pagination For Globally
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class TeacherListView(ListAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer
	pagination_class = PageNumberPagination  # Pagination For Globally 
	# pagination_class = MyPagination  # Pagination For Locally 
	# pagination_class = MyPagination2  # Pagination For Locally 
	# pagination_class = MyPagination3  # Pagination For Locally 

	

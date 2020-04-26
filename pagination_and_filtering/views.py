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


	search_fields = ('tno','tname') #  It returns all Teachers records where tno &tname contains '2'
								    # http://127.0.0.1:8000/api4/pagination/?search=2 ,
	# search_fields = ('^tname',) # It returns all Teachers records where tno is starts with 'A' 
								# http://127.0.0.1:8000/api4/pagination/?search=A 
	# search_fields=('=tno',) # It returns all Teachers records where tno is exactly equals to  '4'
	                        #  http://127.0.0.1:8000/api4/pagination/?search=4 

	ordering_fields = ('tno',)  # Default value is '__all__'

	''' 
	Ordering Fields:
	Client can send request with search and ordering parameters as follows
	http://127.0.0.1:8000/api4/pagination/?mysearch=R 
	http://127.0.0.1:8000/api4/pagination/?myordering=-tno 
	http://localhost:8000/api4/pagination/?mysearch=R&myordering=-tno
	 '''

	

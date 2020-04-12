from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 

# Create your views here.
class TestApiView(APIView):
	def get(self, request, *args, **kwargs):
		colors = ['yellow','green','red','gray','blue']
		return Response({'msg':'Happy Coding', 'colors':colors})



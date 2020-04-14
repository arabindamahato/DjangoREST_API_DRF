from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from apiview_viewset_with_models.models import Employee2
from apiview_viewset_with_models.serializers import Employee2Serializer

#=============================================================
# class EmployeeListAPIView(APIView):
# 	def get(self, request, format=None):
# 		qs = Employee2.objects.all()
# 		serializer = Employee2Serializer(qs, many=True)
# 		return Response(serializer.data)
#===================================================Inside box upper and lower codes returns the same results
# class EmployeeListAPIView(ListAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer
#==============================================================

class EmployeeListAPIView(ListAPIView):
	# queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer
	def get_queryset(self):
		qs = Employee2.objects.all()
		name = self.request.GET.get('ename')
		if name is not None:
			qs = qs.filter(ename__icontains=name)
		return qs


class EmployeeCreateAPIView(CreateAPIView):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer


		

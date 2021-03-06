from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from apiview_viewset_with_models.models import Employee2
from apiview_viewset_with_models.serializers import Employee2Serializer
from rest_framework.generics import  (ListAPIView,
									 CreateAPIView,
									 RetrieveAPIView,
									 UpdateAPIView,
									 DestroyAPIView,
									 ListCreateAPIView,
									 RetrieveUpdateAPIView,
									 RetrieveDestroyAPIView,
									 RetrieveUpdateDestroyAPIView )

from rest_framework import mixins
from rest_framework.mixins import (CreateModelMixin,
	                               UpdateModelMixin,
	                               DestroyModelMixin,
	                                )
# Token Authentication Class
from rest_framework.authentication import TokenAuthentication

# JSONWebToken Authentication Class
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# Basic Authentication Class
from rest_framework.authentication import BasicAuthentication


# Custom Authentication Class
from .authentications import CustomAuthentication
from .authentications import CustomAuthentication2

# Permissions Classes
from rest_framework.permissions import (
	                                   IsAuthenticated,
                                       AllowAny,
                                       IsAdminUser,
                                       IsAuthenticatedOrReadOnly,
                                       DjangoModelPermissions,
                                       DjangoModelPermissionsOrAnonReadOnly,
                                       )

from .permissions import IsReadOnly, IsGetOrPatch, IsArabinda


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




#====================================Only APIView without Mixins=============================



# class EmployeeListAPIView(ListAPIView):
# 	# queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer
# 	def get_queryset(self):
# 		qs = Employee2.objects.all()
# 		name = self.request.GET.get('ename')
# 		if name is not None:
# 			qs = qs.filter(ename__icontains=name)
# 		return qs


# class EmployeeCreateAPIView(CreateAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

# class EmployeeRetrieveAPIView(RetrieveAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

# class EmployeeUpdateAPIView(UpdateAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

# class EmployeeDestroyAPIView(DestroyAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

class EmployeeListCreateAPIView(ListCreateAPIView):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer

# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
# 	queryset = Employee2.objects.all()
# 	serializer_class = Employee2Serializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer




#==========================================APIView With Mixins==================================





class EmployeeListCreate(ListAPIView, CreateModelMixin):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class EmployeeDetailAPIViewMixin(RetrieveAPIView, UpdateModelMixin, DestroyModelMixin):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	def patch(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)




#====================================ViewSet with model with authentication===========================================

from rest_framework.viewsets import ModelViewSet

class EmployeeModelViewSet(ModelViewSet):
	queryset = Employee2.objects.all()
	serializer_class = Employee2Serializer
	# authentication_classes = [TokenAuthentication,]
	# authentication_classes = [JSONWebTokenAuthentication,]
	authentication_classes = [BasicAuthentication,]
	permission_classes = [IsAuthenticated,]
	# permission_classes = [AllowAny,]
	# permission_classes = [IsAdminUser,]
	# permission_classes = [IsAuthenticatedOrReadOnly,]
	# permission_classes = [DjangoModelPermissions,]
	# permission_classes = [DjangoModelPermissionsOrAnonReadOnly,]
	# permission_classes = [IsReadOnly,]
	# permission_classes = [IsGetOrPatch,]
	# permission_classes = [IsArabinda,]

    







		

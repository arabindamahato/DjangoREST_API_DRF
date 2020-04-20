"""djangorestapidrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from only_serializers import views
from APIView_ViewSet.views import TestViewSet
from apiview_viewset_with_models.views import EmployeeModelViewSet
from rest_framework.routers import DefaultRouter

# Here we need to register our view class name.
router = DefaultRouter()
#==========ViewSet without model==========
router.register('test-view-set', TestViewSet, basename='test-view-set')

#==========ViewSet with model==========
router.register('model-view-set', EmployeeModelViewSet) # Here base_name is not required
                                                        # because this is model ViewSet


urlpatterns = [
    # This url mapping is for ViewSet functionality
    path('api2/', include(router.urls)),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # """ only_serializer app"""
    path('api/',include('only_serializers.urls')), 

    # """APIView_ViewSet app"""
    # This url mapping is for APIView functionality
    path('api2/',include('APIView_ViewSet.urls')),
    

    # """ apiview_viewset_with_models app"""
    # This url mapping is for APIView functionality with Model
    path('api3/', include('apiview_viewset_with_models.urls')),





]

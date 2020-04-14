from django.urls import path
from apiview_viewset_with_models import views

urlpatterns = [
	path('apiview-with-models-list/', views.EmployeeListAPIView.as_view()),
	path('apiview-with-models-create/', views.EmployeeCreateAPIView.as_view()),
]
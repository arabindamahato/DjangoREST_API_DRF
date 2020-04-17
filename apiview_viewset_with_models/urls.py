from django.urls import path
from apiview_viewset_with_models import views

urlpatterns = [
	# path('apiview-list/', views.EmployeeListAPIView.as_view()),
	# path('apiview-create/', views.EmployeeCreateAPIView.as_view()),
	# path('apiview-retrieve/<pk>/', views.EmployeeRetrieveAPIView.as_view()),
	# path('apiview-update/<pk>/', views.EmployeeUpdateAPIView.as_view()),
	path('apiview-listcreate/', views.EmployeeListCreateAPIView.as_view()),
	# path('apiview-retrieveupdate/<pk>', views.EmployeeRetrieveUpdateAPIView.as_view()),
	# path('apiview-retrievedestroy/<pk>', views.EmployeeRetrieveDestroyAPIView.as_view()),
	path('apiview-retrieveupdatedestroy/<pk>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),


	
	# With Mixin [api3]	
	path('apiview-listcreate-modelmixin/', views.EmployeeListCreate.as_view()),
	path('apiview-detail-modelmixin/<pk>/', views.EmployeeDetailAPIViewMixin.as_view()),



	# """ For ViewSet functionality app level url is not required. """

]



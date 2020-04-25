from django.urls import path
from pagination_and_filtering.views import TeacherListView

urlpatterns=[
	path('pagination/',TeacherListView.as_view()),

	
]

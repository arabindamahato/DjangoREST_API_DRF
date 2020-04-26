from django.urls import path
from . import views


urlpatterns = [
    path('author-api/', views.AuthorListView.as_view()),
    path('author-api/<pk>/', views.AuthorView.as_view()),

    path('book-api/', views.BookListView.as_view()),
    path('book-api/<pk>/', views.BookView.as_view()),

]

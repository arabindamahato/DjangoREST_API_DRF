from rest_framework import serializers
from nested_serializers.models import Author, Book 


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
	books_by_author = BookSerializer(read_only=True, many=True) # Specially this line is important for nested serializers
	class Meta:
		model = Author
		fields = '__all__'

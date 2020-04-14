from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apiview_viewset_with_models.models import Employee2

class Employee2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Employee2 
		fields = '__all__'
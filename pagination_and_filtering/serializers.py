from pagination_and_filtering.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		fields = '__all__'
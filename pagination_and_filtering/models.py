from django.db import models

# Create your models here.

class Teacher(models.Model):
	tno=models.IntegerField()
	tname=models.CharField(max_length=64)
	tsal=models.FloatField()
	taddr=models.CharField(max_length=64)

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangorestapidrf.settings')
import django
django.setup()

from pagination_and_filtering.models import *
from faker import Faker
from random import *
faker=Faker()  

def populate(n):
	for i in range(n):
		ftno=randint(1001,9999)
		ftname=faker.name()
		ftsal=randint(10000,20000)
		ftaddr=faker.city()
		teacher_record=Teacher.objects.get_or_create(tno=ftno,tname=ftname,tsal=ftsal,taddr=ftaddr)
populate(120)   
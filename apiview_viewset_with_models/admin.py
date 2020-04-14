from django.contrib import admin
from apiview_viewset_with_models.models import Employee2

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id','eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee2, EmployeeAdmin)

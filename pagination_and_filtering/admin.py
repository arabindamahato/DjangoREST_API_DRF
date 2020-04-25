from django.contrib import admin
from pagination_and_filtering.models import Teacher

# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
	list_display = ['id','tno', 'tname', 'tsal', 'taddr']

admin.site.register(Teacher, TeacherAdmin)

from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from only_serializers.models import Employee
from only_serializers.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 

from django.utils.decorators import method_decorator 

# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(View):
	def get(self,request,*args,**kwargs):
		json_data=request.body 
		stream=io.BytesIO(json_data)  # It converting from complex datatype(qs, modelobj, objdata etc) to
									  # python native datatypes(dict, list, str etc) (Which comes from database)
		data=JSONParser().parse(stream) # It converts the data into python dict
		id=data.get('id',None)
		if id is not None:
			emp=Employee.objects.get(id=id) # emp variable contain a particular emp obj (means database supported complex datatype) 
			serializer=EmployeeSerializer(emp) # serializer variable contain python native data .
			json_data=JSONRenderer().render(serializer.data) # render converts the python native datatype to Json data
			return HttpResponse(json_data,content_type='application/json')
		qs=Employee.objects.all()
		serializer=EmployeeSerializer(qs,many=True)
		json_data=JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json')



	def post(self,request,*args,**kwargs):
		json_data=request.body  # getting data from client application
		stream=io.BytesIO(json_data) # this line and next line convert from json data to 
		pdata=JSONParser().parse(stream) # python data.
		serializer=EmployeeSerializer(data=pdata)
		if serializer.is_valid():
			serializer.save()
			msg={'msg':'Resource Created Succesfully'}
			json_data=JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json') 




	def put(self,request,*args,**kwargs):
		json_data=request.body
		stream=io.BytesIO(json_data)
		data=JSONParser().parse(stream)
		id=data.get('id')
		emp=Employee.objects.get(id=id)
		serializer=EmployeeSerializer(emp,data=data,partial=True)
		if serializer.is_valid():
			serializer.save()
			msg={'msg':'Resource Updated Succesfully'}
			json_data=JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type='application/json')
		json_data=JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type='application/json') 



	def delete(self, request, *arks, **kwargs):
		json_data = request.body
		stream=io.BytesIO(json_data)
		pdata = JSONParser().parse(stream)
		id = pdata.get('id')
		emp = Employee.objects.get(id=id)
		emp.delete()
		msg = {'msg':'Resource deleted successfully'}
		json_data = JSONRenderer().render(msg)
		return HttpResponse(json_data, content_type='application/json')
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from APIView_ViewSet.serializers import NameSerializer

# Create your views here.
class TestApiView(APIView):
	def get(self, request, *args, **kwargs):
		colors = ['yellow','green','red','gray','blue']
		return Response({'msg':'Happy Coding', 'colors':colors})

	def post(self, request, *args, **kwargs):
		# return Response({'msg':'This response is from post method of ApiView'})
		serializer = NameSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name') # here serializer.data means python dict
			msg = 'Hello {}, Happy Coding!..'.format(name)
			return Response({'msg': msg})
		else:
			return Response(serializer.errors, status=400)

	def put(self, request, *args, **kwargs):
		return Response({'msg':'This response is from put method of ApiView'})

	def patch(self, request, *args, **kwargs):
		return Response({'msg':'This response is from patch method of ApiView'})

	def delete(self, request, *args, **kwargs):
		return Response({'msg':'This response is from delete method of ApiView'})



from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
	def list(self, request):
		colors = ['yellow','green','red','gray','blue']
		return Response({'msg':'Happy Coding', 'colors':colors})







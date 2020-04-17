from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from APIView_ViewSet.serializers import NameSerializer
from rest_framework.viewsets import ViewSet


# Create your views here.
# ==========only ViewSet,  without model==========
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



class TestViewSet(ViewSet):
	def list(self, request):
		colors = ['yellow','green','red','gray','blue']
		return Response({'msg':'Happy Coding', 'colors':colors})

	def create(self, request):
		serializer = NameSerializer(data=request.data)
		if serializer.is_valid():
			name = serializer.data.get('name') # here serializer.data means python dict
			msg = 'Hello {}, Happy Morning!..'.format(name)
			return Response({'msg': msg})
		else:
			return Response(serializer.errors, status=400)

	def retrieve(self, request, pk=None):
		return Response({'msg':'This is from retrive method of ViewSet..'})

	def update(self, request, pk=None):
		return Response({'msg':'This is from partial_update method of ViewSet..'})

	def partial_update(self, request, pk=None):
		return Response({'msg':'This is from update method of ViewSet..'})

	def destroy(self, request, pk=None):
		return Response({'msg':'This is from destroy method of ViewSet..'})

	'''Note : At the time of testing in browser if you didn't find the last 4 allowed methods then 
		add a number after endpoint eg: localhost:8000/api/test-view-set/1 . Because last 4 methods 
		requires id/(pk) to perform operation'''








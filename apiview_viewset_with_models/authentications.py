from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
	def authenticate(self, request):
		'''I overriding this authenticate method from BaseAuthentication class
		Because I am doing custom authentication, we want to get complete control of 
		authentication in my hand.'''
		username = request.GET.get('username') # getting username from partner app
		if username is None:
			return None
		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			raise AuthenticationFailed('No such type of user./ Invalid Crediantials to access endpoints')
		return(user, None)



class CustomAuthentication2(BaseAuthentication):
	''' This is the endpoint to access this class by POSTMAN 
	 (http://localhost:8000/api2/model-view-set/?username=Arabinda&key=a7ZXA98)
	'''
	def authenticate(self,request):
		username=request.GET.get('username')
		key=request.GET.get('key')
		if username is None or key is None:
			return None
		c1=len(key) == 7
		c2=key[0]==username[-1].lower()        # username=Arabinda&key=a7ZXA98/
		c3=key[2]=='Z'
		c4=key[4]==username[0]
		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			raise AuthenticationFailed('Your provided username is  invalid,plz provide  valid username to access endpoint')
		if c1 and c2 and c3 and c4:
			return (user,None)
			raise AuthenticationFailed('Your provided key is  invalid,plz provide valid key to access endpoint')   
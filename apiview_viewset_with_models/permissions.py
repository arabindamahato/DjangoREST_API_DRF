from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsReadOnly(BasePermission):
	def has_permission(self, request, view):
		if request.method in SAFE_METHODS:
			return True
		else:
			return False



class IsGetOrPatch(BasePermission):
	def has_permission(self, request, view):
		allowed_methods = ['GET', 'PATCH']
		if request.method in allowed_methods:
			return True
		else:
			return False




'''
If the name is arabinda then allow all methods If the name is not arabinda and the name 
contains even number of characters then allow only SAFE_METHODS otherwise not allowed 
to perform any operation.
'''
class IsArabinda(BasePermission):
	def has_permission(self, request, view):
		user = request.user.username
		print(user)
		if user.lower() == 'arabinda':
			return True
		elif len(user) % 2 == 0 and user != '' and request.method in SAFE_METHODS:
			return True
		else:
			return False

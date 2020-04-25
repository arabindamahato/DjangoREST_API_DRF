'''
If you want to customize pagination , then only this module is required.
otherwise global pagination is applied in settings.py'''

from rest_framework import pagination
from rest_framework.pagination import (
	                                     PageNumberPagination,
	                                     LimitOffsetPagination,
	                                     CursorPagination,
	                                  )
class MyPagination(PageNumberPagination):
	page_size=5  # Each page 5 instances 
	# page_query_param='mypage'   # http://127.0.0.1:8000/api/?mypage=4  (default is 'page')
	# page_size_query_param='num'  #  http://127.0.0.1:8000/api/?required_page_size=10 
	# max_page_size=11
	# last_page_strings=('end_page',) # http://localhost:8000/api4/pagination/?page=end_page  (default is 'last')

class MyPagination2(LimitOffsetPagination):
	default_limit = 5
	limit_query_param='mylimit'   # http://localhost:8000/api4/pagination/?mylimit=20&myoffset=55
	offset_query_param='myoffset' # for limit (default is 'limit'), and for offset (default is 'offset')
	max_limit=20


class MyPagination3(CursorPagination):
	'''To get aAll records according to ascending
	 order of employee salaries but 5 resources per page. '''
	ordering='tsal' #based on ascending order of employee salaries
	page_size=5
	cursor_query_param='mycursor' 

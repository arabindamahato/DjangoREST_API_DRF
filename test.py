import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
import time

# time.sleep(5)
# print('get request')
def get_resources(id=None):
	data={}
	if id is not None:
		data={
			'id':id
		}

	response=requests.get(BASE_URL+ENDPOINT, data=json.dumps(data))
	print(response.status_code)
	print(response.json())
# get_resources(2)


# time.sleep(10)
# print('post request')

def create_resource():
	new_emp={
 		'eno':1012,
 		'ename':'monoj',
 		'esal':5700,
 		'eaddr':'Balarampur',
	}

	response=requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
	print(response.status_code)
	print(response.json())
# create_resource()


# time.sleep(15)
# print('update request')
def update_resource(id):
	new_data={
		'id':id,
		'ename':'Ramesh Mahato'
		}
	r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
	print(r.status_code)
	# print(r.text)
	print(r.json())
# update_resource(1)

# time.sleep(15)
# print('delete operation')
def delete_resource(id):
	data={
		'id':id,
		}
	r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
	print(r.status_code)
	# print(r.text)
	print(r.json()) 
delete_resource(3)

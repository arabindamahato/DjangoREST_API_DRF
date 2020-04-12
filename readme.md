###### Here we will work on ###### 
###### 1.Database supported complex datatype ######
###### 2. Python native datatype ######
###### 3. Json datatype ######

* `Sometime we will convert (in get)
    1.complex to python   (Get data from database and convert into python native datatype)
    2.python to json      (Python native dataype to json because we need to send it to the client)
    [Basically GET Method follow this process]`

* `Sometime we will convert (in post)
    1. json to python     (accept from client app and convert into python. )
    2. python to complex  (after converting python stored into database.)
    [Basically POST Method follow this process]` 





###### Serialization ###### 
* `The process of converting complex datatypes(Queryset, ModelObject, ObjectType etc) to 
                             python Native(Dict, List etc) datatype .`

###### Complex ==> Python ######
###### ================== ######


###### Serialize Queryset ######

* `from rest_framework.renderers import JSONRenderer 
   qs = Employee.objects.all()
   serializer = EmployeeSerializer(qs, many=True)
   serializer.data 
   json_data = JSONRenderer().render(serializer.data)
   --->
    Here it converted into qs to python native data then 
    `

###### Serialize Particular Object ######
* `from rest_framework.renderers import JSONRenderer 
   emp = Employee.objects.get(id=1)
   serializer = EmployeeSerializer(emp)
   serializer.data 
   json_data = JSONRenderer().render(serializer.data)
   --->
    Here it converted into qs to python native data`


###### Deserialization ###### 
* `The process of converting python native datatype into database supported complex types is called Deserialization `

###### Python ==> Complex ######
###### ================== ######


* `
import io
from rest_framework.parsers import JSONParser
stream = io.BitesIO(json_data)  # Accept and convert the client data into bites andstored in stream var
pdata=JSONParser().parse(stream)  # here converted from bites data to python data
# By deserialization we have to convert python data to db supported complex type.
serializer = EmployeeSerializer(data=pdata) # hereconverted from python native to complex
serializer.is_valid()
serializer.validated_data  # validated_data is database supported form` 


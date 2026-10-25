#import requests
# above - Allows us to send HTTP requests.

#Get
#response = requests.get("http://127.0.0.1:8000/employees")
#response = requests.get("http://127.0.0.1:8000/employees/1")
#response = requests.get("http://127.0.0.1:8000/employees/99") #if it not data detail will show employee not found
#print(response.status_code)
#print(response.json())
#requests.get(...)	Sends a GET request to your API.
#response	Stores the API's reply.
#response.status_code	Shows whether the request succeeded.
#response.json()	Reads the response data as Python data.


#employees = response.json()

#print(employees[0]["name"])

##for employee in employees:
 #   print(employee["name"])


 #POST
 
#import requests

#employee_data = {
#    "name": "Sanaks",
#    "age": 26,
#    "role": "Python Developer"
#}

#response = requests.post(
#    "http://127.0.0.1:8000/employees",
 #   json=employee_data
#)

#print(response.status_code)
#print(response.json())



#PUT

#import requests

#updated_employee = {
#    "name": "Rahul",
 #   "age": 27,
  #  "role": "AI Developer"
#}

#response = requests.put(
 #   "http://127.0.0.1:8000/employees/3",
  #  json=updated_employee
#)

#print(response.status_code)
#print(response.json())

#DELETE

#import requests

#response = requests.delete(
 #   "http://127.0.0.1:8000/employees/4"
#)

#print(response.status_code)
#print(response.json())

#ERROR HANDLING
#import requests
#
#try:
 #   response = requests.get(
  #      "http://127.0.0.1:8000/employees",
   #     timeout=5
    #)
#
 #   response.raise_for_status()
  #  print(response.json())

#except requests.exceptions.RequestException:
 #   print("Could not connect to the employee API.")


#Example
import requests

try:
    response = requests.get(
        "http://127.0.0.1:8000/employees",
        timeout=5
    )
    print(response.json())

except requests.exceptions.RequestException:
    print("Could not connect to the employee API.")

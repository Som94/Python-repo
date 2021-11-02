import json
  
# JSON string
employee = '{"id":"09", "name": "Narayan Sharma", "department":"Finance"}'
  
# Convert string to Python dict
# CODE HERE 


# Convert Python dict to JSON
# CODE HERE 
#You11:45 AM

employee_json = json.loads(employee)
print(employee_json)
print(type(employee_json))
employee_json_dict=json.dumps(employee_json, indent=4)
print(employee_json_dict)
print(type(employee_json_dict))

#Json_file_read.py

 

import json

 

# JSON string

#employee ='{"id":"09", "name": "Narayan Sharma", "department":"Finance", "is_working": true, "hobbies": "{10:"abc"  20:"xyz"}" }'

#employee ='{"id":"09", "name": "Narayan Sharma", "department":"Finance", "is_working": true, "hobbies": ["abc","xyz"]}'

employee ='{"id":"09", "name": "Narayan Sharma", "department":"Finance", "is_working": true, "hobbies": {"10":"abc" ,"20":"xyz"}}'

# Convert string to Python dict

employee_dict = json.loads(employee)

print(employee_dict)

print(type(employee_dict))

print("\n")

 

# Convert Python dict to JSON

json_object = json.dumps(employee_dict, indent=5)

print(json_object)

print(type(json_object))

print ('---------------')

import json

 

# Opening JSON file

#f = open('C:\\July_2021_Python\\emp_data.json','r')

f = open('E:\\Aroha Tech\\Python Session\\10th Aug\\emp_data.json')

 

# returns JSON object as

# a dictionary

data = json.load(f)

 

# Iterating through the json

# list

for i in data['emp_details']:

               print(i)

 

# Closing file
f.close()

 

 



 


# function to add to JSON

def write_json(new_data, filename='emp_data.json'):

    with open(filename,'r+') as file:

          # First we load existing data into a dict.

        file_data = json.load(file)

        # Join new_data with file_data inside emp_details

        file_data["emp_details"].append(new_data)

        # Sets file's current position at offset.

        file.seek(0)

        # convert back to json.

        json.dump(file_data, file, indent = 4)


    # python object to be appended

y = {"emp_name":"Sushma Rao",

     "email": "sushma@yahoo.com",

     "job_profile": "Lead Analyst"

    }

    

write_json(y)
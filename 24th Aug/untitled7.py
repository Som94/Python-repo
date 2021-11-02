import requests

Base_url='http://127.0.0.1:8000/'
end_point='i/'

def request_data(id):
    resp=requests.get(Base_url+end_point+id+'/')
    
    data=resp.json()
    print(resp.status_code)
    print(data)
id=input("Enter id :")
request_data(id)
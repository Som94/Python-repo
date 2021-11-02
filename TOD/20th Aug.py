#Serial_deserial_demo.py

 

import pickle

 

class Product:

    def __init__(self,pid,nm,cp):

        self.prod_id=pid

        self.prod_name=nm

        self.prod_cost_price=cp

        self.prod_sell_price=0

       

    def calc_selling_price(self):

        self.prod_sell_price=self.prod_cost_price+(0.1*self.prod_cost_price)

       

    def prod_disp(self):

        self.calc_selling_price()

        print ('Id is ',self.prod_id,' name ',self.prod_name)

        print ('Selling Price ',self.prod_sell_price)

 

# wb means  - write binary

# binary file is NON ASCII file

# ab means  append binary mode

f = open('E:\Aroha Tech\Python Session\prod1.dat','wb')       

#f = open('E:\Aroha Tech\Python Session\prod1.dat','ab')       

 

print ('input id , name and cost price of the prod ')

for i in range(0,1):

    id = input()

    nm = input()

    cp = float(input())

   

    objProd = Product(id,nm,cp)

#   pickle dump use the object and FILE HANDLE    

    pickle.dump(objProd,f)

 

f.close()   

print ('about to read the object file stored in the local system')

# rb read binary

f = open('E:\Aroha Tech\Python Session\prod1.dat','rb')       

print ('about to display all the products stored ....')

#result = pickle.load(f)

#result.prod_disp()

 

while True:

    try:

        result = pickle.load(f)

        result.prod_disp()

    except EOFError:

        break

 

f.close()   

print ('object serialisation and de-serialisation is over ')   
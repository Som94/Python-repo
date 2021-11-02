
class Product:
    def __init__(self,prod_id,name,category,cost):
        self.prod_id=prod_id
        self.name=name
        self.category=category
        self.cost=cost
    
    
    def selling_price(self):
        if self.category=="A":
            self.sp=self.cost+ self.cost*(10.5/100)
            print("Selling Price of the product is :",self.sp)
        elif self.category=="B":
            self.sp=self.cost+ self.cost*(8.5/100)
            print("Selling Price of the product is :",self.sp)
        elif self.category=="C":
            self.sp=self.cost+ self.cost*(7.5/100)
            print("Selling Price of the product is :",self.sp)
    def profit(self):
        self.selling_price()
        
        self.profit=self.sp-self.cost
        print("Profit in that product :",self.profit)
      

    def display(self):
        print("Product id is :",self.prod_id)
        print("Product Name :",self.name)
        print("Category of product :",self.category)
        print("Cost price of the product :",self.cost)
        self.profit()
        
list_prod_id=[]     #To store unique product id
 
my_dict={}
       
for i in range(3):
    while True:
        prod_id=int(input("Enter Product Id :"))
        if prod_id not in list_prod_id:
            list_prod_id.append(prod_id)
            break
        else:
            print("Product Id already exists, Plz try another one..")
    prod_name=input("Enter Product Name :")
    
    while True:
        category=input("Enter the Product Category :")
        if category=="A" or category=="B" or category=="C":
            break
        else:
            print("Plz Enter a Apropriate Category of product A,B or C")
    cost=int(input("Enter the cost price of the Product :")) 

#'''---------------- -------Q 2 --------------------------------'''  
       
    p=Product(prod_id,prod_name,category,cost)
    p.display()

    my_dict.update({prod_id:[prod_id,prod_name,category,cost,p.profit,p.sp]})
    
print(my_dict)

#'''-------------------------- Q 3 ---------------------------'''

while True:
    user_input=int(input("Enter Your Choice :"))
    if user_input in range(1,6):
        #print(user_input)
        if user_input==1:
            mydict_key=int(input("Enter Key value for retriving data :"))
            if mydict_key in my_dict.keys():
                print(my_dict[mydict_key])
            else:
                print("There are no such Key..")
                
        if user_input==2:
            for k,v in my_dict.items():
                print(k,' = ',v)
                
        if user_input==3:
            mydict_key=int(input("Enter Key value for delete product :"))
            
            if mydict_key in my_dict.keys():
                my_dict.pop(mydict_key)
                print('After Deleting product :',my_dict)
            else:
                print("Key Not Avialable..")
                
        if user_input==4:
            mydict_key=int(input("Enter Key value for update the product :"))
            if mydict_key in my_dict.keys():
                if my_dict[mydict_key][2]=='A':
                    if my_dict[mydict_key][3] <=40000:
                        my_dict[mydict_key][3]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(3.5/100)
                        my_dict[mydict_key][5]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(10.5/100)
                        my_dict[mydict_key][4]=my_dict[mydict_key][5]-my_dict[mydict_key][3]
                    print(my_dict[mydict_key])
                
                if my_dict[mydict_key][2]=='B':
                    if my_dict[mydict_key][3] in range(1000,3001):
                        my_dict[mydict_key][3]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(2.5/100)
                        my_dict[mydict_key][5]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(8.5/100)
                        my_dict[mydict_key][4]=my_dict[mydict_key][5]-my_dict[mydict_key][3]
                        
                    print(my_dict[mydict_key])
                
                if my_dict[mydict_key][2]=='C':
                    
                    my_dict[mydict_key][3]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(1.5/100)
                    my_dict[mydict_key][5]=my_dict[mydict_key][3]+my_dict[mydict_key][3]*(7.5/100)
                    my_dict[mydict_key][4]=my_dict[mydict_key][5]-my_dict[mydict_key][3]
                        
                    print(my_dict[mydict_key])
                    
            
        if user_input==5:
            print("Thank You for using the application.., Halt")
            
            break
        
       # break
    else:
        print("Enter in 1 - 5 only//")
    
    
    
    
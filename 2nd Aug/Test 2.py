#Imp_code.py

 

 

class alpha:

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def get_x(self):

        return self.x

    def get_y(self):

        return self.y

    def complete_alpha1(self):

        return alpha

    def complete_alpha2(self):

        return self

    def disp(self):

#       print ('x is' ,self.x, ' and y is ',self.y)

        return 'VALUE :::  x is' ,self.x, ' and y is ',self.y

    def print_object_data_members(self):

        print ('PRINTING/DISPLAYING  x is ',self.x,' y is ',self.y)

# override what ? __str__

    def __str__(self):

        #str1= 'str1:: returned via __str__()  x is', self.x, ' and y is  ',self.y

        #return str1[0]

        str2 = 'str2:: returned via __str__()  x is'+str(self.x)+' and y is  '+str(self.y)

        return str2

#        return f'returned via __str__()  x is {self.x}, and y is  {self.y}'

st1 = { 89,23,45,33 }

n = 46

while True:

    n = int(input('enter the  number '))

    if (n in st1):

        print ('yes it is there ')

    else:

        print ('No it is unique ')

        st1.add(n)

        break

   

print(st1)       

dict1 = dict()

a1 = alpha(10,20)

a2 = alpha(12,56)

lst = []

lst.append(a1)

lst.append(a2)

print (lst)

for i in lst:

    print (i.get_x(), ' ',i.get_y(),' ',i.complete_alpha1(),' ',i.complete_alpha2())   

#                  KEY           VALUE   

    dict1.update({i.get_x(): i.complete_alpha2()  })

    

print ('objects from the dict....')

print ()

for k,v in dict1.items():

    print ('key is ',k,' value is ',v.disp())   

    v.print_object_data_members()

    print ('-----------------------')

 

ky = 10

try:

    temp = dict1.get(ky)

    print ('found ' ,temp.disp())    # this is returning the value

    temp.print_object_data_members() # this is printing as per my style

    print ('watch the temp ** ',temp, ' **')   # override the __str__

    print()

except AttributeError:

    print ('no such key !! ',ky) 

 

 


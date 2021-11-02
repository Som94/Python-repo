'''
Given

lst1 = [10,20,30,40]

tup1 = (78,34,199,25)

tup2 = (100,125,678,-99,-12,-45,50)

dct1 = { 100 : ‘Ravi’ , 200 :  ‘Hari’,  300 : ‘Kishore’}

dct2 = { 101 : 9667789129 , 202 : 9667788192 }

 

1 write a program to input key and values

   Say roll number and names and add it to the dictionary called school_dictionary

    When the user inputs -1 then stop and display the dictionary

 

    Part B

    If the user inputs  (for key)  say 1000  then the value should be lst1

    If the user inputs  (for key)  say 2000  then the value should be tup1

    If the user inputs  (for key)  say 3000  then the value should be contents of lst1 and contents of tup1 as tuple

   If the user inputs  (for key)  say 4000  then the value should be contents of tup1 and tup2 as tuple

    If the user inputs  (for key)  say 5000  then the value should be contents of dct1

   If the user inputs  (for key)  say 6000  then the value should be contents of dct1 and dct2 as dictionary

 

    Part C

    Once the control comes out of the loop

    Then keep doing the following till -1 to stop

     Display the following options to the users:

Option can be a, b, c, d, e -1 (stop)

    a.To delete a value based on the inputted key
    b.To delete all the entries from the school_dictionary
    c.To display the details of the inputted key if it exists otherwise display appropriate message
    d.To update with the new corresponding value for the inputted key
    (Say)  if the key is 1000 and it exists then replace the 1000 with new list of values as below with same RULES as in part B
        
             

new_ lst1 = [101,201,301,401]

new_tup1 = (789,349,1999,259)

new_tup2 = (1000,1255,6788,-999,-122,-455,500)

new_dct1 = { 101 : ‘Ravi Kumar’ , 201 :  ‘Hari Krishnan’,  301 : ‘Kishore Kumar’}

new_dct2 = { 201 : 9660089120 , 302 : 9667788003 }

 

Display the entire school_dictionary

'''

lst1 = [10,20,30,40]

tup1 = (78,34,199,25)

tup2 = (100,125,678,-99,-12,-45,50)

dct1 = { 100 : 'Ravi' , 200 :  'Hari',  300 : 'Kishore'}

dct2 = { 101 : 9667789129 , 202 : 9667788192 }

school_dictionary={}

while True:
    roll_number=int(input("Enter the student's roll number : "))
    if roll_number== -1:
        break
#-------------Part B Start-----------------------------------------------
    if roll_number>999 and roll_number<6001:    
        if roll_number==1000:
            school_dictionary[roll_number]=lst1
        elif roll_number==2000:
            school_dictionary[roll_number]=tup1
        elif roll_number==3000:
            school_dictionary[roll_number]= tuple(lst1)+tup1
        elif roll_number==4000:
            school_dictionary[roll_number]=tup1 + tup2
        elif roll_number==5000:
            school_dictionary[roll_number]=dct1
        elif roll_number==6000:
            dct1.update(dct2)
            school_dictionary[roll_number]=dct1

#-------------Part B End-------------------------------------------------    
    else:
        names=input("Enter the student's name : ")
        
        school_dictionary[roll_number]=names
        
    
print()
        
print("The Student dictionary is :",school_dictionary)


#-----------------Part C Start--------------------------------------------

new_lst1 = [101,201,301,401]

new_tup1 = (789,349,1999,259)

new_tup2 = (1000,1255,6788,-999,-122,-455,500)

new_dct1 = { 101 : 'Ravi Kumar' , 201 :  'Hari Krishnan',  301 : 'Kishore Kumar'}

new_dct2 = { 201 : 9660089120 , 302 : 9667788003 }

 

str1=input("Can you want to do more oparetions (y/n) : ")
if str1=='y':
    while True:
        opt_type=input(''' 
                       Enter 
                       a.To delete a value based on the inputted key.
                       b.To delete all the entries from the school_dictionary.
                       c.To display the details of the inputted key if it exists
                         otherwise display appropriate message.
                       d.To update with the new corresponding value for the inputted key
                       
                       And -1 for Exit
                       So Input the element according to your requirement :''')
        
        if opt_type=='a':
            roll_number=int(input("Enter the Roll number value for delete operation :"))
            if roll_number in school_dictionary.keys():
                del school_dictionary[roll_number]
                print("After delete :",school_dictionary)
            else:
                print("Key is not available in school_dictionary..")
        
        elif opt_type=='b':
            school_dictionary.clear()
            print("All data clear from school_dictionary..")
            print("After clear :",school_dictionary)
        elif opt_type=='c':
            roll_number=int(input("Enter the Roll number for retrive operation :"))
            if roll_number in school_dictionary.keys():
                print('The Retrival value of inputed Roll Number is :',school_dictionary[roll_number])
            else:
                print("Key is not available in school_dictionary..")
                
        elif opt_type=='d':
            roll_number=int(input("Enter the Roll number for update operation :"))
            
            if roll_number in school_dictionary.keys():    
                if roll_number==1000:
                    school_dictionary[roll_number]=new_lst1
                elif roll_number==2000:
                    school_dictionary[roll_number]=new_tup1
                elif roll_number==3000:
                    school_dictionary[roll_number]= tuple(new_lst1)+new_tup1
                elif roll_number==4000:
                    school_dictionary[roll_number]=new_tup1 + new_tup2
                elif roll_number==5000:
                    school_dictionary[roll_number]=new_dct1
                elif roll_number==6000:
                    new_dct1.update(new_dct2)
                    school_dictionary[roll_number]=new_dct1
                print("After update with existing key :",school_dictionary)
            else:
                print("The inputted roll number not existing in school_dictionary.")
        
        elif opt_type=='e' or opt_type=='-1':
              break
          
#------------------Part C End---------------------------------------------
print("The entire school_dictionary :",school_dictionary)




#------------------------- Q 2. Start -------------------------------------------
'''
process the school_dictionary in such a way that you sum EVERY THING (keys and the values ).
Only ignore the value summing for

 

dct2 = { 101 : 9667789129 , 202 : 9667788192 }

new_dct2 = { 201 : 9660089120 , 302 : 9667788003 }
'''

print('\n','*'*10,'Question 2 Start','*'*10,'\n')

key_list=[]
value_list=[]

for k,v in school_dictionary.items():
    key_list.append(k)
    if type(v)==dict:
        for m,n in v.items():
            key_list.append(m)
            value_list.append(n)
    elif type(v)==list:
        value_list=value_list+v
    elif type(v)==tuple:
        value_list=value_list+list(v)
    else:
        value_list.append(v)
        
result_list=key_list+value_list

print(result_list)

sum_able_result=[]
for i in result_list:
    #print(len(str(i)))
    if type(i)==int and len(str(i))<10:
        
        sum_able_result.append(i)
    
print('Here is the result list which sum every thing : ',sum_able_result)




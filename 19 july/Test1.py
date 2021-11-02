'''
Given

lst1 = [10,20,30,40]

tup1 = (78,34,199,25)

tup2 = (100,125,678,-99,-12,-45,50)

dct1 = { 100 : ‘Ravi’ , 200 :  ‘Hari’,  300 : ‘Kishore’}

dct2 = { 101 : 9667789129 , 202 : 9667788192 }

 Part B

   If the user inputs  (for key)  say 1000  then the value should be lst1

   If the user inputs  (for key)  say 2000  then the value should be tup1

   If the user inputs  (for key)  say 3000  then the value should be contents of lst1 and contents of tup1 as tuple

   If the user inputs  (for key)  say 4000  then the value should be contents of tup1 and tup2 as tuple

   If the user inputs  (for key)  say 5000  then the value should be contents of dct1

   If the user inputs  (for key)  say 6000  then the value should be contents of dct1 and dct2 as dictionary

'''
lst1 = [10,20,30,40]

tup1 = (78,34,199,25)

tup2 = (100,125,678,-99,-12,-45,50)

dct1 = { 100 : 'Ravi' , 200 :  'Hari',  300 : 'Kishore'}

dct2 = { 101 : 9667789129 , 202 : 9667788192 }

school_dictionary={}

for i in range(2):
    roll_number=int(input("Enter value for the key : "))
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
        
print(school_dictionary)
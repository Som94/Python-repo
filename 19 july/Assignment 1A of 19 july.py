'''
 write a program to input key and values

 Say roll number and names and add it to the dictionary called school_dictionary

 When the user inputs -1 then stop and display the dictionary
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
    names=input("Enter the student's name : ")
    
    school_dictionary[roll_number]=names
print()
        
print("The Student dictionary is :",school_dictionary)
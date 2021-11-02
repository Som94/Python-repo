
def correct_spelling(dict2):

    for i in dict2:

        print (i,' ',dict2[i])

 

    temp_str = dict2[1000]

    temp_str = 'Mr '+temp_str

    dict2.update({1000 : temp_str})

   

    temp_str = dict2[2000]

    temp_str = 'Mr '+ temp_str[:4]+'A'+temp_str[4:]

    dict2.update({2000 : temp_str})

   

    print ('inside the function ---before changing ... ',dict2)

    dict2.update({3000 : dict2[1000]})

    dict2.pop(1000)

   

    

    

def my_list_elements_append(lst):

    print ('inside the function lst is  ',lst, ' ******')

    lst = [175,225,335,900,1000,1500]

    lst.append(99)

    lst.append(101)

    lst.append(103)

    print ('inside the function lst is appended with some values ')

    print (' ------------------------ ')

    return lst 

    

 

lst = [18,19,20]

print ('before addition ',lst)

temp1 = my_list_elements_append(lst)

print ('BACK INSIDE THE MAIN BLOCK ....after addition lst is  ',lst,' ',id(lst))

print ('BACK INSIDE THE MAIN BLOCK ....after addition temp1 is ',temp1,' ',id(temp1))

 

dict1= {1000:'Harish',2000:'Richrds'}

print ('inside the main block .... dict1 ',dict1)

correct_spelling(dict1)

print ('again BACK inside the main block .... now dict1 ',dict1)
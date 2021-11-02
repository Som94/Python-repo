def add_new_members(lst1):

    lst1.append(181)

    lst1.insert(4,295)

   

def remove_some_elements(listed,ele):

    listed.remove(ele[0])

    listed.remove(ele[1])

 

def modify_members(lst1,ele):

    pos = ele[0]

    lst1[pos]= 10000

    print ('length of list is ',ele[1])

#IndexError: list assignment index out of range   

    pos = ele[1]-1

    lst1[pos]= 50000

   

def this_is_not_possible(lst1):

    lst1 = list()

    lst1.append(1)

    lst1.append(2)

    lst1.append(3)

    print ('in function this_is_not_possible() ahaha I changed the list ',lst1)

    return lst1

    # the lst1 temporarily created inside this function

    # will be released back at this point (EXITING out of the )

    # function

 

print ('i am in the main BLOCK')

lst1 = [17,22,3,55,66,50,65,90,76]

print (lst1)

add_new_members(lst1)

print ('after addition in the function ',lst1)

remove_some_elements(lst1,(65,17))

print ('after removal of 17,65 in the function ',lst1)

modify_members(lst1,(0,len(lst1)))

print ('after modf of 0th ,last ele in the function ',lst1)

lst2 = this_is_not_possible(lst1)

print ()

print ('I am back in main BLOCK and i am UNCHANGED ',lst1)

print ('and new list i got it returned from a function ',lst2)

 

 

prog2.py

 

x1 = 100

x2 = 'India'

 

def test_func1():

    global x2

    print ('gloabl ',x1,' ',x2)  # you used the values

    x2 = 'Karnataka State'

    print ('gloabl after change ',x1,' ',x2)

    

 

def test_func2():

    x3 = 55

    x4 = 'Korea' # this has got no connection with global x1,x2

    print ('local ',x3,' ',x4)   

    global x1, x2

    print ('global ',x1,' ',x2)   

 

print ('i am in the main BLOCK')   

test_func1()

print ('--------')

test_func2()

 
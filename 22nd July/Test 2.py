#Filter_demo.py

 

check_ev = lambda x : (x%2==0)

 

lst1 = [12,56,21,19,0,39,42,45,-19,10,31,49,50,75,77,86]

 

even_lst = list(filter(check_ev,lst1))

 

print ('even number of ele from the list ', even_lst)

 

odd_list = list(filter( lambda x : x%2==1 ,lst1))

 

print ('odd numbers from the list ',odd_list)

 

odd_tup = tuple( filter(lambda x : x%2==1 ,lst1))

print ('odd numbers from the tuple  ',odd_tup)

 

odd_set =set(filter( lambda x : x%2==1 ,lst1))

print ('odd numbers from the set   ',odd_set)

 

#odd_dct =dict(filter( lambda x : x%2==1 ,lst1))

#print ('odd numbers from the dcit   ',odd_dct)

 

 

names=['Harish','Kiran','Manoj','Kedar','Dolly Poll','Ruben','Issac','Kapil']

print (names)

 

#myname = 'Issac Vivan Alexander Richards'

myname = 123345

dict2 = {'Ajay':10, 'Kapil':20 , 'Kiran':30 ,' Vinod':40}

dict3 = {10:'Ajay' , 20: 'Kapil' , 30:'Kiran' ,40:'Vinod'}

nm_with_k = list(filter( lambda x: x[0] =='K' , dict3.values()))

print ('names with K ' ,nm_with_k)

 

print ()

filter_cond = lambda x : x >=25 and x <=50

print ('watch this way 25-50 ', tuple(filter(lambda x : x >=25 and x <=50,lst1)))

 

print ('watch this style 25-50 ', tuple(filter(filter_cond,lst1)))

 
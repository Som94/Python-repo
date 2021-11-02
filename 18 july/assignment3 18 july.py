'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}

Process the lst, delete all the elements from ‘Deepak’ and onwards and then display the list.
'''

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 


print(lst[0: lst.index('Deepak')])
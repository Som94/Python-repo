'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}

Process the tup, lst ,myset and add all the numeric elements to a new list called new_lst
Sum it , find avg , find max , find min

 '''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}


lst1=list(tup)
lst2=list(myset)
lst3=lst+lst1+lst2
new_lst=[]
sum1=0
for i in lst3:
    if type(i)==int:
        sum1 += i
        new_lst.append(i)
print(new_lst)

print('Sum all  numeric elements is : ',sum(new_lst),'And Average : ',sum(new_lst)/len(new_lst),', ', "Max Value: ",max(new_lst),'  and Min Value: ',min(new_lst))


    
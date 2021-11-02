'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}

 

Process the tup, lst and set – add all the positive numbers only.
If ‘India’ string comes then treat India equivalent to 10  (I mean number) and add it

Find the sum, avg, max , min

'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}

lst1=[]
sum1=0

for i in tup:
    if i=='India':
        i=10
    if type(i)==int:
        if i>0:
            sum1 += i
            lst1.append(i)
print('Sum all +ve number in tup : ',sum1,'And Average : ',sum1/len(lst1),', ', "Max Value: ",max(lst1),'  and Min Value: ',min(lst1))

lst2=[]
sum2=0
for i in lst:
    if i=='India':
        i=10
    if type(i)==int:
        if i>0:
            sum2 += i
            lst2.append(i)
print('Sum all +ve number in lst : ',sum2,'And Average : ',sum2/len(lst2),', ', "Max Value: ",max(lst2),'  and Min Value: ',min(lst2))

lst3=[]
sum3=0
for i in myset:
    if i=='India':
        i=10
    if type(i)==int:
        if i>0:
            sum3 += i
            lst3.append(i)
print('Sum all +ve number in myset : ',sum3,'And Average : ',sum3/len(lst3),', ', "Max Value: ",max(lst3),'  and Min Value: ',min(lst3))

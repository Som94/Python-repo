'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}

Process the myset from the end keep displaying all the numbers. The moment you have 
displayed 2 negative numbers :: then stop
Processing the myset

'''

myset = {'uday','India',67,12,44,-86,-77,-19,29,33,28}

mylst=list(myset)
print(mylst)
neg_count=0
len_mylst=len(mylst)
for i in range(len_mylst):
    if neg_count<2:
        
        print(mylst[len_mylst-1-i])
    else:
        break
    
    if type(mylst[len_mylst-1-i])==int:
        if  mylst[len_mylst-1-i]<0:
            neg_count += 1

'''

tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

myset = {'uday','India',67,12,44,-86,-77,-19,29,28}


Split the lst , tup and myset from it middle element in such a way
as shown. The image is self explanatory.

'''
#tup=(56,78,90,'India',23,'Shyam',33,12,'Ram','Kiran','Gopal',99,23)

#lst =[100,-34,-56,88,22,16,'Arvind','Lalit','Deepak','India','Mohan',199,200] 

#myset = {'uday','India',67,12,44,-86,-77,-19,29,28}


tup= (10,20,30,40,50,60)
lst =[100,200,300,400,500,600,700,800]
myset=['Arun','Bindu','Chandra','Divakar','Eshwar','Frank','Ishan','Kishan']


#lst1=list(tup)
#lst2=list(myset)

len_lst=len(lst)
len_lst1=len(tup)
len_lst2=len(myset)

#print(len_lst//2,',',lst[(len_lst//2)+1::],',',lst[:(len_lst//2)+1:])
#print(len_lst1//2,',', lst1[(len_lst1//2)+1::],',',lst1[:(len_lst1//2)+1:])
#print(len_lst2//2,',',lst2[:(len_lst2//2):],',', lst2[(len_lst2//2)::])

new_lst=tup[(len_lst1//2)+1::] + lst[(len_lst//2)+1::] + myset[:(len_lst2//2):] + lst[:(len_lst//2)+1:] + tup[:(len_lst1//2)+1:] + myset[(len_lst2//2)::]

print(new_lst) 
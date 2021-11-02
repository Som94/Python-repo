'''
new_check_list = [ [12,66,50,49],(100,120,90,9),10,12, (104,320,90,9), [13,66,150,39,25,22],39,49,61]
process new_check_list

find the highest and lowest among all the tuples.

find the highest and lowest among all the list.

find the sum of all the numbers irrespective whether in tup, list or set.

'''

#myset1= { [12,66,50,49],(100,120,90,9),10,12,(104,320,90,9),(13,66,150,39,25,22),39,49,61}

new_check_list = [ [12,66,50,49],(100,120,90,9),10,12, (104,320,90,9), [13,66,150,39,25,22],39,49,61]



tuple1=[]

list2=[]

total_sum=0

for i in new_check_list:
    #print(i)
    if type(i)==list:
        list2=list2+i
        for j in i:
            total_sum=total_sum+j
    elif type(i)==tuple:
        tuple1=tuple1+list(i)
        for k in i:
          total_sum=total_sum+k  
    else:
        total_sum=total_sum+i
        
print('The highest :',max(tuple1),' and lowest :',min(tuple1),' among all the Tuple and Tuple is :',tuple(tuple1))

print('The highest :',max(list2),' and lowest :',min(list2),' among all the List and List is :',list2)

print('The sum of all the numbers irrespective whether in tup, list or set :',total_sum)
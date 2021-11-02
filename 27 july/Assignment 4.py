'''
data1 = [ ‘Deepak’, ‘Manoj’, ‘Arvind’ ,  350, 100, -671 , ‘Vivek’, ‘Harish’]
data2 =  (100,200,225,175,90)

 

sort the tuple.

Create the dictionary with keys from the sorted tuple value

Create the value taking from the list – only names as they appear. Ignore the numbers in the list

Example is

90               100          175          200    225

Deepak       Manoj    Arvind   Vivek   Harish

'''
data1 = [ 'Deepak', 'Manoj', 'Arvind' ,  350, 100, -671 , 'Vivek', 'Harish']
data2 =  (100,200,225,175,90)

def dictionary():
    sorted_tuple=sorted(data2)
    
    for i in data1:
        for j in data1:
            if type(j)==int:
                data1.remove(j)
        
    dict1={sorted_tuple[i]:data1[i] for i in range(len(sorted_tuple))}
    print('The Dictionary is :',dict1)

dictionary()

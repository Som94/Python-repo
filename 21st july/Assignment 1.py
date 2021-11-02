'''
Solve Using Function
Given a range of numbers 400 to 900
Find all Prime numbers
Store it in the list
'''

def prime(low_range, high_range):
        
    for i in range(low_range, high_range):
        for j in range(2,i):
            if i%j==0:
                    #print("Prime Not Number",i)
                break
        else:
            #print("Prime Number",i)
            result_list.append(i)
                     
    return result_list
    
    
low_range=int(input("Enter Low range value : "))
high_range=int(input("Enter High range value : "))
result_list=[]
print(prime(low_range, high_range))
'''
Take several input from user as string , check wether it is palindrome or not
store into a dictionary as if it is palindrome assign the value as true else assign false
{'liril': True, 'abc' : False}
And so on

'''

def palindrome(n):
    
    for i in range(n):
        str1=input("Enter any String :")
        if str1==str1[::-1]:
            dic[str1]=True
        else:
            dic[str1]=False
    return dic
        
n=int(input("Enter number of input you want :"))
dic={}
print(palindrome(n))

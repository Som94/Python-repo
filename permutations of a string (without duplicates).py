'''
create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

'''

# Python code to demonstrate
# to find all permutation of
# a given string
 
# Initialising string
ini_str = "abc"
 
# Printing initial string
print("Initial string", ini_str)
 
# Finding all permutation
result = []
 
def permute(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 
permute(list(ini_str), 0, len(ini_str))
 
# Printing result
print("Resultant permutations", str(result))




#_____________________****************___________________________________



def permutations(string):
    #lst=list(st)
    if len(string)==0:
        return ''
    elif len(string)==1:
        return string
    else:
        e_str=''
        result=[]
        for i in range(len(string)):
            x=string[i]
            xs=string[:i] + string[i+1:]
            for p in permutations(xs):
                e_str=e_str+(x+p)
                result.append(e_str)
                e_str=''
        return sorted(list(set(result)))
        
data='aabb'
permutations(data)

            
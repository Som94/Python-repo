r=[101, 102, 6000, 100, 200, 300, 101, 202, 'som', 'nath', 'Ravi', 'Hari', 'Kishore', 9667789129, 9667788192]
print(r)
r1=[]
for i in r:
    #print(len(str(i)))
    if type(i)==int and len(str(i))<10:
        
        r1.append(i)
    
print(r1)
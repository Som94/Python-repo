st1= {10,20,30}
lst1=[17,19,10,15,10,10,25,20,23,20,29,30,35,30]   

for i in st1:
    #print(i)
    while i in lst1:
        lst1.remove(i)
        
print(lst1)
    
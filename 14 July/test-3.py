lst1 = [12,45,88,[67,22,122],[23,35,17,73],50,40]
for l in range(len(lst1)):
    if type(lst1[l])==list:
        a=sum(lst1[l])
        lst1[l]=a
        
print(lst1)
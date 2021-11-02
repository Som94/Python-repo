'''

names={'Ganesh','liril','malaylam','hari','MadAm','usha','MADam','LirIL','Asha','1001','Raj','LIRiL'}
 

process the set and find out how many are PALENDROME.

do not distinguish between lowercase and uppercase.

'''

names={'Ganesh','liril','malaylam','hari','MadAm','usha','MADam','LirIL','Asha','1001','Raj','LIRiL'}

count=0
for i in names:
    
    if i.islower() or i.isupper() or i.isnumeric():
        if i==i[::-1]:
            #print(i)
            count += 1
print('There are ',count,'PALENDROME elements, which are do not distinguish between lowercase and uppercase.')
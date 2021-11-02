news='today is Wednesday and the month is July'

# important error message

# TypeError: 'str' object does not support item assignment

# string is immutable

# news[3] = 'X'

space_count=0

pos=0

result=''

for x in news.upper():

    print (x,end='')

    if (x == ' '):

        space_count+=1

        result=result+str(pos)+","   #==> ''+'3'+','      '3,'+'9'+','

                                     #==> '3,9,'+'12'     '3,9,12,'

    pos=pos+1

print()

print()

print ('total spaces are ', space_count)

slen=len(result)

slen-=1

#print ('position of spacses ' , result[:-len(result)+1:-1])

    #'3,9,12,

print ('position of spacses ' , result[0:slen])

slen=slen+2

print ('position of reversed spaces ' , result[-2:-slen:-1])
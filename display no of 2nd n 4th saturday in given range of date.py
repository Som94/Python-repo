
"""
Given two dates
d1 to d2 ( both inclusive)
Print all the 2nd and 4th Saturdays
Count how many are there?

"""


import datetime
print("Enter dates input format example: 8 Feb 2021")
date_start_str = '20 Feb 2010' #input("Enter start date: ")
date_end_str = '12 Dec 2011' # input("Enter end date: ")
# convert string to date format 
date_start = datetime.datetime.strptime(date_start_str, '%d %b %Y')
date_end = datetime.datetime.strptime(date_end_str, '%d %b %Y')
# initialization of the initial number of weekends
day = datetime.timedelta(days=1)
count_saturday = 0
count_sunday = 0
# iteration over all dates in the range
while date_start <= date_end:
    if date_start.isoweekday() == 6:
        print(date_start.isoweekday())
        print(date_start.day)
        count_saturday += 1
        
    date_start += day
# output a single line containing two space-separated integers
print(count_saturday)
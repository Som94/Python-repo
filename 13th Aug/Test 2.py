st1 = { 12,56,78,125,100,105,225,66,19,127}

'''
 find the lowest among the 3 digit number (consider ONLY 3 digit numbers)
  lambda filter
  sum, avg ,....
'''



l2=list(filter(lambda x : x>99 and x<1000,st1))
print(min(l2))
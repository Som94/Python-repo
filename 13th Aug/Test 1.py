class emp:
  pass
e1 = emp()
lst1 = [171,'Divakar',e1,56.22,'Ravi','78']

l=len(lst1)

if type(lst1[l-1])==str:
    print("True")
else:
    print("Not a string")
if type(lst1[l-2])==str:
    print("True It's a string")
else:
    print("Not a string")
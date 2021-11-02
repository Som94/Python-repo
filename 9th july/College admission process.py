catagory=int(input("Enter your catagory either 0 for defence or 1 for general :"))

if catagory==0:
    physics=int(input("Enter obtain mark in physics : "))
    chemestry=int(input("Enter obtain mark in chemestry : "))
    mathematics=int(input("Enter obtain mark in mathematics : "))
    english=int(input("Enter obtain mark in english : "))
    puc_percentage=(physics+chemestry+mathematics+english)/4
    pcm_percentage=(physics+chemestry+mathematics)/3
    if puc_percentage>=50 and pcm_percentage>=60 and (physics==100 or chemestry==100 or mathematics==100):
        print("Admission Granted")
    elif puc_percentage>=50 and pcm_percentage>=75 and physics>=85:
        print("Admission Granted")
    else:
        print("Wait for 2nd round selection to be announced")

elif catagory==1:
    physics=int(input("Enter obtain mark in physics : "))
    chemestry=int(input("Enter obtain mark in chemestry : "))
    mathematics=int(input("Enter obtain mark in mathematics : "))
    english=int(input("Enter obtain mark in english : "))
    puc_percentage=(physics+chemestry+mathematics+english)/4
    pcm_percentage=(physics+chemestry+mathematics)/3
    if puc_percentage>=50 and pcm_percentage>=60 and (physics==100 or chemestry==100 or mathematics==100):
        print("Admission Granted")
    elif puc_percentage>=50 and pcm_percentage>=80 and physics>=90:
        print("Admission Granted")
    else:
        print("Wait for 2nd round selection to be announced")

    
    
else:
    print("Please enter only either 0 or 1 nothing else..")
domestic=0
commercial=1
area=int(input("If you are from Domestic Area Press 0 or Commercial Area Press 1:"))
if area>1 or area<0:
    print("Plz.. Enter either 0 or 1 only")
else:
    if area==0:
        
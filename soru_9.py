
for x in range(1,1000):
    x= str(x)

    if len(x)==1 and int(x)<9:
        print(x, end=" ")

    elif len(x)==2 and (int(x[0])+int(x[1]))<9:
        print(x, end=" ")

    elif len(x)==3 and (int(x[0])+int(x[1])+int(x[2]))<9:
        print (x, end=" ")
        


        

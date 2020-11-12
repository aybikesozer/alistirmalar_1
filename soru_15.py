 
for x in range(10000,100000):
    for a in range (2,x):
        if x%a==0:
            break

    else:
        print(x,end=" ")
            

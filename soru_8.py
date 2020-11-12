sum=0
for x in range(100,1000,2):
    x=str(x)
    b1= int(x[0])
    b2= int(x[1])
    b3= int(x[2])

    if b1==b2 or b1==b3 or b2==b3:
        sum= sum+1

print(sum)

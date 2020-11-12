sum=0
for x in range(1000,10000):
    x= str(x)
    if int(x[0])> int(x[-1]):
        sum= sum+1

print(sum)

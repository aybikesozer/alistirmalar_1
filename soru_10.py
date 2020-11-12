sum=0
for x in range(10000,100000):
    x=str(x)
    if x[0]==x[-2] and x[1]==x[-1]:
        sum= sum+1

print(sum)

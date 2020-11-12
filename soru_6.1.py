x=list()
for i in range(1000,10000):
    i= str(i)
    if i[0]>i[-1]:
        x.append(i)

print(len(x))
        

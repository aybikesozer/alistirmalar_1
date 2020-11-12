kalan=[]

for x in range(1,125):
    if 125%x==200%x==350%x:
        kalan.append(125%x)
        enbuyuk=x

    kalan.sort(reverse=True)

print("en büyük kalan:",kalan[0],",En büyük kalanı veren x sayısı:",enbuyuk)


    
        

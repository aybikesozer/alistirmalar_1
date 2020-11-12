toplam=0
n=0
for n in range(1,10000):
   factorial = n*(n+1)
   toplam = toplam+ 1/factorial
   

print ("e'nin yaklaşık değeri",toplam,"dır.")

sayı= input("Sayı giriniz:")
x=int(sayı)
for a in range(2,x):
    if x%a==0:
        print(x,"asal sayı değildir.")
        break

    else:
        print(x,"asal sayıdır.")
        break

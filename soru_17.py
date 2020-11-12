
sayı=input("Sayı giriniz:")
x=str(sayı)
if len(x)==3 or len(x)==4 and x==x[: : 1]:
    print(x,"palindromik bir sayıdır.")
else:
    print("3 veya 4 basamaklı bir palindromik sayı girmediniz.")

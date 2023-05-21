"""
Klavyeden girilen n adet tam sayının birler basamaklarının toplamı
"""
n = int(input("Kaç sayı gireceksiniz:"))
total =0
for i in range(1,n+1):
    print(i,".sayı:", end = "")
    sayi = int(input())
    total+= (sayi%10)
print("Girilen sayıların birler basamaklarının toplamı:%d" %total)

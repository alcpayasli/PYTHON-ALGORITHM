"""
Girilen sayının basamaklarının aritmetik ortalaması
"""
num = int(input("Sayı giriniz:"))
toplam = sayac = 0
while(num>0):
    toplam+= num%10
    sayac+=1
    num//=10
print("Girilen sayının basamaklarının ortalaması:%.3f" %(toplam/sayac))
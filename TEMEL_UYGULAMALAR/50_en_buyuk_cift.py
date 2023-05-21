"""
Klavyeden girilen n tane tam sayıdan en büyük çift sayıyı bulma
"""
n = int(input("Kaç adet sayi gireceksiniz:"))
enb = -1
for i in range(n):
    num = int(input("Sayı giriniz:"))
    if(num % 2 == 0 and num>enb):
        enb = num
if(enb == -1):
    print("Girilen sayıların hiçbiri çift sayı değil")
else:
    print("Girilen sayılardan en büyük çift sayı:", enb)

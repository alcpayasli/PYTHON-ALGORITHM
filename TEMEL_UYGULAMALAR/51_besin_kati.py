"""
Girilen sayıyı kendisinden küçük en yakın 5'in katına yuvarlama
"""
num = int(input("Sayı giriniz:"))
num = num-(num%5)
print(num)
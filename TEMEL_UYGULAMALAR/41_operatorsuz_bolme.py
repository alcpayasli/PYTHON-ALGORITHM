"""
Girilen iki sayının operatör bölme operatörü kullanmadan bölüm ve kalanı bulma
"""
num1 = int(input("Bölünecek sayı:"))
num2 = int(input("Bölen sayı:"))
result = 0
while(num1>=num2):
    num1 -=num2
    result+=1
print("Bölüm sonucu:", result)
print("Kalan:", num1)


"""
Girilen sayıyı tersten yazma
"""
number = int(input("Bir sayı giriniz:"))
b = 0
while(number>0):
    k = number%10
    b =b*10 + k
    number//= 10
print("Girilen sayının tersi:%d" %b)
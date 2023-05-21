"""
Klayveden girilen pay ve payda degerlerine göre bolumun belirtilen basamağı
"""
a = int(input("Pay degeri:"))
b = int(input("Payda degeri:"))
n = int(input("Basamak degeri"))
print("Bölüm sonucu:%f" % (a/b))
for i in range(n):
    a = a*10
    c = a//b
    a = a%b

print("Belirtilen basamak:%d" %c)

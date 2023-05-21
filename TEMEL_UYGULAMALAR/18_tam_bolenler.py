"""
klavyeden girilen sayının tam bölenlerini bulma
"""
a = int(input("Sayı giriniz:"))
print("%d sayısının tam bölenleri:" % a)
for i in range(1, a+1):
    if(a%i == 0):
        print(i)

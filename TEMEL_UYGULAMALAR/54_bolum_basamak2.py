"""
1/a sayısının ilk b basamağını gösterme
"""
a = int(input("Sayı giriniz:"))
b = int(input("Basamak sayısı giriniz:"))
k = 0
r =1
print("0.", end = "")
while(k!=b):
    print(10*r//a, end = "")
    r = 10*r%a
    k+=1

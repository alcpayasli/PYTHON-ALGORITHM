year = int(input("4000'den küçük olmak üzere yılı giriniz:"))
if(year % 4 == 0 and (year % 100 !=0 or year%400 ==0)):
    print("Artık yıldır")
else:
    print("Artık yıl değildir")

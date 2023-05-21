x = eval(input("F(x) fonksiyonu için x değeri giriniz:"))
if(x<0):
    y = 1
elif (x>=0 and x<=2):
    y = x
elif (x>2 and x <=4):
    y = 3
else:
    y = 4-x
print("Girilen x değeri için fonksiyonun değeri: %.2f" %y)
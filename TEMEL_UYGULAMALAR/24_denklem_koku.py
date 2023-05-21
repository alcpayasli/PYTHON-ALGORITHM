"""
ax + b = c şeklinde 1. dereceden denklemin kökünü hesaplama
"""
a = int(input("0'dan farklı olacak şekilde x katsayısını giriniz:"))
if(a == 0):
    print("Sıfırdan farklı bir x katsayısı giriniz!!")

else:
    b = int(input("b değeri:"))
    c = int(input("c değeri:"))
    root = (c-b)/a
    print("%dx + %d = %d şeklindeki denklemin kökü:%.3f" %(a,b,c,root))


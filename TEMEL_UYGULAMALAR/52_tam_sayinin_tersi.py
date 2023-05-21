"""
Klavyeden girilen tam sayının iki katını 3 farklı pozitif tamsayının tersleri toplamı şeklinde yazma
"""
num = int(input("Sayı giriniz:"))
print("1/" + str(num) +" +1/" + str(num+1)+ " +1/" +  str(num*(num+1)) + " = 2/" + str(num))
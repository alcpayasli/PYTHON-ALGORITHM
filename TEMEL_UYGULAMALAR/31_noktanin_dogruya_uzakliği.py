import math
a = int(input("ax + by + c doğrusu için a değeri:"))
b = int(input("ax + by + c doğrusu için b değeri:"))
c = int(input("ax + by + c doğrusu için c değeri:"))
x1 = int(input("Noktanın x değeri:"))
y1 = int(input("Noktanın y değeri:"))
if(a*x1 + b*y1 + c == 0):
    print("Nokta doğru üzerindedir")
else:
    dist = abs(a*x1 + b*y1 + c) / math.sqrt(a**2 + b**2)
    print("Noktanın doğruya uzaklığı: %.3f" %dist)

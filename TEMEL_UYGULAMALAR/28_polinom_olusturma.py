"""
iki reel kökü bilinen polinomu oluşturma
"""

x1 = int(input("x1 kökü:"))
x2 = int(input("x2 kökü:"))
ktop = x1 + x2
kcarp = x1*x2
if(ktop<0):
    print("x^2", -1*ktop, "x", end= "")
else:
    print("x^2-", ktop,  "x", end= "")
if (kcarp<0):
    print(kcarp)
else:
    print("+", kcarp)


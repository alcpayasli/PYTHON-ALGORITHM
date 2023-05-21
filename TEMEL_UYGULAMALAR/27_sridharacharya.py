"""
ax^2 + bx + c = 0 şeklindeki denklemin köklerini diskriminant hesaplamadan bulma
"""

a = int(input("a katsayısı:"))
b = int(input("b katsayısı:"))
c = int(input("c sabiti:"))
if(a + b+ c == 0):
    root_1 = 1
    root_2 = c/a
    print("Denklemin kökleri: %d ve %.3f" %(root_1, root_2))
else:
    delta = b**2-4*a*c
    if(delta>0):
        root_1 = (-b-(delta**(0.5))) / (2*a)
        root_2 = (-b+(delta**(0.5))) / (2*a)
        print("Denklemin kökleri: %.3f ve %.3f" %(root_1, root_2))
    elif (delta == 0):
        root_1 = -b/(2*a)
        print("Denklemin tek kökü: %.3f" %(root_1))
    else:
        print("Denklemin reel kökü mevcut değildir")

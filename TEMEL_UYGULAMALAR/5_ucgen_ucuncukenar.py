"""
İki kenarı ve arasındaki açı verilen üçgenin 3. kenarını bulma
"""
import math
k1 = int(input("1. kenar:"))
k2 = int(input("2. kenar:"))
aci = int(input("Açı:"))
k3 = (k1**2 + k2**2 - 2*k1*k2*(math.cos(math.radians(aci)))) **(1/2)
print(" 3.kenar: {:.3f}".format(k3))
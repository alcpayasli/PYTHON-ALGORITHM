"""
İki kenarı ve aralarındaki açı bilinen ucgenin alanı
"""
import math
k1 = int(input("Birinci kenar:"))
k2 = int(input("İkinci kenar:"))
aci = int(input("Aradaki açı:"))
alan = k1 *k2* math.sin(math.radians(aci)) /2
print("Üçgenin alanı:%.2f cm2" %(alan))
"""
İki köşegeni ve aralarındaki açısı bilinen dörtgenin alanını hesaplama
"""
import math
k1 = int(input("Birinci köşegen:"))
k2 = int(input("İkinci köşegen:"))
aci = int(input("Açı:"))
alan = k1*k2*math.sin(math.radians(aci)) /2
print("Alan: %.2f" %alan)


"""
iki dik kenarı verilen üçgenin hipotenüsünü bulma
"""

d1 = int(input("Birinci dik kenar:"))
d2 = int(input("İkinci dik kenar:"))
hipotenus = (d1**2 + d2**2) **(1/2)
print("Hipotenüs: %.2f" % (hipotenus))

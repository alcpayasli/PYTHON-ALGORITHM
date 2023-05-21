"""
Heronn formülü ile üçgen alan hesaplama
"""
k1 = int(input("Birinci kenar:"))
k2 = int(input("İkinci kenar:"))
k3 = int(input("Üçüncü kenar:"))
u = (k1 + k2+ k3) / 2
alan = (u*(u-k1)*(u-k2)*(u-k3)) **(0.5)
print("Üçgenin alanı: %.3f" %(alan))


"""
radyoaktif element yarılanma süresini ve kalan kütlesini hesaplama
"""
m1 = int(input("Başlangıç kütlesi:"))
t = int(input("Süre:"))
dt = int(input("Yarılanma süresi:"))
n = t/dt
m = m1/2**n

print("Yarılanma süresi:%.3f" %n)
print("Kalan kütle:%.3f" %m)
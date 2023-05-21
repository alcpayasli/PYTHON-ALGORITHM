"""
Yüksekliği ve ilk hızı bilinen cismin havada kalma süresini
 yatayda alacağı yolu ve yere çarpma hızını hesaplama
"""
h = int(input("Yükseklik:"))
v = int(input("İlk hız:"))
sure = (2*h/9.8) **(0.5)
yol = v*sure
hız = ((9.8*sure)**2 + (v**2)) **(0.5)
print("Havada kalacağı süre:%.2f" %(sure))
print("Yatayda alınan yol:%.2f" %yol)
print("Yere çarpma hızı: %.2f" % hız)

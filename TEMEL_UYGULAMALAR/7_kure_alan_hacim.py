"""
Kürenin alanını ve hacmini hesaplama
"""
r = int(input("Kürenin yarıçapı:"))
alan = 4*(3.14)*(r**2)
hacim = 4*(3.14)*(r**3) /3
print("Kürenin alanı:%.2f" % alan)
print("Kürenin hacmi:%.2f"%hacim)

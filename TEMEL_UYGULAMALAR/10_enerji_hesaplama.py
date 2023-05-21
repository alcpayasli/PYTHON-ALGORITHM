"""
kinetik ve potansiyel enerji hesabı
"""
h = int(input("Yükseklik:"))
m = int(input("Kütle:"))
v = int(input("Hız:"))
ke = 0.5*m*(v**2)
pe = m*h*9.8

print("Maddenin kinetik enerjisi:%.2f" %(ke))
print("Maddenin potansiyel enerjisi:%.2f" %(pe))


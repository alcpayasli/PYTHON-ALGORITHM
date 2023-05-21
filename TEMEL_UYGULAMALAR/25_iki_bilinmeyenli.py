"""
ax + by = c
dx + ey = f şeklinde mevcut iki denklemin çözüm kümesi
"""
a = int(input("a katsayısı:"))
b = int(input("b katsayısı:"))
c = int(input("c değeri:"))
d = int(input("d katsayısı:"))
e = int(input("e katsayısı:"))
f = int(input("f değeri:"))

root_x = (c-b*f/e) / (a-b*d/e)
root_y = (c-a*root_x) / b
print("Her iki denklemin kökleri: %.3f ve %.3f" %(root_x, root_y))

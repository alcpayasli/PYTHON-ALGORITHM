""" 
n elemanlı kümenin r'li kombinasyolarını hesaplama
"""
n = int(input("Kümenin eleman sayısını giriniz:"))
r = int(input("Kümenin hesaplanacak kombinasyon sayısını giriniz:"))

f1 = f2 = f3 = 1

for i in range(1, n+1):
    f1*=i
    if(r>=i):
        f2*=i
    if(n-r>=i):
        f3*=i
k = f1/(f2*f3)
print("%d elemanlı kümenin %d elemanlı kombinasyon sayısı:%d" %(n,r,k))

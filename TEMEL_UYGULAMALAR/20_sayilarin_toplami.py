"""
1'den n'e kadar olan tüm sayıların, tek sayıların ve çift sayıların toplamı
"""

t1=t2=t3=0
n = int(input("Üst sınır giriniz:"))
for i in range(1, n+1):
    t1+=i
for i in range(1, n+1,2):
    t2+=i
for i in range(2, n+1, 2):
    t3+=i

print("1'den %d'ye kadar olan sayıların toplamı:%d" %(n, t1))
print("1'den %d'ye kadar olan tek sayıların toplamı:%d" %(n, t2))
print("1'den %d'ye kadar olan çift sayıların toplamı:%d" %(n, t3))
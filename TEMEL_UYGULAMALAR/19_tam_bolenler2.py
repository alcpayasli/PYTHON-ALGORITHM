a = int(input("A sayısı:"))
print("a sayısınınn tam bölenleri:")
print(1)
for i in range(2, int(a/2) +1): 
# hiç bir tam sayı kendi yarısından daha büyük sayıya bölünemeyeceğinden (kendisi hariç) sayının yarısına kadar
    if a % i == 0:
        print(i)
print(a)
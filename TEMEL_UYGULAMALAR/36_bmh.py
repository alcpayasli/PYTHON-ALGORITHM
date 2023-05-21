"""
Bazal metabolizma hızı hesaplama
"""
height = float(input("Boyunuzu metre cinsinden giriniz(Örneğin 1.78 gibi):"))
weight = float(input("Kilonuzu giriniz:"))
age = int(input("Yaşınız:"))
sex = input("Cinsiyetiniz erkek ise 1, kadın ise 2 yazınız:")
if(sex =="1"):
    bmh = 66.473 + 13.7516*weight + 5.0033*height-6.775*age
    print("Bazal metabolizma hızınız: %.3f" %bmh)
elif(sex =="2"):
    bmh = 655.0955 + 9.5634*weight + 1.8496*height-4.6756*age
    print("Bazal metabolizma hızınız: %.3f" %bmh)
else:
    print("Geçersiz cinsiyet seçimi")
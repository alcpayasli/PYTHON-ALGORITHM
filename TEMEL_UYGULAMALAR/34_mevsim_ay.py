"""
Girilen mevsime göre ay isimlerini listeleme
"""
print("Mevsimler:\n1.İlkbahar\n2.Yaz\n3.Sonbahar\n4.Kış")
session =input("Seçiminiz:")
if (session=="1"):
    print("İlkbahar mevsiminin ayları:Mart, Nisan, Mayıs")
elif(session=="2"):
    print("Yaz mevsiminin ayları:Haziran, Temmuz, Ağustos")
elif(session=="3"):
    print("Sonbahar mevsiminin ayları:Eylül, Ekim, Kasım")
elif(session=="4"):
    print("Kış mevsiminin ayları:Aralık, Ocak, Şubat")
else:
    print("Geçersiz seçim.Lütfen 1,2,3,4 numaralı mevsimlerden birini seçiniz.")
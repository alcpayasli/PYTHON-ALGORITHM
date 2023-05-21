dist = eval(input("Metre olarak uzunluğun değerini giriniz:"))
print("Birimler:\n1.mm\n2.cm\n3.dm\n4.km")
change = input("Çevirmek istediğiniz birim **Örneğin milimetre için 1 yazınız:")
if(change == "1"):
    ndist = 1000*dist
    print("%.2f metre %.4f milimetredir" %(dist, ndist))
elif(change == "2"):
    ndist = 100*dist
    print("%.2f metre %.4f santimetredir" %(dist, ndist))
elif(change == "3"):
    ndist = 10*dist
    print("%.2f metre %.4f desimetredir" %(dist, ndist))
elif (change == "4"):
    ndist = dist/1000
    print("%.2f metre %.4f kilometredir" %(dist, ndist))
else:
    print("Geçersiz seçim")

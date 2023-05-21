height = float(input("Boyunuzu metre cinsinden giriniz(Örneğin 1.78 gibi):"))
weight = float(input("Kilonuzu giriniz:"))
bki = weight/(height*height)

if(bki<18.5):
    print("Zayıfsınız")
elif(bki>=18.5 and bki<25):
    print("Kilonuz normal")
elif(bki>=25 and bki<30):
    print("Fazla kilolusunuz")
elif(bki>=30 and bki<35):
    print("1.derece obezsiniz")
elif(bki>=35 and bki<40):
    print("2.derece obezsiniz")
else:
    print("3.derece obezsiniz")

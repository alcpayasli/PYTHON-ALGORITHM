x1 = int(input("Dikdörtgenin kordinatının x1 değeri:"))
x2 = int(input("Dikdörtgenin kordinatının x2 değeri:"))
y1 = int(input("Dikdörtgenin kordinatının y1 değeri:"))
y2 = int(input("Dikdörtgenin kordinatının y2 değeri:"))
x3 = int(input("Noktanın x1 değeri:"))
y3 = int(input("Noktanın y1 değeri:"))

if(((x3>x1) and (y3>y1)) and ((x2>x3) and (y2>y3))):
    print("Girilen nokta dikdörtgen içerisinde")
else:
    print("Girilen nokta dikdörtgen içerisinde değil")
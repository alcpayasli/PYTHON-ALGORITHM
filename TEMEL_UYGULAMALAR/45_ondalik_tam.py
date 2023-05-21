"""
Girilen sayının ondalık ve tam kısımlarını ayırma
"""
number = float(input("Ondalıklı sayı giriniz:"))
print("Girilen sayının tam kısmı:%d\nOndalıklı kısmı:%f" %(number//1, number%1))
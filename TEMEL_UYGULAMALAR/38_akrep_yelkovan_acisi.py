hour = int(input("0 ile 11 arasında bir saat giriniz:"))
minute = int(input("0 ile 59 arasında dakikayı giriniz:"))
n = minute/2
hour *= 30
minute*=6
print("Akrepin açısı:%d derece Yelkovanın açısı:%d derece" %(hour+n, minute))

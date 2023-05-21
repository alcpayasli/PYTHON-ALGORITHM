num = int(input("Sayı:"))
k = num
s = 0
while(k!=0):
    print(str(k%10) +".10^" +  str(s) + "+", end = "")
    k = k//10
    s+=1
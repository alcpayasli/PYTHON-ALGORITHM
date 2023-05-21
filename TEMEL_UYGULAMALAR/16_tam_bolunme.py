"""
a sayısının b sayısına tam bölünüp bölünmediği
"""
a_num = int(input("A sayısı:"))
b_bum = int(input("B sayısı:"))

if(a_num % b_bum == 0):
    print("a sayısı b sayısına tam bölünür")
else:
    print("a sayısı b sayısına tam bölünmez")
"""
Derece cinsinden girilen açıyı radyan ve grad'a çevirme
"""

aci_derece = int(input("Açının derecesini giriniz:"))
radyan = aci_derece*3.14/180
grad = 200*aci_derece/180
print("%d derecenin radyanı:%f" %(aci_derece, radyan))
print("%d derecenin gradı:%f" %(aci_derece, grad))
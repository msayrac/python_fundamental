# conditional statements
kosul = 10>20
if(kosul):
    print("if blogu çalıştı")
else:
    print("kosul false oldugu icin calısmadı")


s1 = 30
s2 = 50
if(s1>s2):
    print("s1 > s2")
elif(s1==s2):
    print("s1 == s2 ")
else:
    print("s1 < s2")


username ="ahmet"
password = "123"

if(username=="ahmet" and password=="123"):
    print("username ve password dogru")
else:
    print("username veya password yanlıs")

v1 =float(input("vize1 :"))
v2 =float(input("vize2 :"))
final =float(input("final :"))

ortalama = (v1+v2/2)*0.4 +(final*0.6)
print(ortalama)

sonuc= ortalama>=50 and final>=50
if(sonuc):
    print(ortalama," ortalama ile gectiniz.")
else:
    print(ortalama," ortalama ile kaldınız.")


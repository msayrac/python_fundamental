# operators

# 1 atama = ile assignment yapılır

x,y,z = 10,20,30

a = 5

print(x,y,z,a)

# # hata alırız fazla deger var
# x,y,z = 10,20,30,40
# print(x,y,z)

# * ile fazla degerleri son variable degerine liste olarak atarız
x,y,*z = 10,20,30,40,50
print(x,y,z)

x = x +5

x += 155 # kısa yol ile artırma

x -=5

x *= 2
x /=5

x %=2
x//=5

print(x)

# 2 karsılastırma

x,y,z = 10,20,30
print(x==y) # False

x,y,z = 10,20,10
print(x==z) # False

print(x!=y)

email = "deneme@gmail.com"
sifre ="123"

print(email=="test@gmail.com")
print(sifre=="123")

print(x>y)
print(y<x)

print(x>=y)

# 3 mantıksal

print(True and True)

print(True and False)

print(True or True)

# and or not operators

# and operatoru ıkı tarafta true olmalı
x = 6
print(5<x<15)

x = 20
print(5<x<15)

x = 15
print(5<x<=15)

# or operatoru 1 tanesi True gelmesi yeterlidir

mezuniyet = "lise"
sonuc = mezuniyet =="lise" or mezuniyet=="önlisans" or mezuniyet=="lisans"
print(sonuc)

mezuniyet = "lise"
age =20

sonuc =(mezuniyet =="lise" or mezuniyet=="önlisans" or mezuniyet=="lisans") and age>=18
print("Ehliyet Alabilir :",sonuc)

# not operatoru bir kosulun degilini almaya yarar. True -> False False ->True olur

sonuc != True
print(sonuc)

print(not(sonuc))


# identity operator

a = [1,2,3]
b = a

print(a is not b)
print(a is b)

print("1  da var :",1 in a)

print("Elma yok :",("elma" not in b))

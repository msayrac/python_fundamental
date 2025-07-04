"""
Coklu yorum satırı
"""
# tek yorum satırı
# variables

sayi1 = 10
# değişkenler sayı ile baslayamaz
# Türkçe karakter içermemelidir

a, b, c = 10,20,30
print(a,b,c)

x = 1
print(type(x))

y = 1.5
print(type(y))

name = "ALi"
print(type(name))
print(type(True))

a = 10
b = 20
toplam = a+b
print(toplam)

a = "10"
b = "20"
toplam = a+b
print(toplam)

ogrenciAdi = "Çınar"
ogrenciSoyad = "Turan"
ogrenciAdSoyad = ogrenciAdi + " " + ogrenciSoyad
ogrenciCinsiyet = True # Erkek
ogrenciCinsiyet = False # Kadın
ogrenciTcKimlik = "12345678910"
ogrenciDogumYili = 2017

ogrenciYas = 2025 - ogrenciDogumYili
ogrenciAdress = "Kocaeli İzmit"


print(ogrenciAdSoyad)
print(ogrenciCinsiyet)
print(ogrenciYas)


# uygulama 2

urun1 = 50
urun2 = 60.5
urun3 = 356.45

toplam = urun1 + urun2 + urun3

print("Ürün toplamı :",toplam)

# casting

x = "10"
y = "20"

toplam = x+ y
print(toplam)

x  = int(input("x : "))
y  = int(input("y : "))
toplam = x+y
print(toplam)


# int to float

print(float(15))

# float to int

print(int(35.4))

# bool to str
status = True
print(str(status))

# bool to int

print(int(status))


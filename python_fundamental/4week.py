

urunAdi = "Elma"
fiyat = 15
miktar = 2.5

sonuc =str(miktar) + " kg "+ urunAdi+ " için ödemeniz gereken ücret " + str(fiyat*miktar)

print(sonuc)

# format

sonuc1 = "format : {} kg {} için ödemeniz gereken ücret {} TL".format(miktar,urunAdi,(miktar*fiyat))
print("*************")
print(sonuc1)


# f- string

sonuc2 = f"f-string : {miktar} kg {urunAdi} için ödemeniz gereken ücret {(miktar*fiyat)} Tl"
print(sonuc2)

msg ="Merhaba python. Nasılsın"
print(msg.upper())
print(msg.lower())
print(msg.lower().islower())

print(msg.split()) # split ile bir listeye cevirdik

print(msg.split(".")) # nokta dan liste halinde ayırma yapar

print(msg.replace(".","*")) # noktayı * ile replace eder

# python da listeler / array

isim = "Çınar"
isim2 = "Ali"
isim3 = "Deniz"

isimler = ["Çınar","Ali","Deniz","Deniz"]
print(isimler[1])

# list veri tipi : elemanlar sıralanabilir degisitirlebilir elemalar tekrar edilebilir

print(type(isimler))

notlar = [70,80,50]
print(f"{isimler[0]} isimli ögrencisnin notu : {notlar[0]}")
print(f"{isimler[1]} isimli ögrencisnin notu : {notlar[1]}")
print(f"{isimler[2]} isimli ögrencisnin notu : {notlar[2]}")

# nested list
ogrenciler = [
    ["Çınar",70],
    ["Ali",80],
    ["Deniz",50]
]

print(ogrenciler[0])
print(ogrenciler[0][0])
print(ogrenciler[0][1])

arabaMarkalari = ["opel","mazda","toyota","bmw"]

print(arabaMarkalari[0:3]) #son index 3 dahil degil
# sıfır bilgisini yazmaay gerek yok
print(arabaMarkalari[:3])

print(arabaMarkalari[1:])

print(arabaMarkalari[::-1]) # tersten yazdırır

# elemanlar degistirilebilir
arabaMarkalari[0:2]  =["citroen","audi"]

print(arabaMarkalari)


# liste metodları

urunler = ["samsung s20","samsung s21","samsung s22"]
print(urunler)
urunler.insert(1,"iphone x") # 1 index e ekle
print(urunler)

urunler.insert(-1,"iphone 12") # -1 indexe ekle
print(urunler)

urunler.insert(len(urunler),"iphone 13") # iphone sona ekler
print(urunler)

urunler.remove("samsung s20")
print(urunler)

urunler.pop() # son elemanı siler
print(urunler)

urunler.pop(0) # ilk elemanı siler
print(urunler)

del urunler[0]
print(urunler)

# del urunler # listeyi komple siler
# print(urunler)

urunler.clear() # sadece elemanları siler
print(urunler)

urunler = ["samsung s20","samsung s21","samsung s22"]

urunler2 = urunler.copy()
print(urunler2)

# liste genisletme
urunler3 = ["tv","table","pc"]
urunler.extend(urunler3)
print(urunler)
 # ya da 

print(urunler+ urunler3)

# reverse(), sort(), min(), max() vb metodlarda kullanılabilir

# uygulama

isimler = []

isim = input("isim :")
isimler.append(isim)

isim = input("isim :")
isimler.append(isim)

isim = input("isim :")
isimler.append(isim)

print(isimler)











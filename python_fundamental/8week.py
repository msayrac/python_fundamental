# loops

urunler = ["iphone 12","samsung 22","iphone 13","iphone 13 pro"]

for urun in urunler:
    print(urun)

fiyatlar = [8000, 10000,13000,17000]

for fiyat in fiyatlar:
    if(fiyat>=10000):
        print(fiyat)


for urun in urunler:
    if urun.startswith("i"):
        print(urun)
count =0
for urun in urunler:
    if urun.find("iphone")> -1:
        count+=1
        print(urun)
        print(count)


telefonlar =[
    {"urun_ad":"iphone 8","fiyat":4000},
    {"urun_ad":"iphone X","fiyat":6000},
    {"urun_ad":"iphone 12","fiyat":8000},
    {"urun_ad":"iphone 13","fiyat":14000},
    {"urun_ad":"iphone 13 pro","fiyat":24000}
]

for telefon in telefonlar:
    print(telefon["urun_ad"])
    print(telefon["fiyat"])

print("****************************")
toplam = 0
for telefon in telefonlar:
    toplam += telefon["fiyat"]

print("Toplam telefon fiyatı :", toplam)

for telefon in telefonlar:
    if telefon["fiyat"]>8000:
        print(telefon["urun_ad"])


# tekrarlayan işlemlerde while kullanırız

sayilar = [1,3,6,8,9]

i=0

while i<5:
    i +=1
    print(i,"Merhaba")
    

i=0

while i<len(sayilar):
    print(sayilar[i])
    i += 1

adet =int(input("Kaç adet sayı eklemek istersiniz? : "))
urunler = []

i = 0

while(i < adet):
    urunAdi =input("urun adı :")
    fiyat =input("Fiyat : ")
    urunler.append({
        "urunAdi":urunAdi,
        "fiyat":fiyat
        })
    i += 1

for urun in urunler:
    print(f"urun adi : {urun["urunAdi"]}, {urun["fiyat"]}")

# kosula baglı olarka kosul gerceklestigi surece while ile de loop olusturabiliriz


# start stop step
for i in range(2,10,3):
    print(i)

for i in range(5,-2,-1):
    print(i)

sayilar = []

for i in range(1,10,2):
    sayilar.append(i)
print(sayilar)

# list compherension
sayilar2 = [i**2 for i in range(1,5)]
print(sayilar2)
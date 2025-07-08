# tuple veriler değişmez
# liste degistiirlebilir ancak tuple degistiirlemez

_liste = [3,5,7]
_tuples = (1,3,5,7)

print(type(_liste))
print(type(_tuples))

# tuple ==> sıralanabilir, tekrarlanabilir, elemanlar güncellenemez. Remove append metodları bulunmaz

sonuc = _tuples[0]
print(sonuc)
print(len(_tuples))

_liste.append(10)
# _tuples.append(5) # tuple ekleme yapılmaz

_tuple2= (2,3,6)

print(_tuples+_tuple2)

# print(_tuple2 + _liste) # can only concatenate tuple (not "list") to tuple

print(_tuple2 + tuple(_liste)) # casting

_tuple3 = 10,30,20 # bu sekılde de parantez olmadan tuple olusturabiliriz

print(_tuple3)


# dictionary data type

thedict ={
    "brand":"Ford",
    "model":""
}

plakalar = {
    34 :"İstanbul",
    53 : "Rize",
    41 :"Kocaeli"
}

print(plakalar[41])
print(plakalar[53])


rehber = {
    "Sadık Kaya":["123456","326541254"],
    "Çınar Mert" : {
        "ev":"2565412335",
        "iş":"1232121",
        "cep":"254412541",
        "adres":{
            "mahalle":"Atatürk Mah.",
            "cadde" : "Sürmene Sok.",
            "No":35,
            "Şehir":"Kocaeli"
        }

    }
}

print(rehber["Sadık Kaya"])

print(rehber["Çınar Mert"])

print(rehber["Çınar Mert"]["ev"])

print(rehber["Çınar Mert"])

print(rehber["Çınar Mert"]["adres"]["Şehir"])

print(rehber["Çınar Mert"]["adres"]["mahalle"])

# json veri yapısına karsılık gelir json veri yapısı


p1 = {
    "name":"samsung s20",
    "price":6000
}

print(p1["name"])

print(p1["price"])

print(p1.get("price"))
print(p1.get("name"))

_keys =p1.keys() # key degerlerini liste halinde getiriyor

_values = p1.values() # butun value degerleri geliyor

print(_keys)
print(_values)

_items = p1.items()

print(_items) # tüm elemanlar key ve value olarak gelir

for x in _keys:
    print(x)

for a in p1.values():
    print(a)

for i in p1.items():
    print(i)

for i in p1.items():
    print(i[0])

for i in p1.items():
    print(i[1])

for key,value in p1.items():
    print(key,value)

p1["price"] = 1000
print(p1["price"])

# update eslesen key yoksa ekleme yapılır varsa guncelleme yapılır
p1.update(
    {"name":"samsung s21",
     "price":12000,
     "description":"iyi telefon"
     }
)
print(p1["price"])

print(p1)

p1["color"]="Red"
print(p1)

p1.popitem() # son elemanı siler
print(p1)

# p1.clear() # dict temizler
# print(p1)

# del p1 # dict komple siler
# print(p1)

p2 = {
    "name":"samsung s22",
    "price":8000
}

p1["price"]= "9000"
print(p1)
print(p2)

p1 = p2.copy() # kopyalama yapar bellekte farklı adreste tutar

products = [p1,p2,{
    "name":"samsung s23",
    "price":18000,
    "color":"Beyaz"
}]

print(products)

for p in products:
    print(p)

for p in products:
    print(p.get("name"))

for value in products:
    print(value.values())


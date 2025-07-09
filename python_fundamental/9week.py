"""
1-100 arası random sayı üretimi.
Kullanıcıdan sayı alınıp kac kere bildigi belirlenecektir. Her yanlıs cevap ıcın toplam puanından dusulecektir.
"""

import random

sayi = random.randint(1,10)
print(sayi)

can = int(input("Kaç hak kullanmak istersiniz : "))
hak = can
sayac = 0

while hak>0:
    hak-=1
    tahmin = int(input("Tahmininiz : "))
    sayac +=1

    if(tahmin==sayi):
        print(f"Tebrikler {sayac}. defada bildiniz. Toplam puanınız : {100-(100/can)*(sayac-1)}")
        
        break
    elif sayi>tahmin:
        print("Yukarı")
    else:
        print("Asağı")

    if(hak==0):
        print(f"Hakkınız Bitti. Tutulan sayi : {sayi}")

import time
import matplotlib.pyplot
class yemek():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = True

BEYTI = yemek("Beyti","30 TL")
LEVREK = yemek("Levrek","33 TL")
MANTI = yemek("Mantı","27 TL")
CORBA = yemek("Çorba","15 TL")
GUVEC = yemek("Güveç","26 TL")

menu = [BEYTI.name + "(" + BEYTI.price + ")",
        LEVREK.name + "(" + LEVREK.price + ")",
        MANTI.name + "(" + MANTI.price + ")",
        CORBA.name + "(" + CORBA.price + ")",
        GUVEC.name + "(" + GUVEC.price + ")"
        ]

def yemekEkle():

     try:
        a = str(input(("Yemek İsmi: "))).capitalize()
        b = int(input("Yemek Fiyatı: "))
        yeniYemek = yemek(a,b)
        result = yeniYemek.name + "(" + str(yeniYemek.price) + " TL" + ")"
        menu.append(result)
        print(f"Tebrikler {yeniYemek.name} Başarıyla Listelendi")
        time.sleep(1)
     except ValueError:
         print("Yemek İsmi Harflerden Yemek Fiyatı Rakamlardan Oluşmalıdır!!!!")
         yemekEkle()


while True:

    print("""
    
    SAYIN YÖNETİCİ;
    
    LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİN
    
    [1] Kullanıcı Gözünden Kullanım
    
    
    [2] Satış Verileri
    
    
    [3] Puan Grafiği
    
    
    [4] Yemek Ekleme
    """)

    choice = int(input("     Seçiminiz: "))


    if choice == 3:
        aylar = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]
        puanlar = [7.9,8.1,8.3,8.4,9,8.9,8.8,8.2,7.3,6.4,5.8,5.3]
        matplotlib.pyplot.figure(num=16,figsize=(14,5))
        matplotlib.pyplot.xlabel("Aylar")
        matplotlib.pyplot.ylabel("Ortalama Puan")
        matplotlib.pyplot.title("2020 Yılında Aylara Göre Restorant Puan Ortalaması")
        matplotlib.pyplot.bar(aylar,puanlar)
        matplotlib.pyplot.show()

    if choice ==2:
        aylar =["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım","Aralık"]
        kar = [50,54 ,56 ,48 ,55,45,45,37,32,29 ,27 ,25]
        matplotlib.pyplot.figure(num=16, figsize=(14, 5))
        matplotlib.pyplot.xlabel("Aylar")
        matplotlib.pyplot.ylabel("TL Cinsinden Net Kar (BİN TL)")
        matplotlib.pyplot.title("2020 Yılında Aylara Göre Satış Dağılım Verileri")
        matplotlib.pyplot.bar(aylar,kar)
        matplotlib.pyplot.show()

    if choice == 4:
        yemekEkle()


    if choice == 1:
        print("""
    
        DEĞERLİ MÜŞTERİMİZ
    
        SİPARİŞ VERMEK İÇİN 1'İ 
    
        SİPARİŞİNİZİ PUANLAMAK İÇİN 2'Yİ 
    
        ÇIKMAK İÇİN LÜTFEN 3'Ü TUŞLAYINIZ
    
        """)

        choice2 = int(input("Seçiminiz: "))

      
        if choice2 == 1:
            x = 0
            y = 1
            while True:
                print(f"{menu[x]} için {y} tuşlayınız")
                x += 1
                y += 1
                if x == len(menu):
                    break

            choice3 = int(input("Seçiminiz: "))
            print(f"{menu[choice3-1]} siparişiniz onaylanmıştır")
            time.sleep(3)

        if choice2 == 2:
            print("""Siparişinizi Puanlamak İçin Lütfen 1-10 Arası Değerler Giriniz""")
            speed = int(input("Hız: "))
            time.sleep(0.3)
            service = int(input("Servis: "))
            time.sleep(0.3)
            flavor = int(input("Lezzet :"))
            result = (speed+service+flavor) // 3
            if (speed < 0 or speed > 10 ) or (service < 0 or service > 10) or (flavor < 0 or flavor > 10):
                print("Sadece 1-10 arası değerler verebilirsiniz!")
                time.sleep(2)
                continue
            print(f"Teşekkürler Restorantımıza {result} Puan Verdiniz")
            time.sleep(1)

        if choice2 ==3:
            print("Hoşçakalın")
            time.sleep(1)
            quit()

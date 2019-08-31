class Muzik_calar:

    def __init__(self, sarkilistesi=[]):
        self.sarkilistesi = sarkilistesi


    def sarki_ekleme(self, sarkici, sarki):
        print("Sarki listenize ekleme yapiliyor...")
        time.sleep(1)
        parca = sarkici, sarki
        self.sarkilistesi.append(parca)
        sarkim.liste_goruntule()

    def sarki_silme(self, sarki):
        for i in self.sarkilistesi:
            if i[1] == sarki:
                sarki_yeri = self.sarkilistesi.index(i)
                self.sarkilistesi.pop(sarki_yeri)
                print("Isteginiz uzere sarki siliniyor. Lutfen bekleyiniz...")
                time.sleep(1)
        sarkim.liste_goruntule()

    def sarki_sifirla(self):
        self.sarkilistesi.clear()
        print("Isteginiz uzere sarki listesi sifirlaniyor. Lutfen bekleyiniz...")
        time.sleep(1)
        sarkim.liste_goruntule()

    def liste_goruntule(self):
        print(sarkim.sarkilistesi)

    def onceki_sarki(self, oncekinin_sirasi):
        print("Istediginiz sarki caliniyor.", self.sarkilistesi[oncekinin_sirasi])

    def sonraki_sarki(self, sonrakinin_sirasi):
        print("Istediginiz sarki caliniyor.", self.sarkilistesi[sonrakinin_sirasi])

    def karisik_sarki(self):
        siradaki= int(len(self.sarkilistesi)) - 1
        siradaki = random.randint(0, siradaki)
        print("Istediginiz sarki caliniyor.", self.sarkilistesi[siradaki])

sarkim = Muzik_calar()


print("""Muzik calar programimiza hosgeldiniz.
Lutfen yapmak istediginiz islemi seciniz\n
        Sarki ekleme                    1
        Sarki silme                     2
        Sarki listesini sifirla         3
        Sarki listesini goruntule       4
        Sarki calma duzeni belirle      5
""")

import time
import random

while True:                                                                         # muteaadit islem yapilacagi icin dongu olusturduk

    islem = input("\nLutfen yapmak istediginiz islemi seciniz : ")                  # kullanicidan yapacagi islemi talep ettik

    if islem == "1":                                                                # kullanicinin rehbere ekleme yapma secenegini kodladik
        sarkici = input("Sarkicinin adini giriniz : ")                                                         # kullanicidan verileri aldik
        sarki = input("Sarkinin adini giriniz : ")

        sarkim.sarki_ekleme(sarkici, sarki)


    elif islem == "2":
        sarki = input("Sarkinin adini giriniz : ")

        sarkim.sarki_silme(sarki)


    elif islem == "3":
        sarkim.sarki_sifirla()


    elif islem == "4":
        sarkim.liste_goruntule()


    elif islem == "5":
        print("""
        Sarki dinleme secenekleri :
        Onceki sarki        1
        Sonraki sarki       2
        Karisik             3
        """)
        sarki_tercihi=input("Lutfen dinlemek istediginiz sarki ile ilgili tercihinizi giriniz : ")

        if sarki_tercihi == "1":
            mevcudun_sirasi=int(input("Su anda dinlediginiz sarkinin sira numarasini giriniz : "))
            oncekinin_sirasi = mevcudun_sirasi - 2
            sarkim.onceki_sarki(oncekinin_sirasi)

        elif sarki_tercihi == "2":
            mevcudun_sirasi=int(input("Su anda dinlediginiz sarkinin sira numarasini giriniz : "))
            sonrakinin_sirasi = mevcudun_sirasi
            sarkim.onceki_sarki(sonrakinin_sirasi)

        elif sarki_tercihi == "3":
            sarkim.karisik_sarki()
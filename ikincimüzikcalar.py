import time as zaman
import random as rastgele

class Winamp():

    def __init__(self, sarkilar = []):
        self.sarkilar = sarkilar
        self.durum = True
        self.ses = 100
        self.calanSarki = " "


    def sesArttir(self):
        if (self.ses >= 95):
            pass

        else:

            print("Ses artiriliyor")
            zaman.sleep(2)
            self.ses += 5
            print("Ses arttirildi. Güncel Ses: {} ".format(self.ses))


    def sesAzalt(self):
        if (self.ses <= 0):
            pass
        else:
            print("Ses azaltiliyor")
            zaman.sleep(2)
            self.ses -= 5
            print("Ses azaltildi. Güncel Ses: {} ".format(self.ses))


    def sarkiEkle(self, sarki):
        self.sarkilar.append(sarki)


    def sarkiListesi(self):
        print(self.sarkilar)


    def sarkiSec(self):
        sayac = 1
        for i in self.sarkilar:
            print("{}.{}".format(sayac, 1))
        secim = int(input("Sarki numarasini giriniz :"))
        print("Sarki degistiriliyor")
        zaman.sleep(2)
        self.calanSarki = self.sarkilar[secim]
        print("Sarki degistirildi, suan calan sarki = {}".format(self.calanSarki))


    def rastgeleSarki(self):
        rastgele_sayi = rastgele.randint(0, len(self.sarkilar))
        self.calanSarki = self.sarkilar[rastgele_sayi]


    def kapa(self):
        self.durum = False


    def sarkiSil(self):
        secim = int(input("Silmek istediginiz sarkinin numarasini giriniz: "))
        self.sarkilar.pop(secim)


    def arayüz(self):
        print("""
                Sarki Listesi = {}
                Suan Calan Sarki = {}
                Ses = {}
                Durum {}
                1 -Sarki Sec
                2 -Ses Arttir
                3 -Ses Azalt
                4 -Rastgele Sarki Sec
                5 - Sarki Ekle
                6 -Sarki Sil
                7-Kapa

                Secim: """.format(self.sarkilar, self.calanSarki,self.ses , self.durum))


o1 = Winamp (sarkilar = [ "Erkin Koray - Saskin" ])


while o1.durum:
    o1.arayüz()
    secim = int(input("Seciminizi girebilirsiniz: "))
    if (secim == 1):
        o1.sarkiSec()
    elif (secim == 2):
        o1.sesArttir()
    elif (secim == 3):
        o1.sesAzalt()
    elif (secim == 4):
        o1.rastgeleSarki()
    elif (secim == 5):
        sarki = input("Sarki giriniz : ")
        o1.sarkiEkle(sarki)
    elif (secim == 6):
        o1.sarkiSil()
    else:
        o1.kapa()
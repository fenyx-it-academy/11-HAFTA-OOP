""" Bir muzik calar objesi yapmanizi istiyoruz. Instance(Object) attribute olarak bos bir sarki listesi olusturun.
 Class methods olarak sarki listesini
 ~sifirlama,
 ~listeyi goruntuleme,
 ~sarki ekleme,
 ~sarki silme,
 ~sonraki parcayi cal,
 ~onceki parcayi cal,
 ~karisik cal
 ozelliklerini ekleyin."""


import time
import random



class MuzikCalar():
    muzik_liste=[]
    def __init__(self,sarki_ad='unknown',sarki_sanatci="",sarki_tur='unknown'):
        self.sarki_ad=sarki_ad
        self.sarki_sanatci=sarki_sanatci
        self.sarki_tur=sarki_tur

    def __str__(self):
        return "sarki isimi:   {}\n".format(self.sarki_ad)      #sarkilarin sadece ismini goruntulemesini tercih ettim.
    @classmethod
    def liste_sifirlama(cls):
        print("Listedeki parcalar siliniyor..")
        time.sleep(2)
        MuzikCalar.muzik_liste.clear()



    @classmethod
    def sarki_ekle(cls):
        print("Listeye ekleyeceginiz yeni sarkinin:")
        ad=input("Sarki adi:")
        sure=input("Sarkiyi seslendiren sanatci:")
        tur=input("Sarkinin turu:")
        if ad=="":
            yeni_sarki=MuzikCalar('sarki'+str(len(MuzikCalar.muzik_liste)+1),sure,tur) #kullanici sarki ismini bos girerse sarki1 sarki2 diye adlandiracak
            MuzikCalar.muzik_liste.append(yeni_sarki)
        else:
            yeni_sarki = MuzikCalar(ad, sure, tur)
            MuzikCalar.muzik_liste.append(yeni_sarki)

        print("{} isimli sarki listeye eklendi".format(yeni_sarki.sarki_ad))

    @classmethod
    def liste_goruntule(cls):
        print("muzik listesi goruntuleniyor...")
        print()
        for i in MuzikCalar.muzik_liste:
            print(i)

    @classmethod
    def sarki_silme(cls):
        print("Listeden sarki silmek icin liste goruntuleniyor:")
        MuzikCalar.liste_goruntule()

        while True:
            sarkisil=input("listeden silmek istediginiz sarki ismini giriniz:(cikis icin q)")
            if sarkisil == "q":
                print("Anamenuye donuluyor..")
                break
            else:
                for i in MuzikCalar.muzik_liste:
                    if i.sarki_ad == sarkisil:
                        MuzikCalar.muzik_liste.remove(i)
                        print("{} isimli sarki listeden silindi".format(sarkisil))
                        break

                else:
                    print("silmek istediginiz sarki listede bulunamamistir")

    @classmethod
    def calan_parca(self):
        i = 0
        while True:
            print(f"{MuzikCalar.muzik_liste[i]} sarkisi caliyor...")
            time.sleep(2)
            print("""
            (1) sonraki parcaya gec
            (2) onceki parcaya gec
            (3) karisik cal
            (q) cikis""")
            parca_sec=input("yapmak istediginiz islemi seciniz:")
            if parca_sec == "q":
                break
            elif parca_sec not in ["1","2","3"]:
                print("gecersiz islem numarasi")
            elif parca_sec =="1":
                i=(i+1)%len(MuzikCalar.muzik_liste)
            elif parca_sec == "2":
                i = (i - 1) % len(MuzikCalar.muzik_liste)
            elif parca_sec == "3":
                i=random.randint(0,len(MuzikCalar.muzik_liste)-1)

print("Muzik Calar baslatiliyor")
while True:

    print("""  
  (1)   listeyi goruntule,
  (2)   sarki ekle,
  (3)   sarki sil,
  (4)   sarki cal
  (5)   listeyi sifirlama,
  (q)   cikis """)
    print()
    islem=input("islem numarasi:")

    if islem == "q":
        break

    elif islem not in ["1","2","3","4","5"]:
        print("gecersiz islem numarasi")

    elif islem == "1":
        MuzikCalar.liste_goruntule()
    elif islem == "2":
        MuzikCalar.sarki_ekle()
    elif islem == "3":
        MuzikCalar.sarki_silme()
    elif islem == "4":
        MuzikCalar.calan_parca()
    elif islem == "5":
        MuzikCalar.liste_sifirlama()












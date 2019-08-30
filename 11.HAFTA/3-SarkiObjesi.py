"""Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi  olusturun.
 Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin."""
class MuzikCalar():
    sarki_listesi = []
    def __init__(self,sarki):
        self.sarki = sarki
        self.sarki_ekle()
    def sarki_ekle(self):
        self.sarki_listesi.append(self.sarki)
        print("{} adli sarki listeye eklendi".format(self.sarki))
    def listeyi_goruntule(self):
        for sarki in self.sarki_listesi:
            print(sarki)
    def sarki_silme(self):
        try:
            silinecek = int(input("silinecek sarkinin sirasini girin,sarki sirasi 0 dan baslamaktadir"))
            if silinecek in self.sarki_listesi[silinecek]:
                del self.sarki_listesi[silinecek]
                print("{} numarali sarki silindi".format(self.sarki_listesi[silinecek]))
            else:
                print("listenizde boyle bir sarki yok")
        except:
            print("hatali giris")

    def listeyi_sifirlama(self):
        self.sarki_listesi.clear()

    def sonraki_parca(self):
        try:
            calinan_parca = int(input("caldiginiz parca no"))
            if calinan_parca in self.sarki_listesi:
                print("{} numarali sarkiyi dinliyorsunuz...♫ ♫ ♫ ♫".format(self.sarki_listesi[calinan_parca+1]))
            else:
                print("listenizde boyle bir sarki yok")
        except:
            print("hatali giris")

    def onceki_parca(self):
        try:
            calinan_parca = int(input("caldiginiz parca no,sarki sirasi 0 dan baslamaktadir"))
            if calinan_parca in self.sarki_listesi:
                print("{} numarali sarkiyi dinliyorsunuz...♫ ♫ ♫ ♫".format(self.sarki_listesi[calinan_parca-1]))
            else:
                print("listenizde boyle bir sarki yok")
        except:
            print("hatali giris")

    def karisik_cal(self):
        import random
        karisik = random.randint(0,len(self.sarki_listesi))
        print("{} numarali sarki caliyor...♫ ♫ ♫ ♫".format(karisik))
muzikcalar = MuzikCalar("yeni bir dunya")



while True:
    print(""""
    ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ 
    sarki listesi secenekleri:
    (1) sarki ekle
    (2) listeyi goruntule
    (3) sarki silme
    (4) listeyi sifirlama
    (5) sonraki parca
    (6) onceki parca
    (7) karisik cal
    ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ ♫ 
    """)
    try:
        secenek = int(input("yapmka istediginiz islemi seciniz: "))
        if secenek == 1:
            muzikcalar.sarki_ekle()
        elif secenek == 2:
            muzikcalar.listeyi_goruntule()
        elif secenek == 3:
            muzikcalar.sarki_silme()
        elif secenek == 4:
            muzikcalar.listeyi_sifirlama()
        elif secenek == 5:
            muzikcalar.sonraki_parca()
        elif secenek == 6:
            muzikcalar.onceki_parca()
        elif secenek == 7:
            muzikcalar.karisik_cal()
        else:
            print("hatali giris")
    except:
        print("hatali secenek")


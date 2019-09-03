#Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun.
# Class methods olarak sarki listesini sifirlama,
#listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal,
# karisik cal ozelliklerini ekleyin.
import time
import random
class Muzikcalar():
    __sarkilistesi = [] # disaridan erisimi engellemek icin gizlendi
    calinan_sarki = ""

    @classmethod
    def sarki_cal(cls, sarki):
        if sarki in cls.__sarkilistesi:
            print(sarki, "Caliniyor...")
            cls.calinan_sarki = sarki
        else:
            print("Sarki listenizde boyle bir sarki mevcut degil...")

    @classmethod
    def sarkilistesi_sifirla(cls):
        cls.__sarkilistesi.clear()
        cls.calinan_sarki = ""
        print("\nSarki Listeniz Sifirlandi...")

    @classmethod
    def sarkilistesi_goruntule(cls):
        print("\nSarki Listesi\n")
        for sarki in cls.__sarkilistesi:
            print(sarki)

    @classmethod
    def sarki_ekle(cls, sarki):
        print("\n", sarki, "eklendi...")
        cls.__sarkilistesi.append(sarki)

    @classmethod
    def sarki_sil(cls, sarki):
        cls.__sarkilistesi.pop(cls.__sarkilistesi.index(sarki))
        print('\n', sarki, "silindi..")
        if sarki == cls.calinan_sarki:
            cls.calinan_sarki = ""

    @classmethod
    def sonrakisarki_cal(cls):
        if cls.calinan_sarki == "":
            print("Once bir sarki calmalisniz...")
        else:
            index = cls.__sarkilistesi.index(cls.calinan_sarki)
            if index + 1 == len(cls.__sarkilistesi):
                cls.sarki_cal(cls.__sarkilistesi[0])
            else:
                cls.sarki_cal(cls.__sarkilistesi[index + 1])

    @classmethod
    def oncekisarki_cal(cls):
        if cls.calinan_sarki == "":
            print("Once bir sarki calmalisniz...")
        else:
            index = cls.__sarkilistesi.index(cls.calinan_sarki)
            if index == 0:
                cls.sarki_cal(cls.__sarkilistesi[len(cls.__sarkilistesi) - 1])
            else:
                cls.sarki_cal(cls.__sarkilistesi[index - 1])

    @classmethod
    def karisik_cal(cls):
        calinan_sarkilar = [] # surekli random dan ayni sarkinin calinmasini engellemek icin, onceden calinanlarin listesi
        while len(calinan_sarkilar) < len(cls.__sarkilistesi):
            karisik = random.randint(0, len(cls.__sarkilistesi)-1)
            if karisik in calinan_sarkilar:
                continue
            else:
                cls.sarki_cal(cls.__sarkilistesi[karisik])
                calinan_sarkilar.append(karisik)


Muzikcalar.sarki_ekle("Mehmet Erdem - Oyle Bir Yerdeyim Ki")
Muzikcalar.sarki_ekle("Mehmet Erdem - Aglayamam")
Muzikcalar.sarki_ekle("Sezai - Kimseye Etmem Sikayet")
Muzikcalar.sarki_ekle("Tamino - Habibi")
Muzikcalar.sarkilistesi_goruntule()
Muzikcalar.sarki_sil("Tamino - Habibi")
Muzikcalar.sarki_cal("Mehmet Erdem - Aglayamam")
Muzikcalar.sonrakisarki_cal()
Muzikcalar.oncekisarki_cal()
Muzikcalar.karisik_cal()

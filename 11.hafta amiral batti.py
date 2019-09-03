"""Odev 1: Gecen hafta basladigimiz amiral batti oyununu gelistirecegiz.
Bu hafta kodunuzu Object Oriented sekline cevirmenizi istiyoruz. Ayrica randomsuz yapanlarin random gemi
yerlestirme ozelligini eklemelerini bekliyoruz. Bonus ozellik olarak oyunun bilgisayara karsi oynanan
iki kisilik versiyonunu yapabilirsiniz."""


from functools import reduce
from random import randint
from time import sleep

class AmiralBatti:

    __hata_bekleme_suresi = 2

    def __init__(self):
        self.__deniz = []
        self.__kayitliGemiler = []
        self.__kullaniciHakki = 15
        self.__bilinenGemiler = []


    def denizOlustur(self):
        for _ in range(10):
            self.__deniz.append(['0']*10)


    def denizYazdir(self):
        # cikti = reduce(lambda sonuc, satir: sonuc + ' '.join(satir) + '\n', deniz, '')
        # print(cikti)
        print(reduce(lambda sonuc, satir: sonuc + ' '.join(satir) + '\n', self.__deniz, ''))


    def gemiVarMi(self, gemicik):
        cakisangemiler = list(
            filter(lambda gemi: gemi[0] == gemicik[0] and gemi[1] == gemicik[1], self.__kayitliGemiler))  # 0: satir, 1: sutun
        if len(cakisangemiler) > 0:
            return True
        else:
            return False


    def birlikGemiYap(self):
        while True:
            satir = randint(0, 9)
            sutun = randint(0, 9)
            if self.gemiVarMi([satir, sutun]):
                continue
            else:
                return [satir, sutun]


    def ikilikGemiYap(self):
        yeni_satir = -1
        yeni_sutun = -1
        while yeni_satir == -1 and yeni_sutun == -1:
            birinci_birim_gemi = self.birlikGemiYap()
            satir = birinci_birim_gemi[0]
            sutun = birinci_birim_gemi[1]
            if sutun < 9: #saga ekleme
                if not self.gemiVarMi([satir, sutun + 1]):
                    yeni_satir = satir
                    yeni_sutun = sutun + 1
                    return [birinci_birim_gemi, [yeni_satir, yeni_sutun]]
            if sutun > 0: #sola ekleme
                if not self.gemiVarMi([satir, sutun - 1]):
                    yeni_satir = satir
                    yeni_sutun = sutun - 1
                    return [[yeni_satir, yeni_sutun], birinci_birim_gemi]
            if satir < 9: #alta ekleme
                if not self.gemiVarMi([satir + 1, sutun]):
                    yeni_satir = satir + 1
                    yeni_sutun = sutun
                    return [birinci_birim_gemi, [yeni_satir, yeni_sutun]]
            if satir > 0: #uste ekleme
                if not self.gemiVarMi([satir - 1, sutun]):
                    yeni_satir = satir - 1
                    yeni_sutun = sutun
                    return [[yeni_satir, yeni_sutun], birinci_birim_gemi]


    def uclukGemiYap(self):
        yeni_satir = -1
        yeni_sutun = -1
        while yeni_satir == -1 and yeni_sutun == -1:
            iki_birimlik_gemi = self.ikilikGemiYap()
            ilk_birim_gemi = iki_birimlik_gemi[0]
            ikinci_birim_gemi = iki_birimlik_gemi[1]
            if ilk_birim_gemi[0] == ikinci_birim_gemi[0]: #yatay gemi
                if ikinci_birim_gemi[1] < 9: #geminin sagindaki birim kontrolu
                    if not self.gemiVarMi([ikinci_birim_gemi[0], ikinci_birim_gemi[1] + 1]):
                        yeni_satir = ikinci_birim_gemi[0]
                        yeni_sutun = ikinci_birim_gemi[1] + 1
                        return [ilk_birim_gemi, ikinci_birim_gemi, [yeni_satir, yeni_sutun]]
                if ilk_birim_gemi[1] > 0:  # geminin solundaki birim kontrolu
                    if not self.gemiVarMi([ilk_birim_gemi[0], ilk_birim_gemi[1] - 1]):
                        yeni_satir = ilk_birim_gemi[0]
                        yeni_sutun = ilk_birim_gemi[1] - 1
                        return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi]
            else: #dikey gemi
                if ikinci_birim_gemi[0] < 9: #geminin altindaki birim kontrolu
                    if not self.gemiVarMi([ikinci_birim_gemi[0] + 1, ikinci_birim_gemi[1]]):
                        yeni_satir = ikinci_birim_gemi[0] + 1
                        yeni_sutun = ikinci_birim_gemi[1]
                        return [ilk_birim_gemi, ikinci_birim_gemi, [yeni_satir, yeni_sutun]]
                if ilk_birim_gemi[0] > 0:  # geminin ustundeki birim kontrolu
                    if not self.gemiVarMi([ilk_birim_gemi[0] - 1, ilk_birim_gemi[1]]):
                        yeni_satir = ilk_birim_gemi[0] - 1
                        yeni_sutun = ilk_birim_gemi[1]
                        return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi]


    def dortlukGemiYap(self):
        yeni_satir = -1
        yeni_sutun = -1
        while yeni_satir == -1 and yeni_sutun == -1:
            uc_birimlik_gemi = self.uclukGemiYap()
            ilk_birim_gemi = uc_birimlik_gemi[0]
            ikinci_birim_gemi = uc_birimlik_gemi[1]
            ucuncu_birim_gemi = uc_birimlik_gemi[2]
            if ilk_birim_gemi[0] == ikinci_birim_gemi[0]: #yatay gemi
                if ucuncu_birim_gemi[1] < 9: #geminin sagindaki birim kontrolu
                    if not self.gemiVarMi([ucuncu_birim_gemi[0], ucuncu_birim_gemi[1] + 1]):
                        yeni_satir = ucuncu_birim_gemi[0]
                        yeni_sutun = ucuncu_birim_gemi[1] + 1
                        return [ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi, [yeni_satir, yeni_sutun]]
                if ilk_birim_gemi[1] > 0:  # geminin solundaki birim kontrolu
                    if not self.gemiVarMi([ilk_birim_gemi[0], ilk_birim_gemi[1] - 1]):
                        yeni_satir = ilk_birim_gemi[0]
                        yeni_sutun = ilk_birim_gemi[1] - 1
                        return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi]
            else: #dikey gemi
                if ucuncu_birim_gemi[0] < 9: #geminin altindaki birim kontrolu
                    if not self.gemiVarMi([ucuncu_birim_gemi[0] + 1, ucuncu_birim_gemi[1]]):
                        yeni_satir = ucuncu_birim_gemi[0] + 1
                        yeni_sutun = ucuncu_birim_gemi[1]
                        return [ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi, [yeni_satir, yeni_sutun]]
                if ilk_birim_gemi[0] > 0:  # geminin ustundeki birim kontrolu
                    if not self.gemiVarMi([ilk_birim_gemi[0] - 1, ilk_birim_gemi[1]]):
                        yeni_satir = ilk_birim_gemi[0] - 1
                        yeni_sutun = ilk_birim_gemi[1]
                        return [[yeni_satir, yeni_sutun], ilk_birim_gemi, ikinci_birim_gemi, ucuncu_birim_gemi]


    def gemileriDenizeEkle(self):
        for i in range(2):
            dortluk_gemi = self.dortlukGemiYap()
            for gemi in dortluk_gemi:
                self.__kayitliGemiler.append(gemi)
            ucluk_gemi = self.uclukGemiYap()
            for gemi in ucluk_gemi:
                self.__kayitliGemiler.append(gemi)
            ikilik_gemi = self.ikilikGemiYap()
            for gemi in ikilik_gemi:
                self.__kayitliGemiler.append(gemi)
            self.__kayitliGemiler.append(self.birlikGemiYap())


    def bilgilendirmeVeKontrol(self):
        print('Kalan deneme sayiniz:', self.__kullaniciHakki)
        print("Gemi koordinatinda satir ve sutun bilgileri:")
        satir = int(input("Satir giriniz: "))
        sutun = int(input("Sutun giriniz: "))
        if not self.gemiVarMi([satir, sutun]):
            print('Isabet ettiremediniz!!!')
            self.__kullaniciHakki = self.__kullaniciHakki - 1
            self.__deniz[satir][sutun] = ' '
            sleep(AmiralBatti.__hata_bekleme_suresi)
        else:
            if [satir, sutun] in self.__bilinenGemiler:
                print("Daha onceden bu gemiyi bildiniz.")
            else:
                print("Bir gemiye denk geldiniz!!!!")
                self.__bilinenGemiler.append([satir, sutun])
            self.__deniz[satir][sutun] = 'X'
        self.denizYazdir()

    def oyunuBaslat(self):
        self.denizOlustur()
        self.gemileriDenizeEkle()
        self.denizYazdir()
        while self.__kullaniciHakki > 0:
            self.bilgilendirmeVeKontrol()
            if len(self.__bilinenGemiler) == len(self.__kayitliGemiler):
                print("TEBRIKLER: Kazandiniz.")
                break
        if self.__kullaniciHakki == 0:
            print("Basarisiz oldunuz... :(")

oyun = AmiralBatti()
oyun.oyunuBaslat()
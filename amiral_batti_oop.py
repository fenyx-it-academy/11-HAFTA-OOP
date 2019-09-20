from random import*
import secrets
from time import*
class TahtaOlustur():
    # tablonun her bir kutucugu ikili sayi listesinden olusuyor.tum kutucuklar tek bir liste icinde 00 01 43 56..gibi
    def tabloilk(self):
        tbl = [str(i) + str(j) for i in range(10) for j in range(10)]
        return tbl

    def yazdir(self,a, g):  # bir satir ele alindiginda 00   01   02   03 ...aralari 3 bosluklu yaziyor
        for i in range(10):
            print(g[i + a], end=' ' * 3)
        print("\n")

    def gorunen(self, grnn):  # her bir satirin kutucuk numaralrini 3er boslukla yaziyor

        print('')  # tablodan once bir satir bosluk yapar
        self.yazdir(0, grnn)  # 1.satir
        self.yazdir(10, grnn)  # 2.satir
        self.yazdir(20, grnn)  # 3.satir
        self.yazdir(30, grnn)
        self.yazdir(40, grnn)
        self.yazdir(50, grnn)
        self.yazdir(60, grnn)
        self.yazdir(70, grnn)
        self.yazdir(80, grnn)
        self.yazdir(90, grnn)

    def cozumtablosu(self,cozum):  # 15 hakkini bitirip oyunu bitiren oyuncuya cozumu gosterir
        tson = self.tabloilk().copy()
        for i in cozum:  # cozum listesindeki kutukcuklari bul

            yer = int(i)  # bu kumede sayilar str seklindeydi.integer yap
            tson[yer] = "X "  # gemilerin bulundugu yeri X ile goster
        return tson

#     # from amiralrandomcozum import *
#     # simdilik cozum alttaki gibi olsun
# cozum = ['00', '05', '06', '07', '19', '22', '29', '32', '39', '42',
#          '55', '56', '57', '70', '81', '82', '83', '84', '96', '97']

class CozumGemileri(TahtaOlustur):
    def __init__(self,uzunluk):
        self.yatay_dikey=""
        self.uzunluk=uzunluk

    def sayi(self,x,y,i):
        if self.yatay_dikey=="yatay":
        # sayilari 00 01 02.. veya 23 24 25 26 diye yazmasi icin
            s = f"{x}{y + i}"  # ilk sabit ikinciye ekleyerek gitsin
            return s  # string olarak sayi duruyor
        else:
             # sayilari dikeye yerlestirsin
            s = f"{x + i}{y}"  # 23 33 43 53 gibi
            return s

    def kutubirim(self):  # geminin uzunluguna bagliolarak 4 kutu mu sececek 3 kutumu belirliyor
        if self.yatay_dikey=="yatay":
            x = randint(0,9)  # geminin ilk kutusu icin yatayda birler basamagina ekleme yapmayacak.0 dan 9 a istedigini alabilir
            y = randint(0, 10 - self.uzunluk)  # 0dan 9 a kadar secemez.ekleme yapacak yeri bos birakiyor
            # gemi uzunlugu kadar yatayda ardarda gelen sayiyi kume icine atiyor.
        else:
            x = randint(0, 10 - self.uzunluk)  # onlar basamagi artarak gidecek.kuyruga yer birakiyor
            y = randint(0, 9)  # birler basamagi sabit olacak
            # gemi uzunlugu kadar dikey kutucugu kume de tutuyor
        kume=[self.sayi(x, y, i) for i in range(self.uzunluk)]
        return kume
    def gemiolustur(self):
        return self.kutubirim()


    def yerlestir(self,ck):

        while True:
            dikeyyatay = secrets.choice(["yatay", "dikey"])
            # yatay mi dikey mi yerlestircek random karar versin.listelerde random.
            # choice kullanilamiyormus secrets modulu import edilip bu calisiyor
            self.yatay_dikey = dikeyyatay
            a = self.kutubirim()  # yataydikeyi ve uzunlugu belli gemileri yerlestirecek

            if [True for i in a if i in ck]:
                continue
            else:  # aksi halde
                ck.extend(a)  # ck icine koy
                break  # while durdur
        return ck

ck=[]
oyuncu1=TahtaOlustur()
gemi1=CozumGemileri(4)
gemi2=CozumGemileri(4)
gemi3=CozumGemileri(3)
gemi4=CozumGemileri(3)
gemi5=CozumGemileri(2)
gemi6=CozumGemileri(2)
gemi7=CozumGemileri(1)
gemi8=CozumGemileri(1)
gemi1.yerlestir(ck)
gemi2.yerlestir(ck)
gemi3.yerlestir(ck)
gemi4.yerlestir(ck)
gemi5.yerlestir(ck)
gemi6.yerlestir(ck)
gemi7.yerlestir(ck)
gemi8.yerlestir(ck)
print("...AMIRAL BATTI OYUNUNA HOSGELDINIZ...")
print("""Bu tabloda:
- 2 adet 4 birimlik, 
- 2 adet 3 birimlik, 
- 2 adet 2 birimlik ve 
- 2 adet 1 birimlik gemiler yerlestirilmistir.
Gemilerin yerlerini dogru tahmin ettiginizde X ile gosterilecek.
Bulmak icin 15 caniniz var.Kolay gelsin.""")
baslangic_zamani = time()               #oyun baslama zamanini tutar

tablo = oyuncu1.tabloilk().copy()               #00 01 02 gibi numaralardan olusan listeyi copy
oyuncu1.gorunen(tablo)
hak = 2                                #oyunucunun 15 hakki var

while True:
    # oyuncunun hamlesi
    hamle = input(''' ~hamle yapmak icin tablodan bir sayi girin 
 ~cikis icin q ya basin:''')

    # hamle cikis istiyorsa cikis yapar
    if hamle == "q":
        break

    # tabloda zamanla "  " ve "X " olacak.isabet eden ya da etmeyen kutular.
    elif hamle == '  ' or hamle == "X ":
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.') #daha onceki secimlerden tekrar yaptirmiyor

    # tabloda olmayan sayi isaret veya yazi girilirse tekrar hamle istiyor
    elif hamle not in tablo:
        print('Tablodaki henuz acilmamis kutucuk numaralarindan secim yapiniz.')
        oyuncu1.gorunen(tablo)
    #oyuncu tabloda acilmamis kutulardan tercih yaptiginda hamle yapiyor

    else:
        #hamle cozum icinde varsa
        if hamle in ck:
            konum = int(hamle)   #kutucuk numaralari ayni zamanda indexlerdir
            tablo[konum] = 'X '  #tabloda index yardimiyla hamle yapilan kutucugun dolu oldugunu X ile gosteriyor
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)                        #1 sn tabloyu kontrol ediyormus gibi dusunup bekletiyor
            print("gemimin bir parcsini vurdun.")
            oyuncu1.gorunen(tablo)                  #tabloyu yeni haliyle ekrana basiyor


            # toplam 20 tane gemi parcasi var.eger 20 si de bulunursa oyuncu oyunu kazandi
            if tablo.count('X ') == 20:
                print("...TEBRIKLER...".center(20))
                print("oyunu kazandiniz".center(20))
                break

        # sartlari saglayan hamle yapildi.fakat cozum listesinde olmayan kutu secildi
        else:
            konum = int(hamle)  # tablodaki index bulunur
            tablo[konum] = '  '  # tabloda boslik ile gosterilir
            print(f'{hamle} kutusunda gemi parcasi varmi bir bakayim...')
            sleep(1)  # 1 sn tabloyu kontrol ediyormus gibi dusunup bekletiyor
            print("gemilerim hala guvende.Iskaladin")
            oyuncu1.gorunen(tablo)  # tabloyu yeni haliyle ekrana basiyor
            hak -= 1  # hakkindan bir tane dusuyor
            print(f'{hak} canin kaldi.')

            # 15 hakkin tamamini kullanmissa
            if hak == 0:
                print("..Oyun Bitti..")
                print("Hic canin kalmadi")
                print("iste aradiginiz cozum:")
                oyuncu1.gorunen(oyuncu1.cozumtablosu(ck))  # cozum tablosunu ekrana printler

                break

bitirme_zamani = time()
print(f"{baslangic_zamani - bitirme_zamani} sn de oyun tamamladiniz.")

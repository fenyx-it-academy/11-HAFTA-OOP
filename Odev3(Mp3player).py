#Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun.
#Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal,
#onceki parcayi cal, karisik cal ozelliklerini ekleyin.

class Muzikcalar():
    sarki_listesi=[]

    def __init__(self,sarkilistesi):
        self.sarkilistesi = sarkilistesi

    def listeyi_sifirla(self):
        self.sarki_listesi.clear()
        print("Sarki listenizdeki tum sarkilar basariyla silinmistir.")

    def listeyi_goruntuleme(self):
        print("Sarki listesi:")
        for sira,sarki in enumerate(self.sarki_listesi,1):
            print('{}: {}'.format(sira,sarki))

    def sarki_ekle(self,sarki):
        self.sarki_listesi.append(sarki)
        print("'{}' adli parca sarki listenize eklenmistir".format(sarki))

    def sarki_sil(self,sarki):
        self.sarki_listesi.remove(sarki)
        print("'{}' adli parca sarki listenizden silinmistir.".format(sarki))

    def sonraki_parca(self):
        print("Sonraki parca caliniyor.")

    def onceki_parca(self):
        print("Onceki parca caliniyor.")

    def karisik_cal(self):
        print("Karisik cal modu etkinlestirildi.")
from time import sleep

print("""Mp3 Player'inizin aktif olmasi icin oncelikle bir 'Sarki listesi' olusturmaniz gerekmektedir.""")
dosyaisim=input("Lutfen bir sarki listesi ismi giriniz:")
dosyaisim=Muzikcalar("dosyaisim")
print("Lutfen bekleyin...")
sleep(2)
print("Sarki liste dosyasi basariyla olusturuldu.")
sleep(1)
while True:
    print("_____"*20)
    print("""<<<<<<<< Mp3 Player>>>>>>>>
    Ana Ekran Menusu:
    1: Sarki Listesini goruntuleme.
    2: Sarki ekleme.
    3: Sarki silme.
    4: Tum sarkilari silme.
    5: Sonraki sarkiyi oynat.
    6: Onceki sarkiyi oynat.
    7: Karisik oynat modunu etkinlestir.
    8: Cikis""")
    try:
        secim=int(input("Lutfen 'Ana Ekran Menusunden' bir secim yapiniz:"))
    except:
        print("Lutfen seciminizi kontrol ediniz!")
        sleep(3)
        continue
    if secim == 8:
        print("Mp3 player kapatiliyor...")
        sleep(3)
        break
    elif secim<1 or secim>8:
        print("Lutfen seciminizi kontrol ediniz!")
        sleep(3)
        continue
    elif secim == 1:
        sleep(2)
        if dosyaisim.sarki_listesi == []:
            print("Listenizde suan bir sarki bulunmuyor")
            continue
        else:
            dosyaisim.listeyi_goruntuleme()

    elif secim == 2:
        sleep(2)
        sarki_ismi=input("Lutfen bir sarki ismi giriniz:")
        dosyaisim.sarki_ekle(sarki_ismi)

    elif secim == 3:
        sleep(2)
        while True:
            dosyaisim.listeyi_goruntuleme()
            sarki_ismi = input("Lutfen silmek istediginiz sarkinin ismini giriniz.Iptal etmek icin 'I':").lower()
            if sarki_ismi =="i":
                print("Isleminiz iptal edildi!")
                break
            elif sarki_ismi not in dosyaisim.sarki_listesi:
                print("Bu sarki listenizde mevcut degildir!!!")
                continue
            else:
                dosyaisim.sarki_sil(sarki_ismi)
                break

    elif secim == 4:
        sleep(2)
        if dosyaisim.sarki_listesi == []:
            print("Listenizde suan bir sarki bulunmuyor")
            continue
        else:
            while True:
                soru=input("Dikkat!!! Listenizdeki tum sarkilar silinecek. Devam icin 'D', iptal icin 'I' basiniz:").lower()
                if soru == "d":
                    dosyaisim.listeyi_sifirla()
                    break
                elif soru == "i":
                    print("Isleminiz iptal edildi!")
                    break
                else:
                    print("Lutfen verilen seceneklerden birini seciniz:")
                    continue
    elif secim == 5:
        sleep(2)
        if dosyaisim.sarki_listesi == []:
            print("Suan listenizde sarki bulunmuyor!!! ")
            continue
        else:
            dosyaisim.sonraki_parca()

    elif secim == 6:
        sleep(2)
        if dosyaisim.sarki_listesi == []:
            print("Suan listenizde sarki bulunmuyor!!! ")
            continue
        else:
            dosyaisim.onceki_parca()

    elif secim == 7:
        sleep(2)
        dosyaisim.karisik_cal()

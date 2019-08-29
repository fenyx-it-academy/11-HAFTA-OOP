print('b.')
'''
Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun. 
Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, sarki silme, 
sonraki parcayi cal,onceki parcayi cal, karisik cal ozelliklerini ekleyin.
'''
import random as r
import time


class MuzukCalar:

    def __init__(self):

        self.sarki_listesi = {'1': 'a sarkisi', '2': 'b sarkisi', '3': 'c sarkisi'}

    def sarki_ekleme(self, sarki_no, sarki_adi):
        self.sarki_listesi[sarki_no] = sarki_adi

    def sarki_silme(self, sarki_no):
        self.sarki_listesi.pop(sarki_no)

    def sarki_listesi_goruntule(self):
        for i in self.sarki_listesi.items():
            print(*i)

    def sarki_cal(self):
        global sarki_no
        sarki_no = input('calmak istediginiz sarki numarasini giriniz')
        print(f'{self.sarki_listesi[sarki_no]} sarkisi caliniyor.......')

    def sarki_liste_sifirlama(self):
        self.sarki_listesi.clear()
        print('sarki listesi temizleniyor.....')

    def karisik_sarki_cal(self):
        sayi = str(
            r.randint(1, len(self.sarki_listesi)))  # randint ile 1 den sarki sayisi arasinda rastgele sarki secti
        print(f'{self.sarki_listesi[sayi]} caliniyor.......')

    def sonraki_sarkiyi_cal(self):
        global sarki_no
        print(f'sonraki sarki {self.sarki_listesi[str(int(sarki_no) + 1)]}  caliniyor.......')
        sarki_no = str((int(sarki_no) + 1) % len(self.sarki_listesi))  # mod alip basa dondurduk

    def onceki_sarkiyi_cal(self):
        global sarki_no
        sarki_no = str(int(sarki_no) - 1)  # sarki noyu bir azaltip onceki sarkiya gelmesini sagladik
        if int(sarki_no) == 0:  # sarki no sifir oluncada en sondaki sarkiya dondurduk
            sarki_no = str(len(self.sarki_listesi))
            print(f'onceki sarki {self.sarki_listesi[sarki_no]}  caliniyor.......')
        else:
            print(f'onceki sarki {self.sarki_listesi[sarki_no]}  caliniyor.......')


muzik_kutusu = MuzukCalar()


def giris():
    print('''
    1-sarki_ekleme
    2-sarki_silme
    3-sarki listesini goruntule
    4-sarki_cal
    5-karisik_sarki_cal
    6-sarki_liste_temizleme
    7-sonraki sarki
    8-onceki sarki cal

    >>>>...cikis icin bir tusa basiniz \n''')


while True:
    giris()
    cvp = input('tercih yapiniz....>>>')
    if cvp not in "1,2,3,4,5,6,7,8":
        print('lutfen menuden dogru degerleri giriniz')
    else:
        if cvp == '1':  # sarki_ekleme
            sarki_no = input('\nlutfen sarki no giriniz :')
            sarki_adi = input('lutfen sarki adini giriniz :')
            muzik_kutusu.sarki_ekleme(sarki_no, sarki_adi)

        elif cvp == '2':  # sarki silme
            sarki_no = int(input('lutfen silmek istediginiz sarki noyu giriniz :'))
            muzik_kutusu.sarki_silme(sarki_no)
        elif cvp == '3':  # listeyi goruntule
            muzik_kutusu.sarki_listesi_goruntule()
        elif cvp == '4':  # sarki cal
            muzik_kutusu.sarki_cal()
            time.sleep(5)
        elif cvp == '5':  # karisik cal
            muzik_kutusu.karisik_sarki_cal()
            time.sleep(5)
        elif cvp == '6':  # listeyi temizleme
            muzik_kutusu.sarki_liste_sifirlama()
            time.sleep(5)
        elif cvp == '7':  # sonraki sarki
            muzik_kutusu.sonraki_sarkiyi_cal()
            time.sleep(5)
        elif cvp == '8':  # onceki sarki
            muzik_kutusu.onceki_sarkiyi_cal()
            time.sleep(5)
        else:
            print('cikiliyor....bye')
            quit()

# Odev 3: Bir muzik calar objesi yapmanizi istiyoruz.
# Class attribute olarak bos bir sarki listesi olusturun.
# Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme,
# sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.


class muzikCalar():
    def __init__(self, sarkiListesi):
        self.sarkiListesi = sarkiListesi

    def listeyiSifirla(self):
        del self.sarkiListesi
        print('Sarki Listesi Sifirlandi..')
    def listeyiGoruntule(self):
        print('''    

        Sarki Listesi: {}

        '''.format(muzikCalarim.sarkiListesi))
        print('')
    def sarkiEkle(self, sarkiIsmi, sanatciIsmi):
        self.sarkiListesi.append([sanatciIsmi, sarkiIsmi])
        print('{} - {} adli sarki listeye eklendi...'.format(sanatciIsmi, sarkiIsmi))
    def sarkiSil(self, sarkiIsmi):
        isim = sarkiIsmi.lower()
        for i in self.sarkiListesi:
            if isim in i:
                self.sarkiListesi.remove(i)
                print('Rehberden Silindi...')
                break
            else:
                print('Rehberde boyle bir kayit bulunamadi!')
                break

    def sonrakiParca(self):
        print('Siradaki parca caliniyor..')
    def oncekiParca(self):
        print('Onceki parca caliniyor..')
    def karisikCal(self):
        print('Sarkilar karisik caliniyor.. ')

import random

muzikCalarim = muzikCalar([])


print('''
       Muzik Calar olusturuldu..

       Sarki Listesi: {}

       '''.format(muzikCalarim.sarkiListesi))
print('')

while True:
    print('*' * 30 + '\n\n' + 'Muzik Calar'.rjust(
        22) + '\n\n' + '1.Sarki Ekle\n' + '2.Sarki Sil\n' + '3.Listeyi Sifirla\n'
          + '4.Sonraki Parcayi Cal\n'+ '5.Onceki Parcayi Cal\n'+ '6.Karisik Cal\n'+ '7.Listeyi Goruntule\n' + 'Cikis icin "q" ya basin!\n\n' + '*' * 30 + '\n')

    islem = input('Lutfen yapmak istediginiz islemi secin:')

    if islem == '1':
        sarkiIsmi = input('Sarki Ismi Girin: ')
        sanatciIsmi = input('Sarkiyi soyleyen sanatci: ')

        muzikCalarim.sarkiEkle(sarkiIsmi,sanatciIsmi)

    elif islem == '2':
        isim = input('Silmek istediginiz ismi girin: ')
        muzikCalarim.sarkiSil(isim)
    elif islem == '3':
        isim = input('Aramak istediginiz ismi girin: ')
        muzikCalarim.listeyiSifirla(isim)
    elif islem == '4':
        muzikCalarim.sonrakiParca()
    elif islem == '5':
        muzikCalarim.oncekiParca()
    elif islem == '6':
        muzikCalarim.karisikCal()
    elif islem == '7':
        muzikCalarim.listeyiGoruntule()
    elif islem == 'q':
        print('Programdan cikiliyor...')
        break
    else:
        print('Gecersiz islem! tekrar deneyin..')
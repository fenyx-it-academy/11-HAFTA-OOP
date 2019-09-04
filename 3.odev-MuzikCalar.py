##Odev 3:
##Bir muzik calar objesi yapmanizi istiyoruz. Class attribute
##olarak bos bir sarki listesi  olusturun. Class methods olarak
##sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme,
##sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik
##cal ozelliklerini ekleyin.
import random
class MuzikCalar():
    liste = []
    def __init__(self,sanatci,sarki):
        self.sanatci = []
        self.sarki = []
    def liste_sifirlama(self):
        self.sarki.clear()
        print('Sarki listeniz sifirlandi')
    def liste_goruntule(self):
        print('Sarki Listesi:')
        for i in self.sarki:
            print(i)
    def sarki_ekle(self,sarkilar):
        self.sarki.append(sarkilar)
        print("{} isimli sarkiyi eklediniz.".format(self.sarki))
    def sarki_silme(self,sarkilar):
        self.sarki.remove(sarkilar) 
        print("{} isimli sarkiyi sildiniz.".format(sarkilar))
    def sarki_ac(self):
        sec=input("Listeden bir sarki seciniz: ")
        print("{} isimli sarki caliyor..".format(sec))
    def secimli_cal(self):
        sec=input("Sonraki sarki icin '1'e, onceki sarki icin '2'ye, karisik calmak icin '3'e basiniz")
        if sec == '1':
            print("{} caliyor..".format(self.sarki[0]))
        if sec == '2':
            print("{} caliyor..".format(self.sarki[0]))
        if sec == '3':
            sec1=random.choice(self.sarki)
            print('{} caliyor.'.format(sec1))           
sanatci1 = MuzikCalar('Orhan Hakalmaz','Leylim amman')
sanatci2 = MuzikCalar('Erkan Mutlu','Kabenin yollari')
sanatci3 = MuzikCalar('Baris Manco','Halilibrahim sofrasi')
sanatci4 = MuzikCalar('Cem Karaca','Allah yar')
sanatci1.sarki_ekle('Kara tren gecikir')
sanatci1.sarki_ekle('Turnalar')
sanatci1.sarki_ekle('Nazli yarim')
sanatci2.sarki_ekle('Bornovaya varamadim')
sanatci3.sarki_ekle('Gumus halhal')
sanatci1.sarki_silme('Kara tren gecikir')
print(sanatci1.sarki)
print(sanatci2.sarki)
print(sanatci3.sarki)
#print(MuzikCalar.liste_goruntule(sanatci2))
sanatci1.sarki_ac()
sanatci1.secimli_cal()
sanatci1.liste_sifirlama()
sanatci1.liste_goruntule()  
print(MuzikCalar.liste)

"""
Odev 3: Bir muzik calar objesi yapmanizi istiyoruz.
Class attribute olarak bos bir sarki listesi olusturun.
Class methods olarak sarki listesini sifirlama, listeyi goruntuleme,
sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.
"""
import random
class muzik_calar:
    sarki_listesi=[]
    def __init__(self):
        pass
    def sarki_calma(self,index_sarki):
        print("{} sarkisi caliniyor.".format(self.sarki_listesi[index_sarki]))
    def sifirlama(self):
        self.sarki_listesi.clear()
        print("sarki listesi temizlendi.")
    def goruntule(self):
        print(*self.sarki_listesi)
    def ekleme(self):
        while True:
            a=input("Eklemek istediginiz sarkiyi yaziniz:")
            self.sarki_listesi.append(a)
            self.goruntule()
            print("cikmak icin q ya basiniz:")
            if a=="q":
                break
    def silme(self):
        a = input("silmek istediginiz sarkiyi yaziniz:")
        self.sarki_listesi.remove(a)
    def sonraki(self,calan_sarki):
        self.sarki_calma( self.sarki_listesi.index(calan_sarki)+1)
    def onceki(self,calan_sarki):
        self.sarki_calma( self.sarki_listesi.index(calan_sarki)-1)
    def karisik(self):
         self.sarki_calma(random.randint(len(self.sarki_listesi)))




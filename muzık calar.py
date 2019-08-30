##Odev 3: Bir muzik calar objesi yapmanizi istiyoruz.
##Instance(Object) attribute olarak bos bir sarki listesi olusturun.
##Class methods olarak sarki listesini sifirlama,
##listeyi goruntuleme,
##sarki ekleme,
##sarki silme,
##sonraki parcayi cal,
##onceki parcayi cal,
##karisik cal ozelliklerini ekleyin.
import time
import random
class muzik_calar():
    sarki_listesi=[]
    def __init__(self, calansarki):
        self.calansarki=calansarki
    def goruntule(self):
        print(*self.sarki_listesi)
    def calan_sarki(self,calansarki):
        if calansarki in self.sarki_listesi:
            print(calansarki,"sarkisi caliyor..")
        else:
            print("bole sarki yok")
        
    def sarki_ekleme(self):
        sarki=input("kaydetmek istediginiz sarkiyi yaziniz:")
        print(sarki,"kardedildi..")
        self.sarki_listesi.append(sarki)
        time.sleep(2)
        
    def sarki_silme(self):
        sil=input("silmek istediginiz sarkinin adini giriniz:")
        self.sarki_listesi.remove(sil)
        print(sil,"sarki silindi..")
        time.sleep(2)
        
    def sifirlama(self):
        self.sarki_listesi.clear()
        print("sarki listesi bos...")
        time.sleep(2)
    def karisik_cal(self):
        karisik=random.randint(0,len(self.sarki_listesi)-1)
        print(self.sarki_listesi[karisik], "Caliniyor..")
        time.sleep(2)
    def onceki_sarki(self):
        print("onceki parca caliyor..")
        self.a=1
        self.calan_sarki=self.sarki_listesi[self.a]
        print(self.calan_sarki)
        time.sleep(2)
        
    def sonraki_sarki(self):
        print("sonraki parca caliyor..")
        self.b=1
        self.calan_sarki=self.sarki_listesi[self.b]
        print(self.calan_sarki)
        time.sleep(2)
        
        time.sleep(2)
        
muzigim=muzik_calar([])
print("muzik calari goruntulemek icin 1'e basiniz\nsarki eklemek icin 2'e basiniz\sarki silmek icin 3'e basiniz\nkarisik calmak icin 4'e basiniz\nonceki parcayi calmak icin 5'e basiniz\nsonraki parcayi calmak icin 6'ya basiniz\nlisteyi temizlemek icin 7'e basiniz\ncikmak icin 8'a basiniz")
        
        
while True:
    secim=input("seciminiz:")
    if secim == "1":
        muzigim.goruntule()
    elif secim == "2":
        muzigim.sarki_ekleme()
    elif secim =="3":
      muzigim.sarki_silme()
    elif secim == "4":
      muzigim.karisik_cal()
    elif secim == "5":
      muzigim.onceki_sarki()
    elif secim == "6":
      muzigim.sonraki_sarki()
      
    elif secim == "7":
      muzigim.sifirlama()
    elif secim == "8":
      print("cikiliyor..")
      break

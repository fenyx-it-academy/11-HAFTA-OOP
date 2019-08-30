'''Bir muzik calar objesi yapmanizi istiyoruz. Instance(Object) attribute olarak
bos bir sarki listesi olusturun. Class methods olarak sarki listesini sifirlama, listeyi goruntuleme,
sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.'''
import random
class Muzikcalar():
    sarkilar=["benzemez kimse sana","zeytin gozlum","donulmez aksamin ufkundayim","grenade","happy","without me"]

    def listeyi_sifirla(self):
        self.sarkilar.clear()
    def listeyi_goruntule(self):
        for i in self.sarkilar:
            print(i)
    def sarki_ekle(self,eklenecek_sarki):
        self.sarkilar.append(eklenecek_sarki)
    def sarki_silme(self,silinecek_sarki):
        for i in self.sarkilar:
            if silinecek_sarki==i:
                a=self.sarkilar.index(i)
                self.sarkilar.pop(a)
        else:
            print(silinecek_sarki,"listenizde mevcut degil.")
    def sonraki_parcayi_cal(self,sonraki_sarki):
        for i in self.sarkilar:
            if sonraki_sarki == i:
                a = self.sarkilar.index(i)
                print("Caliniyor...",self.sarkilar[a+1])
    def onceki_parcayi_cal(self,onceki_sarki):
        for i in self.sarkilar:
            if onceki_sarki == i:
                a = self.sarkilar.index(i)
                print("Caliniyor...", self.sarkilar[a - 1])
    def karisik_cal(self):
        karisik=random.choice(self.sarkilar)
        print("Caliniyor...",karisik)
calmalistesi=Muzikcalar()
while True:
    print("""
    ############################################
                  Muzik Calar                   
    _________________Menu_______________________
    1________:Listeyi sifirla___________________
    2________:Listeyi Goruntule_________________
    3________:Sarki Ekleme______________________
    4________:Sarki Silme_______________________
    5________:Sonraki Parca_____________________
    6________:Onceki Parca______________________
    7________:Karisik___________________________
    8________:Cikis_____________________________""")
    try:
        giris=int(input("Lutfen isleminizi 1-8 rakamlarini kullanarak seciniz:"))
        if giris==8:
            print("Sistemden Cikiliyor...")
            quit()
        elif not giris:
            print("lutfen bir giris yapiniz...")
            continue
        elif len(str(giris))>1:
            print("Lutfen 1-8 arasinda giris yapiniz...")
            continue
        if giris == 1:
            print("Liste sifirlaniyor...")
            calmalistesi.listeyi_sifirla()
            print("Liste sifirlandi.")
        elif giris==2:
            print('Listeniz:')
            calmalistesi.listeyi_goruntule()
        elif giris==3:
            eklenecek_sarki=input("Eklemek istediginiz sarki adi:")
            calmalistesi.sarki_ekle(eklenecek_sarki)
        elif giris==4:
            silinecek_sarki=input("Silmek istediginiz sarki adi:")
            calmalistesi.sarki_silme(silinecek_sarki)
        elif giris==5:
            kalinan=input("kaldiginiz sarki:")
            calmalistesi.sonraki_parcayi_cal(kalinan)
        elif giris==6:
            kalinan=input("kaldiginiz sarki:")
            calmalistesi.onceki_parcayi_cal(kalinan)
        elif giris==7:
            print("Karisik moda geciliyor...")
            calmalistesi.karisik_cal()
    except ValueError:
        print("Hatali giris. Lutfen tekrar deneyiniz.")



#
# calmalistesi=Muzikcalar()
# calmalistesi.listeyi_goruntule()
# calmalistesi.sarki_ekle("Gangam style")
# calmalistesi.listeyi_goruntule()
# calmalistesi.sarki_silme("Gangam style")
# calmalistesi.listeyi_goruntule()
# calmalistesi.sonraki_parcayi_cal("donulmez aksamin ufkundayim")
# calmalistesi.karisik_cal()

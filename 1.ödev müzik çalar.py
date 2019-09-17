#Bir muzik calar objesi yapmanizi istiyoruz.
#Class attribute olarak bos bir sarki listesi olusturun.
#Class methods olarak sarki listesini sifirlama, listeyi goruntuleme,
#sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal,
#karisik cal ozelliklerini ekleyin.
import random

class müzikçalar:
    şarkı_listesi = ["cengiz-geceler","orhan-ziyankar","müslüm-usta","ferdi-derbeder"]
   

    def çal(self):
        self.şarkı = input("listeden şarkı seçiniz:")
        for i in self.şarkı_listesi:
            if i == self.şarkı:
                print(self.şarkı,"çalınıyor")
                break
            else:
                print("sadece listede olanları çalar")
                break

    def ekle(self):
        self.şarkı = input("sanatçı adı-şarkı adı giriniz:")
        self.şarkı_listesi.append(self.şarkı)
        print("şarkı listeye eklenmiştir...")

    def sil(self):
        self.şarkı = input("sanatçı adı-şarkı adı giriniz:")
        if self.şarkı in self.şarkı_listesi:
            self.şarkı_listesi.remove(self.şarkı)
            print("girmiş olduğunuz şarkı silinmiştir...")
        else:
            print("işleminiz hatalı...")

    def görüntüle(self):
        for i in self.şarkı_listesi:
            print(i)

    def karışık(self):
        a = random.choice(self.şarkı_listesi)
        print(a)

    def sıfırla(self):
        a = self.şarkı_listesi.clear()

    def ilerisar(self,sonraki):
        for i in self.şarkı_listesi:
            if sonraki == i:
                a = self.şarkı_listesi.index(i)
                print("Caliniyor...",self.şarkı_listesi[a+1])

    def gerisar(self,önceki):
        for i in self.şarkı_listesi:
            if önceki == i:
                a = self.şarkı_listesi.index(i)
                print("Caliniyor...", self.şarkı_listesi[a - 1])
        
            
müzik = müzikçalar()

while True:
    print("""
    *-*-*-*-*-*-*MENÜ *-*--*-*-*-*-*
    (1) çalmaya başla
    (2) listeye parça ekle
    (3) listeden parça sil
    (4) listeyi görüntüle
    (5) listeden karışık çal
    (6) listeyi sıfırla
    (7) önceki şarkı
    (8) sonraki şarkı
    (9) çıkış için q basınız...
    """)


    
    cevap=input("istediginiz islemi seciniz: ")
    if cevap=="1":
        müzik.çal()
    elif cevap=="2":
        müzik.ekle()
    elif cevap=="3":
        müzik.sil()
    elif cevap=="4":
        müzik.görüntüle()
    elif cevap == "5":
        müzik.karışık()
    elif cevap == "6":
        müzik.sıfırla()
    elif cevap == "7":
        müzik.ilerisar("orhan-ziyankar")
    elif cevap == "8":
        müzik.gerisar("orhan-ziyankar")
    elif cevap == "q":
        print("mazik çalardan çıkılıyor...")
    else:
        print("hatalı işlem...")
        break

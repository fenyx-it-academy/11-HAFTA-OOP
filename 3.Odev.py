
#Programi direk calistirip deneyebilirsiniz..


import time
import random


class muzikcalar():
    def __init__(self):
        self.sarki_listesi = ["HAluk Levent - Daglar","Baris MAnco - Kol dugmeleri","Ahmet Kaya - Agladikca"]
        self.x=0
        self.calinansarki = self.sarki_listesi[self.x]
        print("Muzikcalar Calistiriliyor..")
        time.sleep(3)
        print("Calinan Sarki : ",self.calinansarki)
        time.sleep(2)
    #bir sonraki ve bir onceki parcayi cal foksiyonunu yazmak icin
    #sarki listesinin ilk elemanini degiskene atamak zorunda kaldim self.x olarak.


    def liste_goruntuleme(self):
        print("Sarki Listesi Goruntuleniyor..")
        time.sleep(2)
        sayac = 0
        for i in self.sarki_listesi:
            sayac = sayac+1
            print("""
            
             {}.{}
            """.format(sayac,i))
        time.sleep(2)

# Sarkilarin yaninda sira numarlaarini da gostersin diye for ile cevrildi..


    def liste_sifirlama(self):
        print("Liste Sifirlaniyor..")
        time.sleep(2)
        self.sarki_listesi.clear()
        print("""Liste Sifirlandi! 
                Guncel Sarki Listesi 

                {} - Liste Bos..
                """.format(self.sarki_listesi))
        if not self.sarki_listesi:
            self.calinansarki=[]
        time.sleep(2)
    # Clear metodu kullanildi..sarki listesi sifirlandiktan sonra
    # mevcut calinan sarki da if kullanilarak sifirlandi.

    def sarki_ekleme(self,sarkiadi):
        print("Sarki Ekleniyor..")
        time.sleep(2)
        self.sarki_listesi.append(sarkiadi)
        self.calinansarki=self.sarki_listesi[0]
        print("Guncel Sarki Listesi")
        sayac = 0                     
        for i in self.sarki_listesi:
            sayac = sayac+1
            print("""                                                   
            {}.{}   
            """.format(sayac,i))


#append metodu kullanildi


    def sarki_silme(self,silineceksarki):
        print("Sectiginiz sarki siliniyor..")
        time.sleep(2)
        if silineceksarki==self.calinansarki:
            self.calinansarki=random.choice(self.sarki_listesi)
        self.sarki_listesi.remove(silineceksarki)
        sayac = 0
        print("Guncel Sarki Listesi")
        for i in self.sarki_listesi:
            sayac = sayac + 1
            print(""" 
                    {}.{}   
                    """.format(sayac, i))
        time.sleep(2)

# remove metodu ile belirlenen sarki silindi

    def sonrakiparcayical(self):
        print("Sonraki parca caliniyor..")

        if self.calinansarki==self.sarki_listesi[-1]:
            self.calinansarki=self.sarki_listesi[0]
        print(self.calinansarki)



    def oncekiparcayical(self):
        print("onceki parca caliniyor..")
        self.x-=1
        self.calinansarki = self.sarki_listesi[self.x]
        print(self.calinansarki)
        time.sleep(2)

    def karisikcal(self):
        print("Karisik caliniyor..")
        time.sleep(2)
        self.calinansarki = random.choice(self.sarki_listesi)
        print(self.calinansarki)


    def calinansarkigoruntuleme(self):
        print("Suanda Calinan Sarki : {}".format(self.calinansarki))
        time.sleep(2)


a = muzikcalar()

a.liste_goruntuleme()

a.liste_sifirlama()



a.sarki_ekleme("Ali guven - Yolcu")
a.sarki_ekleme("Sagopa KAjmer - Istisnalar Kaideyi Bozmaz")
a.sarki_ekleme("Sezen Aksu - Bir Cocuk Sevdim")
a.sarki_ekleme("Ibrahim Tatlises - Belalim")

a.sarki_silme("Ali guven - Yolcu")

a.calinansarkigoruntuleme()

a.oncekiparcayical()

a.sonrakiparcayical()

a.karisikcal()

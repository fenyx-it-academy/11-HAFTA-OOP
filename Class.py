#Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz. 
#Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
#Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin (class methods) olmasini istiyoruz.
import random

class ceptelefonu():
  
  def __init__(self,marka,model,uretim_yili,tel_no,rehber=[]):
    self.marka=marka
    self.model=model
    self.uretim_yili=uretim_yili
    self.tel_no=tel_no
    self.rehber=[]
  def rehber_ekle(self,ad,tel_no):
    self.rehber.append([ad,tel_no])
    print(ad,tel_no,"eklendi...")
  def rehber_sil(self,ad):
    for i in self.rehber:
      if i[0]==ad:
        self.rehber.pop(self.rehber.index(i))
        print(*i, "Silindi...")
      else:
        print("Boyle bir kisi yok..")
        
  def rehber_goruntule(self):
    for i in self.rehber:
      print(*i)
  def Ara(self,isim):
    for i in self.rehber:
      if i[0]==isim:
         print(i[1], " araniyor...")
      else:
        print("Boyle bir kisi yok..")

Nokia = ceptelefonu("Nokia","A101","1991","242 23 43")  
Samsung=ceptelefonu("Samsung","123","2010","345 34 34")
Nokia.rehber_ekle("Sehri","123 23 43")
Nokia.rehber_ekle("Nermin","123 23 43")
Nokia.rehber_ekle("Guldane","123 23 23")
Nokia.rehber_ekle("Merve","234 342 234")
Nokia.rehber_sil("Merve")
Nokia.rehber_goruntule()
Nokia.Ara("Sehri")




#Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun. Class methods olarak sarki listesini sifirlama,
#listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.
import time 
class Muzikcalar():
  sarkilistesi=[]
  def sarki_cal(self,sarki):
    if sarki in self.sarkilistesi:
      print(sarki,"Caliniyor...")
    else:
      print("Sarki listenizde boyle bir sarki ekli degil...")

  def sarkilistesi_sifirla(self):
    self.sarkilistesi.clear()
    print("\nSarki Listeniz Sifirlandi...")
  def sarkilistesi_goruntule(self):
    print("\nSarki Listesi\n")
    for i in self.sarkilistesi:
      print(i)
  def sarki_ekle(self,sarki):
    print("\n",sarki,"eklendi..")
    self.sarkilistesi.append(sarki)
  def sarki_sil(self,sarki):
    self.sarkilistesi.pop(self.sarkilistesi.index(sarki))
    print('\n',sarki,"silindi..")
  def sonrakisarki_cal(self,sarki):
    a=self.sarkilistesi.index(sarki)
    print("\nSonraki Sarki")
    print(self.sarkilistesi[a+1],"caliniyor...")
  def oncekisarki_cal(self,sarki):
    a=self.sarkilistesi.index(sarki)
    print("\nOnceki Sarki")
    print(self.sarkilistesi[a-1], "caliniyor...")
  def karisik_cal(self):
    karisik=random.randint(0,len(self.sarkilistesi)-1)
    print(self.sarkilistesi[karisik], "Caliniyor..")


mc1= Muzikcalar()
mc1.sarki_ekle("Baris Manco-Benden Ote Benden Ziyade")
mc1.sarki_ekle("Cem Karaca Of Be")
mc1.sarki_ekle("Ahmet Kaya Oyle Bir Yerdeyim ki")
mc1.sarki_ekle("Sezen Aksu Gecer")
mc1.sarkilistesi_goruntule()
mc1.sarki_sil("Sezen Aksu Gecer")
mc1.sonrakisarki_cal("Baris Manco-Benden Ote Benden Ziyade")
mc1.oncekisarki_cal("Ahmet Kaya Oyle Bir Yerdeyim ki")
mc1.karisik_cal()
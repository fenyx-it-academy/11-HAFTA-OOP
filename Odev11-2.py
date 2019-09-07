# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:37:53 2019

@author: HP
"""

# Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, uretim yili, tel nosu ve 
# rehber ozelliklerinin(class attributes) olmasini bekliyoruz. Ayrica bu objenin rehbere no ekleme, silme, 
# rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin 
# (class methods) olmasini istiyoruz
import time

class telefoon():
    
    rehber={}    # Sozluk
    def __init__(self,isim,marka,model,uretim_yili,tel_no):
        self.isim=isim
        self.marka=marka
        self.model=model
        self.uretim_yili=uretim_yili
        self.tel_no=tel_no
        #self.rehbere_isim_ve_no_ekle()
        
    def tel_sahibi(self):
        
        print("""
        Telefon Sahibinin:
                İsim :             {}
                Tel Markasi :      {}
                Tel Modeli:        {}
                Tel Uretim Yili :  {}
                Tel No :           {}
        """.format(self.isim,self.marka,self.model,self.uretim_yili,self.tel_no))
                
    def rehbere_isim_ve_no_ekle(self):    
        self.isim=input('Telefon rehberine isim ekleyiniz ;')
        self.tel_no=input('Eklenilen kisinin Telefon nosunu ekleyiniz ;')
        self.rehber.setdefault(self.isim,self.tel_no)
        print('{} adlı kişinin numarasi {} da rehbere eklendi'.format(self.isim,self.tel_no))
        
    def rehberden_kisi_sil(self):
        self.isim=input('Rehberden kisi siliniz,isim ;')
        self.rehber.pop(self.isim)
        print('{} adlı kişi rehberden silindi'.format(self.isim))
        
    def rehber_goruntuleme(self):
        count=1
        for self.isim in self.rehber:
            print(f'{count}. {self.isim} kisinin numarasi {self.rehber[self.isim]}')
            count+=1        
        
    def aramayap(self):
        self.isim=input("Aranmasi istenilen kisinin ismini giriniz ;")
        print(self.isim,'araniyor...')
    
    def temizle(self):
        self.rehber.clear()
        print('Rehber fabrika ayarlarina donuyor...')
    
kisi1=telefoon('Aydin','Nokia','Sj3',2000,'0687654231')
print(kisi1.tel_sahibi())
kisi2=telefoon('Aydin','LG','G3',2005,'0987654321')

while True:
    print("""\nRehber de yapmak istediginiz islemlere :
        Telefon Sahibinin Bilgileri icin 1 tusuna
        rehberi goruntulemek icin 2 tusuna
        rehbere kisi eklemek icin 3 tusuna
        reherden kisi silmek icin 4 tusuna
        rehberden arama yapmak icin 5 tusuna
        rehberi tamamen temizlemek icin 6 tusuna 
        ve cimak icin 0 tusuna basarak ulasabilirsiniz...:""")

    cevap=input("istediginiz islemi seciniz: ")
    if cevap=="1":
        kisi1.tel_sahibi()
    elif cevap=='2':
        kisi2.rehber_goruntuleme()
    elif cevap=="3":
        kisi2.rehbere_isim_ve_no_ekle()
    elif cevap=="4":
        kisi2.rehberden_kisi_sil()
    elif cevap=="5":
        kisi2.aramayap()
    elif cevap=='6':
        kisi2.temizle()
    elif cevap=="0":
        print("Cikiliyor...")
        break
    time.sleep(3)
    


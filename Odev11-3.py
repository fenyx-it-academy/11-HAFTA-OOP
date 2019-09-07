# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:38:10 2019

@author: HP
"""

# Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun. 
# Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal,
# onceki parcayi cal, karisik cal ozelliklerini ekleyin.
import random
import time

class liedje():
    sarki='Yalan Dunya'
    sarkilist=[]    
    
    def __init__(self,sarki):
        self.sarki=sarki
        self.ekle()
                
    def ekle(self):
        self.sarkilist.append(self.sarki)
        print('Listeye Sarki ekleniyor...')
        time.sleep(3)
        print('{} adlı sarki eklendi'.format(self.sarki))
        
    def sil(self,sarki):
        self.sarkilist.remove(self.sarki)
        print('Listeden sarki siliniyor...')
        
    def liste_goruntule(self):
        print("Listedeki sarkilari goruntuleniyor...")
        count=1
        for sarki in self.sarkilist:
            print(count,'.',sarki)
            count+=1
    def play(self):
        global x
        x=int(input('Calinmasini istediginiz sarki numarasini giriniz ;'))-1
        print(f'{self.sarkilist[x]} sarkisi caliniyor...')
        
       
    def sonraki_cal(self):
        global y
#        y=self.sarkilist[x]
        sonra=self.sarkilist[x+1]
        print(f'Sonraki sarki caliniyor ; {sonra}')
        
    def onceki_cal(self):
#        x=self.sarkilist.index
        eski=self.sarkilist[x-1]
        print(f'Onceki sarki caliniyor ;{eski}')
        
    def karisik_cal(self):
        lied=random.choice(self.sarkilist)
        print('Karisik caliyor...sarki;',lied)
        
    def sifirla(self):
        self.sarkilist.clear()
        
s1=liedje('Nane limon kabugu')
s2=liedje('Istanbul')
s3=liedje('Aynalar')
s1=liedje('MayaDag')

print("""\nCD calarda yapmak istediginiz islemlere :
sarki listesini gormek icin 1 tusuna
CD ye sarki eklemek icin 2 tusuna
CD den sarki silmek icin 3 tusuna
CD den sarki calmak icin 4 tusuna
ardindan bir sonraki sarkiyi calmak icin 5 tusuna
ardindan bir onceki sarkiyi calmak icin 6 tusuna
karisik sarki calmak icin 7 tusuna 
sarki listesini temizlemek icin 8 tusuna
ve cimak icin 0 tusuna basarak ulasabilirsiniz...:""")

while True:
    cevap=input("istediginiz islemi seciniz: ")
    if cevap=="1":
        s2.liste_goruntule()
    elif cevap=="2":
        sarki=input('Sarki ismi giriniz ;')
        s5=liedje(sarki)
    elif cevap=="3":
        sarki=input('Sarki ismi giriniz ;')
        s1.sil(sarki)
    elif cevap=="4":
        s3.play()
    elif cevap=="5":
        s3.sonraki_cal()
    elif cevap=="6":
        s3.onceki_cal()
    elif cevap=="7":
        s3.karisik_cal()
    elif cevap=="8":
        s3.sifirla()
    elif cevap=="0":
        print("Cikiliyor...")
        break


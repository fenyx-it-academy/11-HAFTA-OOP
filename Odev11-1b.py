# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:43:37 2019

@author: HP
"""

# Odev 1: Gecen hafta basladigimiz amiral batti oyununu gelistirecegiz. Bu hafta kodunuzu Object Oriented sekline 
# cevirmenizi istiyoruz. Ayrica randomsuz yapanlarin random gemi yerlestirme ozelligini eklemelerini bekliyoruz. 
#Bonus ozellik olarak oyunun bilgisayara karsi oynanan iki kisilik versiyonunu yapabilirsiniz.

# Bonus kismi ile.... Bilgisayar karsi kisi!
import random
import time

class Amiir():
    vurulduP=0
    vurulduC=0
    hataP=0
    hataC=0
    def __init__(cls):
        cls.tablogizliC=[]
        cls.tablogizliP=[] 
      
    @classmethod          
    def kisioyunu(cls):    
        
        print("Lutfen vurmak istediginiz noktanin satir ve sutununu yaziniz ;")
        x=int(input("Satir ;"))-1
        y=int(input("Sutun ;"))-1
        
        if cls.tablogizliC[x][y]=='G':  # Geminin basi-govde-kuyruk varsa vurur
            cls.vurulduC +=1
            print("\n")
            print(f'\tHedef vuruldu! Simdilik kisi isabet orani {cls.vurulduC} / 20')
            tablogorC[x][y]='X' ; cls.tablogizliC[x][y]='X'
            for i in range(10):   
                print('\t',*[tablogorC[i][j] for j in range(10)])
            print('\n'*2)
            if cls.vurulduC==20:
                print("\tTebrikler! Tum gemiler batti...")
            
        elif cls.tablogizliC[x][y]=='X' or cls.tablogizliC[x][y]=='K':
            print("\tDaha once vurulmustu ; Tekrar deneyiniz!")
            for i in range(10):
                print('\t',*[tablogorC[i][j] for j in range(10)])
            print('\n'*2)
            
        elif cls.tablogizliC[x][y]=='O':
            cls.tablogizliC[x][y]='K'
            tablogorC[x][y]='K'
            print("\t Karavana!")
            cls.hataP+=1
            print('\t',15-cls.hataP,"atis hakkiniz kaldi")
            for i in range(10):   
                print('\t',*[tablogorC[i][j] for j in range(10)])
            print('\n'*2)
            time.sleep(3)
        return cls.hataP  

         
    @classmethod                    
    def compoyunu(cls):
        x = random.randint(0,9)
        y = random.randint(0,9)   
        print(x,y)
        print("Bilgisayar oynuyor , lutfen bekleyiniz...")
        time.sleep(2)
        
        if cls.tablogizliP[x][y]=='G':  # Geminin basi-govde-kuyruk varsa vurur
            cls.vurulduP +=1
            print("\n")
            print(f'\tHedef vuruldu! Simdilik bilgisayar isabet orani {cls.vurulduP}/ 20')
            tablogorP[x][y]='X' ; cls.tablogizliP[x][y]='X'
            for i in range(10):   
                print('\t',*[tablogorP[i][j] for j in range(10)])
            print('\n'*2)
            if cls.vurulduP==20:
                print("\tTebrikler! Tum gemiler batti...")
            
        elif cls.tablogizliP[x][y]=='X' or cls.tablogizliP[x][y]=='K':
            pass
            
        elif cls.tablogizliP[x][y]=='O':
            cls.tablogizliP[x][y]='K'
            tablogorP[x][y]='K'
            print("\t Karavana!")
            cls.hataC+=1
            print('\t',15-cls.hataC,"atis hakkiniz kaldi")
            for i in range(10):   
                print('\t',*[tablogorP[i][j] for j in range(10)])
            print('\n'*2)
            time.sleep(3)
        return cls.hataC 

     
    @classmethod
    def persongemiler(cls):   # 8 farkli gemiyi random yerlestiren fonksiyon
        global a,b
        cls.tablogizliP=[['O' for x in range(10)] for y in range(10)]
        a=random.randrange(0,4) 
        cls.tablogizliP[a][a]='G' ; cls.tablogizliP[a+3][a+5]='G'
        cls.tablogizliP[a+4][a+4:a+6]='G','G' ; cls.tablogizliP[a+6][a+1:a+3]='G','G'
        cls.tablogizliP[a+1][a+1:a+4]='G','G','G' ; cls.tablogizliP[a+5][a:a+3]='G','G','G'
        cls.tablogizliP[a][a+2:a+6]='G','G','G','G' ; cls.tablogizliP[a+2][a:a+4]='G','G','G','G'
        return cls.tablogizliP
    @classmethod
    def compgemiler(cls):
        cls.tablogizliC=[['O' for x in range(10)] for y in range(10)]
        b=random.randrange(0,4) 
        cls.tablogizliC[b][b+1]='G' ; cls.tablogizliC[b+3][b+5]='G'
        cls.tablogizliC[b+4][b+4:b+6]='G','G' ; cls.tablogizliC[b+6][b+1:b+3]='G','G'
        cls.tablogizliC[b+1][b+1:b+4]='G','G','G' ; cls.tablogizliC[b+5][b:b+3]='G','G','G'
        cls.tablogizliC[b][b+2:b+6]='G','G','G','G' ; cls.tablogizliC[b+2][b:b+4]='G','G','G','G'
        
        
        return cls.tablogizliC
#=========================================================================================================
        
    

while True:   # Oyunu pynatir ya da cikis yapar
    doorgaan=input("Oyundan tamamen cikmak icin 'q' ya basiniz, Amiral Batti oyunu oynamak icin 'enter' e basiniz ;")
    print("\n"*2)
    if doorgaan=='q':
        print("Cikiliyor...")
        break
    else:
        print("\tAMIRAL BATTI oyunu basliyor...\n")
        print("""2 adet 4 birimlik, 2 adet 3 birimlik, 2 adet 2 birimlik ve 2 adet 1 birimlik (uzunlugunda)
gemilerin batirilmasi icin karavana/bosa hamle sayiniz 15dir,Lutfen dikkatli olun! Buyurun; \n""")
        print("Deniz de yuzen 8 gemi vardir...")
        for x in range(10):
            print('\t',*['O' for y in range(10)]) 
        print('\n'*2) 
        
        tablogorC=[['O' for x in range(10)] for y in range(10)]
        Amiir.compgemiler()
        
        tablogorP=[['O' for x in range(10)] for y in range(10)]
        Amiir.persongemiler()
        
        sayi=0 ; hataP=0 ; hataC=0
        while hataP<15 or hataC<15:
            cikis=input("Bu oyundan cikmak icin q ya, devam etmek icin enter a basiniz ;")
            if cikis=='q':
                break
            sayi+=1
            if sayi%2==0:
                Amiir.kisioyunu()
            elif sayi%2==1:
                Amiir.compoyunu()
              
                
                
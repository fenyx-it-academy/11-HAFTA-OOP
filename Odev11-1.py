# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 04:41:14 2019

@author: HP
"""
# Odev 1: Gecen hafta basladigimiz amiral batti oyununu gelistirecegiz. Bu hafta kodunuzu Object Oriented sekline 
# cevirmenizi istiyoruz. Ayrica randomsuz yapanlarin random gemi yerlestirme ozelligini eklemelerini bekliyoruz. 

# OOP seklinde hazirlandi, Random gemi secer ancak bilgisayara karsi oynama yok
import random
import time


class Amiir():
    
    
    def __init__(self):
        self.oyun()
        self.gemiler()
        self.tablogizli=[]
        
    @classmethod        
    def oyun(self):    # Oyun Fonksiyonu 
        hata=0  ; vuruldu=0  
        while hata<15:   # Max bosa 15 atis, veriler girilir satir-sutun olarak
            try :
                cik=input("Cikmak icin 'q' ya basiniz, devam etmek icin emter a basiniz ;")
                if cik=='q':
                    break
                
                print("Lutfen vurmak istediginiz noktanin satir ve sutununu yaziniz ;")
                x=int(input("Satir ;"))-1
                y=int(input("Sutun ;"))-1
                if self.tablogizli[x][y]=='G':  # Geminin basi-govde-kuyruk varsa vurur
                    vuruldu +=1
                    print("\n")
                    print(f'\tHedef vuruldu! Simdilik isabet orani {vuruldu}/ 20')
                    tablogor[x][y]='X' ; self.tablogizli[x][y]='X'
                    for i in range(10):   
                        print('\t',*[tablogor[i][j] for j in range(10)])
                    print('\n'*2)
                    if vuruldu==20:
                        print("\tTebrikler! Tum gemiler batti...")
                        break
                elif self.tablogizli[x][y]=='X' or self.tablogizli[x][y]=='K':
                    print("\tDaha once vurulmustu ; Tekrar deneyiniz!")
                    for i in range(10):
                        print('\t',*[tablogor[i][j] for j in range(10)])
                    print('\n'*2)
                elif self.tablogizli[x][y]=='O':
                    self.tablogizli[x][y]='K'
                    tablogor[x][y]='K'
                    print("\t Karavana!")
                    hata+=1
                    print('\t',15-hata,"atis hakkiniz kaldi")
                    for i in range(10):   
                        print('\t',*[tablogor[i][j] for j in range(10)])
                    print('\n'*2)
                    time.sleep(5)
            except :
                print("Hatali giris, tekrar deneyin!")
        
    @classmethod
    def gemiler(self):   # 8 farkli gemiyi random yerlestiren fonksiyon
        global a 
        self.tablogizli=[['O' for x in range(10)] for y in range(10)]
        a=random.randrange(0,4) 
        self.tablogizli[a][a]='G' ; self.tablogizli[a+3][a+5]='G'
        self.tablogizli[a+4][a+4:a+6]='G','G' ; self.tablogizli[a+6][a+1:a+3]='G','G'
        self.tablogizli[a+1][a+1:a+4]='G','G','G' ; self.tablogizli[a+5][a:a+3]='G','G','G'
        self.tablogizli[a][a+2:a+6]='G','G','G','G' ; self.tablogizli[a+2][a:a+4]='G','G','G','G'
        return self.tablogizli
#=========================================================================================================
        
 # Oyuncuya oyunu oynatma bolumu...    

while True:   # Oyunu pynatir ya da cikis yapar
    doorgaan=input("Oyundan cikmak icin 'q' ya basiniz, Amiral Batti oyunu oynamak icin 'enter' e basiniz ;")
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
        tablogor=[['O' for x in range(10)] for y in range(10)]
        Amiir.gemiler()
#        for i in range(10):
#            print('\t',*[tablogizli[i][j] for j in range(10)])
        Amiir.oyun()




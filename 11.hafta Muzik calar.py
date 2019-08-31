##Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute
##olarak bos bir sarki 
##listesi olusturun. Class methods olarak sarki listesini sifirlama,
##listeyi goruntuleme, 
##sarki ekleme, sarki silme, sonraki parcayi cal, onceki parcayi cal,
##karisik cal ozelliklerini ekleyin.

class MuzikCalar():     #Muzikcalar icin class olusturyoruz
    
    def __init__(self,muzikcalar_durum,sarki,liste=[]):# Bu class icinde metodlar gelistirelim
        self.liste=liste
        self.muzikcalar_durum=muzikcalar_durum
        self.sarki=sarki
        
    def mc_ac(self):
        if self.muzikcalar_durum=="Acik":           #Muzikcalarin acilip kapanmasi
            print("Muzikcalar zaten acik...")
        else:
            print("Muzikcalar aciliyor...")
            self.muzikcalar_durum="Acik"
    def mc_kapat(self):
        if self.muzikcalar_durum=="Kapali":
            print("Muzikcalar zaten kapali...")
        else:
            print("Muzikcalar kapatiliyor...")
            self.muzikcalar_durum="Kapali"   
    def listeyigoster(self):                    #Muzik Listessinin printlenmesi
        print("""
        Sarki Listesi: {}""".format(self.liste))
    def sarki_ekle(self,yeni_sarki):
        self.liste.append(yeni_sarki)           #Listeye sarki ekleme, cikarma islemleri
        print(yeni_sarki,"Listeye yeni sarki olarak eklendi...\n")
    def sarki_sil(self,sil_sarki):
        self.liste.pop(sil_sarki)
        print(sil_sarki,"Sarki listesinden silindi...")
    def liste_sil(self,liste):
        self.liste.clear(liste)
        print("Sarki Listesi bosaltilmistir.",liste)
    def sarki_cal(self,sarki):
        if sarki in self.liste:
            print(sarki,"sarkisi caliniyor...")
        else:
            print("Listede boyle bir sarki yoktur...")
    def sonrakini_cal(self,sarki):          #Listedeki sarkilarin calma sirasinin belirlenmesi
        sonraki=self.liste.index(sarki)
        print("Siradaki sarki: ",sonraki)
        print(self.liste[sarki+1],"caliniyor...")
    def oncekini_cal(self):
        onceki=self.liste.index(sarki)
        print("Bir onceki sarki: ",onceki)
        print(self.liste[sarki-1],"caliniyor...")
    def karisik_cal(self):
        rastgele=random.randint(0,len(self.liste)-1)
        self.sarki=self.liste(rastgele)
        print("Su anki sarki: ",self.sarki)
                     
muzik=MuzikCalar

print("""   MuzikCalar Programi
        
        Yapmak İstediginiz islemi seciniz:

        1. Sarki Listesini Goruntulemek

        2. Listeye Sarki Eklemek

        3. Listeden Sarki Silmek

        4. Listeyi Silmek

        5. Karisik Calmasini İstemek

        6. Muzik Calar'i Acmak

        7. Muzik Calar'i Kapatmak

        8. Cikis

        """)

while True:
    islem=int(input("Yapmak İstediginiz İslemi Seciniz: "))
    if 1>islem>8:
        print("Yanlis bir tusa bastiniz.Tekrar deneyiniz...")
        continue
    elif islem==8:
        print("Programdan cikiliyor...\n")
        break
    elif islem==1:
        muzik.listeyigoster()
    elif islem==2:
        yeni_sarki=input("Lutfen listeye eklemek istediginiz sarkiyi giriniz: ")
        muzik.sarki_ekle(yeni_sarki)
    elif islem==3:
        sil_sarki=input("Silmek istediginiz sarkiyi yaziniz: ")
        muzik.sarki_sil()
        print("Sarki basariyla listeden kaldirilmistir...")
    elif islem==4:
        muzik.liste.clear(liste)
    elif islem==5:
        muzik.karisik_cal()
    elif islem==6:
        muzik.mc_ac()
        
    elif islem==7:
        muzik.mc_kapat()
    else:
        print("Yanlis islem secimi yaptiniz... Tekrar deneyiniz...\n")
        continue
        




                    

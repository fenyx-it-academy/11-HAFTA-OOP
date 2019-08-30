import time
import random
class muzik():
    sarki_liste = []

    def __init__(self,sarki_isim,muzisyen):
        self.sarki_isim = sarki_isim
        self.muzisyen = muzisyen

    def sarki_ekle(self):
        self.sarki_liste.append(self)

    def sarki_goster(self):
        for i in range(len(self.sarki_liste)):
            print("\n{} ---> {} <----> {}".format(i+1,self.sarki_liste[i].muzisyen,self.sarki_liste[i].sarki_isim))

    def sarki_sil(self):
        self.sarki_goster()
        self.sira = int(input("\nLutfen silmek istediginiz sarkinin numarasini giriniz :"))
        if self.sira>len(self.sarki_liste) or self.sira<=0:
            print("Lutfen Sarki Numarasini Dogru giriniz ....")
            time.sleep(2)
        else:
            self.sira = self.sira - 1
            print("\n{} isimli parca siliniyor......\n".format(self.sarki_liste[self.sira].sarki_isim))
            del self.sarki_liste[self.sira]
            time.sleep(2)

    def sarki_cal(self):
        self.sira = int(input("\nLutfen calmak istediginiz sarkinin numarasini giriniz :"))
        if self.sira>len(self.sarki_liste) or self.sira<=0:
            print("Lutfen Sarki Numarasini Dogru giriniz ....")
            time.sleep(2)
            return False
        else:
            self.sira = self.sira - 1
            print("\n{} isimli parca oynatiliyor.......\n".format(self.sarki_liste[self.sira].sarki_isim))
            time.sleep(2)
            numara = self.sira
            return numara

    def sarki_sonraki(self,sira):
        if sira+1 >= len(self.sarki_liste):
            print("\n{} isimli parca oynatiliyor.......\n".format(self.sarki_liste[0].sarki_isim))
            sira = 0
            return sira
        else:
            print("\n{} isimli parca oynatiliyor.......\n".format(self.sarki_liste[sira+1].sarki_isim))

        return sira+1
        time.sleep(2)

    def sarki_onceki(self,sira):
        if sira-1 < 0 :
            sira = len(self.sarki_liste)
            print("\n{} isimli parca oynatiliyor.......\n".format(self.sarki_liste[sira - 1].sarki_isim))

        else:
            print("\n{} isimli parca oynatiliyor.......\n".format(self.sarki_liste[sira-1].sarki_isim))
        time.sleep(2)
        return sira-1

    def liste_sifirlama(self):
        self.sarki_liste.clear()
        print("\nSarki Listesi Bosaltilmistir........\n")
        time.sleep(2)

    def karisik_cal(self):
        self.secim = random.choice(self.sarki_liste)
        print("\n{} isimli parca oynatiliyor.......\n".format(self.secim.sarki_isim))
        time.sleep(2)

while True:
    menu = int(input("""\n Yy Muzik Calar 
    
    1- Liste Goruntuleme
    2- liste Temizleme
    3- Sarki Ekle
    4- Sarki Sil
    5- Listeden Sarki Oynat
    
    Lutfen Yapmak Istediginiz Islemin Numarasini Giriniz : """))

    if menu == 1:
        if muzik.sarki_liste==[]:
            print("\nSarki listenizde sarki bulunmamaktadir.....\n")
            time.sleep(2)
        else :
            sarki.sarki_goster()
    elif menu == 2:
        if muzik.sarki_liste==[]:
            print("\nSarki listeniz zaten bostur.....\n")
            time.sleep(2)
        else :
            sarki.liste_sifirlama()
            print("\nSarki listeniz bosaltilmistir....\n")
            time.sleep(1)
    elif menu == 3 :
        sarki_isim = input("Lutfen Sarki Ismi Giriniz :")
        muzisyen = input("Lutfen Muzisyen Ismi Giriniz :")
        sarki = muzik(sarki_isim,muzisyen)
        sarki.sarki_ekle()
    elif menu==4:
        if muzik.sarki_liste==[]:
            print("\nSarki listenizde sarki bulunmamaktadir.....\n")
            time.sleep(2)
        else :
            sarki.sarki_sil()

    if menu == 5 :
        if muzik.sarki_liste==[]:
            print("\nSarki listenizde sarki bulunmamaktadir.....\n")
            time.sleep(2)
        else :
            sarki.sarki_goster()
            numara = sarki.sarki_cal()

            while numara!=False:
                menu_calma = int(input("""" 1- Onceki Parca     2- Karisik Cal   3 - Sonraki Parca  4- Ana Menu
                 
                Yapmak istediginiz islem numarasini giriniz :"""))

                if menu_calma == 1:
                    sarki.sarki_goster()
                    numara = sarki.sarki_onceki(numara)

                elif menu_calma == 2:
                    sarki.karisik_cal()
                elif menu_calma == 3 :
                    sarki.sarki_goster()
                    numara = sarki.sarki_sonraki(numara)
                elif menu_calma == 4:
                    break







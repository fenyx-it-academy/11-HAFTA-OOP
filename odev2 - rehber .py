import time
class telefon():
    marka = ""
    model = ""
    uretim_yili = ""
    tel_no = ""
    liste = []
    def __init__(self,isim_soyisim,tel_1):
        self.isim_soyisim = isim_soyisim
        self.tel_1 = tel_1
    def kayit_ekle(self):
        self.liste.append(self)

    def goster(self):
        for i in range(len(self.liste)):
            print(i+1 , " --> ", self.liste[i].isim_soyisim, " " , self.liste[i].tel_1)
    def kayit_sil(self,sira):
        del self.liste[sira]

    def arama_yap(self,sira):
        print(self.liste[sira-1].isim_soyisim , " Araniyor ......")
        time.sleep(2)
        print("\n\n", self.liste[sira-1].tel_1 , " Nolu Numaraya Ulasilamadi ........\n\n")
        time.sleep(2)





while True:
    menu = int(input("""" REHBER PROGRAMI
    1- Kisi Ekle
    2- Kisi Sil
    3- Rehber Goruntule
    4- Arama Yap
    
     Lutfen bir menu numarasi giriniz :"""))
    if menu == 1:
        isim_soyisim = input("Isim giriniz :")
        tel_1 = input("Telefon Numarasi giriniz :")
        numara = telefon(isim_soyisim,tel_1)
        numara.kayit_ekle()

    elif menu==2:
        if telefon.liste == []:
            print("\nRehberinizde Kayit Bulunmamaktadir\n")
            time.sleep(2)
        else:
            numara.goster()
            sira = int(input("Lutfen silmek istediginiz kaydin sira numarasini giriniz : "))
            numara.kayit_sil(sira-1)

    elif menu == 3:
        if telefon.liste == []:
            print("\nRehberinizde Kayit Bulunmamaktadir\n")
            time.sleep(2)
        else:
            numara.goster()


    elif menu == 4:
        if telefon.liste == []:
            print("\nRehberinizde Kayit Bulunmamaktadir\n")
            time.sleep(2)
        else:
            numara.goster()
            sira = int(input("Lutfen arama yapmak istediginiz kaydin sira numarasini giriniz : "))
            numara.arama_yap(sira)
















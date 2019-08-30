''' Bir cep telefonu objesi yapmanizi istiyoruz.
Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini
bekliyoruz. Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen
bir noyu arama(gostermelik) gibi ozelliklerinin (class methods) olmasini istiyoruz.'''

class Cep_Telefonu():
    rehber={}
    def __init__(self,marka, model, uretim_yili, tel_no):
        self.marka=marka
        self.model=model
        self.uretim_yili=uretim_yili
        self.tel_no=tel_no
    def bilgileri_goster(self):
        print('''
        Cep Telefonunun ozellikleri
        marka         :{}
        model         :{}
        uretim yili   :{}
        tel no        :{}
        '''.format(self.marka,self.model,self.uretim_yili,self.tel_no))
    def numara_ekle(self):
        while True:
            ky=input("Isim:")
            val=input("Numara:")
            if ky.isnumeric()==False and val.isnumeric():
                print("Isim-Numara ekleniyor...")
                self.rehber[ky] = val
                pass
            else:
                print("Kisi veya numarayi yanlis girdiniz.\nLutfen tekrar giris yapiniz.")
                continue
            break
    def numara_sil(self):
        silinen=input("Silmek istediginiz kisiyi giriniz:")
        if silinen in self.rehber:
            print("Kisi-Numara siliniyor...")
            self.rehber.pop(silinen,"Lutfen mevcut bir numarayi sildiginizden emin olun")
        else:
            print("Kisi mevcut degil!")
    def rehberi_gor(self):
        print("Rehber Goruntuleniyor...")
        for k,v in self.rehber.items():
            print(str(k) + " : " + str(v) + "\n")
    def arama(self):
        aranacak=input("lutfen aramak istediginiz ismi giriniz:")
        if aranacak in self.rehber:
            print('{} kisisi araniyor...'.format(aranacak))
        else:
            print("Rehberde {} kisisi mevcut degil...".format(aranacak))

tel1=Cep_Telefonu('Samsung','J6+',2016,'+90505')


while True:
    print("Cep Telefonu Uygulamamiza Hos Geldiniz\n"
          "1)Cep Telefonunun Ozellikleri icin 1'i,\n"
          "2)Numara eklemek icin 2'yi,\n"
          "3)Numara silmek icin 3'u,\n"
          "4)Rehberi gormek icin 4'u,\n"
          "5)Arama Yapmak icin 5'i tuslayiniz.\n"
          "6)Cikmak icin 'q'ya basiniz...")
    secim = input("Seciminiz:")
    if not secim:
        continue
    elif len(secim) > 1:
        print("Seciminiz 1-5 araliginda olmali.\nCikmak icin 'q'ya basiniz.")
        continue
    if secim == 'q' or secim == 'Q':
        print("Sistemden Cikiliyor...")
        quit()
    elif int(secim) == 1:
        Cep_Telefonu.bilgileri_goster(tel1)
    elif int(secim) == 2:
        tel1.numara_ekle()
    elif int(secim) == 3:
        tel1.numara_sil()
    elif int(secim) == 4:
        tel1.rehberi_gor()
    elif int(secim) == 5:
        tel1.arama()
    else:
        print("Hatali giris yaptiniz!!!")











"""Odev 2:
Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin (class methods) olmasini istiyoruz.
"""
class Cep_Telefonu():
    def __init__(self,marka,model,uretim_yili,tel_no,tel_rehberi):
        self.marka = marka
        self.model = model
        self.ureim_yili = uretim_yili
        self.tel_no = tel_no
        self.tel_rehberi = tel_rehberi

    def rehber_goruntuleme(self):
        print("rehber bilgisi: marka: {} \nmodel: {} \nuretim yili: {} \ntelefon no: {} \ntelefon numaralari: {}".format(self.marka,self.model,self.ureim_yili,self.tel_no,self.tel_rehberi))
    def numara_ekleme(self):
        try:
            eklenecek_no  = int(input("eklemek istediginiz numarayi giriniz:"))
            print("Numara eklendi")
            self.tel_rehberi.append(eklenecek_no)
        except:
            print("hatali giris")
    def numara_silme(self):
        try:
            silinecek = int(input("silinecek numarayi giriniz"))
            if silinecek in self.tel_rehberi:
                self.tel_rehberi.remove(silinecek)
                print("Numara silindi")
            else:
                print("boyle bir numara yok")
        except:
            print("hatali giris")
    def no_arama(self):
        try:
            aranacak_no = int(input("araamak sitediginiz numarayi girin"))
            if aranacak_no in self.tel_rehberi:
                print("{} numarasi araniyor....".format(aranacak_no))
            else:
                print("numara bulunamadi")
        except:
            print("hatali giris")

ceptelefonu = Cep_Telefonu("samsung","galaxy A10",2019,4274563,[23456247])


while True:
    print("""
             ##############################################
             secnekeler:
             (1) rehber_goruntuleme(self)
             (2) numara_ekleme(self,eklenilen_no)
             (3) numara_silme(self)
             (4) no_arama(self)
             ##############################################
             """)

    try:

         islem =  int(input("yapmak istediginiz islemi seciniz: "))


         if islem == 1:
             ceptelefonu.rehber_goruntuleme()

         elif islem == 2:
             ceptelefonu.numara_ekleme()

         elif islem == 3:
             ceptelefonu.numara_silme()

         elif islem == 4:
             ceptelefonu.no_arama()
         else:
             print("lutfen gecerli bir giris yapiniz: ")
    except:
        print("hatali giris")




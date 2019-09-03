#Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
#Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
#Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik)
# gibi ozelliklerinin (class methods) olmasini istiyoruz.

class CepTelefonu:

    # class attributes, instance dan ayirmak icin herbirinin basinda c harfi var
    cmarka = ""
    cmodel = ""
    curetim_yili = 2010
    __crehber = [] # disaridan erisim olmamasi icin gizlendi

    # instance icin
    def __init__(self, marka, model, uretim_yili, tel_no):
        self.marka = marka
        self.model = model
        self.uretim_yili = uretim_yili
        self.tel_no = tel_no
        self.rehber = []

    def rehber_ekle(self, ad, tel_no):
        self.rehber.append([ad, tel_no])
        print(ad, tel_no, "eklendi...")

    def rehber_sil(self, ad):
        for kayit in self.rehber:
            if kayit[0] == ad:
                self.rehber.pop(self.rehber.index(kayit))
                print(*kayit, "Silindi...")
                return
        print("Boyle bir kisi yok..")

    def rehber_goruntule(self):
        for kayit in self.rehber:
            print(*kayit)

    def arama_yap(self, ad):
        for kayit in self.rehber:
            if kayit[0] == ad:
                print(kayit[1], " araniyor...")
                return
        print("Boyle bir kisi yok..")

    #class methods
    @classmethod
    def crehber_ekle(cls, ad, tel_no):
        cls.__crehber.append([ad, tel_no])
        print(ad, tel_no, "eklendi...")

    @classmethod
    def crehber_sil(cls, ad):
        for kayit in cls.__crehber:
            if kayit[0] == ad:
                cls.__crehber.pop(cls.__crehber.index(kayit))
                print(*kayit, "Silindi...")
                return
        print("Boyle bir kisi yok..")

    @classmethod
    def crehber_goruntule(cls):
        for kayit in cls.__crehber:
            print(*kayit)

    @classmethod
    def carama_yap(cls, ad):
        for kayit in cls.__crehber:
            if kayit[0] == ad:
                print(kayit[1], " araniyor...")
                return
        print("Boyle bir kisi yok..")

#instance ornek
Nokia = CepTelefonu("Iphone", "S6", "2015", "212 81 87")
Samsung = CepTelefonu("Samsung", "S7", "2016", "218 453 22 13")
Nokia.rehber_ekle("Tuba", "232 34 35")
Nokia.rehber_ekle("Kubra", "123 45 67")
Nokia.rehber_ekle("Sernur", "123 45 67")
Nokia.rehber_ekle("Asli", "345 32 34")
Nokia.rehber_sil("Asli")
Nokia.rehber_goruntule()
Nokia.arama_yap("Kubra")

Samsung.arama_yap("Kubra")

#class ornek
CepTelefonu.cmarka = "BlackBerry"
CepTelefonu.cmodel = "B2"
CepTelefonu.curetim_yili = 2018
CepTelefonu.crehber_ekle("Annem", "123 456 78")
CepTelefonu.crehber_ekle("Babam", "321 456 78")
CepTelefonu.crehber_ekle("Kardesim", "213 456 78")
CepTelefonu.crehber_sil("Kardesim")
CepTelefonu.crehber_goruntule()
CepTelefonu.carama_yap("Annem")




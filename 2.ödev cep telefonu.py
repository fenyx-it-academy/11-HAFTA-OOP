#Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, uretim yili,
#tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
#Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme,
#rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin
#(class methods) olmasini istiyoruz.
class mobil:
    marka = "samsung"
    model = "a3"
    üretim_yılı = "2016"
    tel_numarası = "0613266479"
    rehber = ["1234","1235","1236"]

    
    def ekle(self):
        self.numara = input("eklemek istediğiniz numarayı giriniz:")
        self.rehber.append(self.numara)
        print("numara listeye eklenmiştir")
           
    def sil(self):
        self.numara = input("silmek istediğiniz numarayı giriniz:")
        self.rehber.remove(self.numara)
        print("numara listeden silinmiştir")

    def görüntüle(self):
        for i in self.rehber:
            print(i)

    def arama(self):
        self.numara = input("aramak istediğiniz numarayı giriniz:")
        
        if self.numara==self.rehber[0] or self.numara==self.rehber[1] or self.numara==self.rehber[2]:
            print("aranıyor")
        else:
            print("hatalı işlem...")

mobil1 = mobil()

while True:
    print ("""
    (1) numara ekle
    (2) numara sil
    (3) rehber görüntüle
    (4) arama yap
    (5) ana sayfaya dön
    """)
    cevap = input("yapmak istediğiniz işlemi seçiniz:")
    if cevap == "1":
        mobil1.ekle()
    elif cevap == "2":
        mobil1.sil()
    elif cevap == "3":
        mobil1.görüntüle()
    elif cevap == "4":
        mobil1.arama()
    elif cevap == "0":
        print("ana sayfaya gidiliyor...")
        break
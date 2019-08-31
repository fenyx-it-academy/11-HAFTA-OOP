class Mobil_tel:

    def __init__(self, marka, model, uretim_yili, tel_no, rehber={}):
        self.marka = marka
        self.model = model
        self.uretim_yili = uretim_yili
        self.tel_no = tel_no
        self.rehber = rehber

    def kisi_ekleme(self, adi, soyadi, mobile_no):
        print("Rehberinize yeni bir kisi ekleniyor...")
        time.sleep(1)
        nam_sur = adi + " " + soyadi
        self.rehber[nam_sur] = mobile_no

    def kisi_silme(self, sil_ad, sil_soyad):
        sil=sil_ad + " " + sil_soyad
        self.rehber.pop(sil)

    def rehber_goruntule(self):
        print(telim.rehber)

    def kisi_arama(self, adi, soyadi):
        print(adi, soyadi, "araniyor. Lutfen bekleyiniz.")
        time.sleep(3)


telim = Mobil_tel("Samsung", "J7", 2015, 6543212468)


print("""Telefon rehberimize hosgeldiniz.
Lutfen yapmak istediginiz islemi seciniz\n
    Rehbere kisi ekleme         1
    Rehberden kisi silme        2
    Kisi arama                  3
""")

import time

while True:

    islem = input("\nLutfen yapmak istediginiz islemi seciniz : ")

    if islem == "1":
        adi = input("Adi : ")
        soyadi = input("Soyadi : ")
        mobile_no = input("Telefon numarasi : ")

        telim.kisi_ekleme(adi, soyadi, mobile_no)
        telim.rehber_goruntule()


    elif islem == "2":
        sil_ad = input("Lutfen silmek istediginiz kisinin adini giriniz : ")
        sil_soyad = input("Lutfen silmek istediginiz kisinin soyadini giriniz : ")

        telim.kisi_silme(sil_ad, sil_soyad)
        telim.rehber_goruntule()

    elif islem == "3":
        adi = input("Adi : ")
        soyadi = input("Soyadi : ")

        telim.kisi_arama(adi, soyadi)
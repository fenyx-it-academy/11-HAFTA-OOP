#Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, uretim yili, tel nosu ve rehber
#ozelliklerinin(class attributes) olmasini bekliyoruz. Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme,
#rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin (class methods) olmasini istiyoruz.

class Telefon():
    marka = ""
    model = ""
    uretim_yili = ""
    tel_no = ""
    rehber_ozellik = []

    def __init__(self,rehber):
        self.rehber = rehber
    def tel_bilgi(self):
        print("Telefon bilgileriniz:","\n",
              "Marka\t\t\t:",self.marka,"\n",
              "Model\t\t\t:",self.model,"\n",
              "Uretim yili\t:",self.uretim_yili,"\n",
              "Tel no\t\t\t:",self.tel_no)

    def no_ekleme(self,telno):
        self.rehber_ozellik.append(telno)
        print("'{}' bilgileri rehberinize eklenmistir.".format(telno))

    def no_silme (self,telnosira):
        print(self.rehber_ozellik[telnosira-1], "bilgileri rehberinizden silinmistir.")
        self.rehber_ozellik.remove(self.rehber_ozellik[telnosira-1])

    def rehber_goruntuleme(self):
        print("Telefon Rehberiniz:")
        for sira,numaralar in enumerate(self.rehber_ozellik,1):
            print("{}:{}".format(sira,numaralar))

    def arama_yap(self,secim):
        print(self.rehber_ozellik[secim-1],"araniyor...")
from time import sleep
print("************  HOSGELDINIZ  ***************")
print("""Telefonunuzu kullanima acmak icin lutfen gerekli bilgileri giriniz:""")
tel_marka = input("Telefonunuzun markasi:")
tel_model = input("Telefonunuzun modeli:")
tel_uretim = input("Telefon uretim yili:")
tel_nosu = input("Telefon numaraniz:")
rehber = input("Telefon rehber ismi:")
Telefon.marka = tel_marka
Telefon.model = tel_model
Telefon.uretim_yili = tel_uretim
Telefon.tel_no = tel_nosu
rehber=Telefon(rehber)
print("Biligileriniz guncelleniyor...")
sleep(2)
print("Basariyla guncellendi.")
sleep(2)
while True:
    print("_____" * 20)
    print("""<<<<<<<< Telefon >>>>>>>>
    Ana Ekran Menusu:
        1. Telefon bilgileri goruntule.
        2: Telefon marka guncelleme.
        3: Telefon model guncelleme.
        4: Telefon uretim yili guncelleme.
        5: Telefon numaranizi guncelleme.
        6: Yeni telefon numarasi ekleme.
        7: Telefon numarasi silme.
        8: Telefon rehberini goruntuleme.
        9: Arama yapma.
        10: Cikis.""")
    try:
        secim = int(input("Lutfen 'Ana Ekran Menusunden' bir secim yapiniz:"))
    except:
        print("Lutfen seciminizi kontrol ediniz!")
        sleep(3)
        continue
    if secim == 10:
        print("Telefonunuz kapatiliyor...")
        sleep(3)
        break
    elif secim < 1 or secim > 10:
        print("Lutfen seciminizi kontrol ediniz!")
        sleep(3)
        continue
    elif secim == 1:
        rehber.tel_bilgi()
        sleep(3)
    elif secim == 2:
        yeni_marka = input("Guncel telefon markanizi giriniz:")
        Telefon.marka = yeni_marka
        print("Bilgileriniz guncellendi.")
        sleep(2)
    elif secim == 3:
        yeni_model = input("Guncel telefon modelinizi giriniz:")
        Telefon.model = yeni_model
        print("Bilgileriniz guncellendi.")
        sleep(2)
    elif secim == 4:
        yeni_tarih = input("Yeni uretim tarihini giriniz:")
        Telefon.uretim_yili = yeni_tarih
        print("Bilgileriniz guncellendi.")
        sleep(2)
    elif secim == 5:
        yeni_no= input("Guncel telefon numaranizi giriniz:")
        Telefon.tel_no = yeni_no
        print("Bilgileriniz guncellendi.")
        sleep(2)
    elif secim == 6:
        tel_no=input("Eklemek istediginiz telefon numarasini giriniz")
        rehber.no_ekleme(tel_no)
        sleep(2)
    elif secim == 7:
        if rehber.rehber_ozellik == []:
            print("Rehberinizde bir telefon numarasi mevcut degildir!!! ")
            continue
        rehber.rehber_goruntuleme()
        try:
            sil_no=int(input("Silmek istediginiz numaranin liste nosunu giriniz: "))
        except:
            print("Liste disi bir secim yaptiniz. giris degerini kontrol ediniz!!!")
            continue
        if sil_no<1 or sil_no>len(rehber.rehber_ozellik):
            print("Liste disi bir secim yaptiniz. giris degerini kontrol ediniz!!!")
            continue
        else:
            rehber.no_silme(sil_no)
            sleep(2)
    elif secim == 8:
        rehber.rehber_goruntuleme()
        sleep(2)
        if rehber.rehber_ozellik == []:
            print("Rehberinizde suan bir numara bulunmuyor")
            continue
        else:
            rehber.rehber_goruntuleme()
            sleep(2)
    elif secim == 9:
        if rehber.rehber_ozellik == []:
            print("Rehberinizde aranacak bir telefon numarasi mevcut degildir!!! ")
            continue
        rehber.rehber_goruntuleme()
        try:
            arama= int(input("Lutfen aramak istediginiz numaranin liste nosunu giriniz:"))
        except:
            print("Liste disi bir secim yaptiniz. giris degerini kontrol ediniz!!!")
            continue
        if arama<1 or arama>len(rehber.rehber_ozellik):
            print("Liste disi bir secim yaptiniz. giris degerini kontrol ediniz!!!")
            continue
        else:
            rehber.arama_yap(arama)
            sleep(3)
            print("Aradiginiz kisi bir baskasiyla gorusuyor, lutfen sonra tekrar deneyiniz!!!")
            sleep(2)



import time

class telefon ():

    def __init__(self,marka, model, uretim_yili, tel_no):
        self.marka = marka
        self.model = model
        self.uretim_yili = uretim_yili
        self.rehber = tel_no

    def rehberi_goruntule(self):
        print("Rehber Goruntuleniyor..")
        time.sleep(2)
        print("""
        Rehber Numalari\n
        {}
        """.format(self.rehber))

    def NoEkle(self,eklenecekNo):
        print("Numara Ekleniyor...")
        time.sleep(2)
        self.rehber.append(eklenecekNo)

    def NoSil(self,silinecekNo):
        print("Numara siliniyor...")
        time.sleep(2)
        self.rehber.remove(silinecekNo)

    def NoArama(self):
        print("""
            Rehber Numaralari
            {}
            """.format(self.rehber))

        secim = int(input("Lutfen aramak istediginiz telefonun sira numarasini giriniz: "))
        print("""
                {} numarali telefon araniyor...""".format(self.rehber[secim - 1]))
        time.sleep(2)


huwai7132 = telefon("huwai",7132,2017,["0647755543"])

huwai7132.NoEkle("0377557790")

huwai7132.rehberi_goruntule()

huwai7132.NoSil("0377557790")

huwai7132.rehberi_goruntule()

huwai7132.NoArama()
























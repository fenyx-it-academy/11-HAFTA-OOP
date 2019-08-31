import random

class Muzikcalar():
    sarkilistesi = []

    def sarki_cal(self, sarki):
        if sarki in self.sarkilistesi:
            print(sarki, "Caliniyor...")
        else:
            print("Sarki listenizde boyle bir sarki ekli degil...")

    def sarkilistesi_sifirla(self):
        self.sarkilistesi.clear()
        print("\nSarki Listeniz Sifirlandi...")

    def sarkilistesi_goruntule(self):
        print("\nSarki Listesi\n")
        for i in self.sarkilistesi:
            print(i)

    def sarki_ekle(self, sarki):
        print("\n", sarki, "eklendi..")
        self.sarkilistesi.append(sarki)

    def sarki_sil(self, sarki):
        self.sarkilistesi.pop(self.sarkilistesi.index(sarki))
        print('\n', sarki, "silindi..")

    def sonrakisarki_cal(self, sarki):
        a = self.sarkilistesi.index(sarki)
        print("\nSonraki Sarki")
        print(self.sarkilistesi[a + 1], "caliniyor...")

    def oncekisarki_cal(self, sarki):
        a = self.sarkilistesi.index(sarki)
        print("\nOnceki Sarki")
        print(self.sarkilistesi[a - 1], "caliniyor...")

    def karisik_cal(self):
        karisik = random.randint(0, len(self.sarkilistesi) - 1)
        print(self.sarkilistesi[karisik], "Caliniyor..")


m1 = Muzikcalar()

m1.sarki_ekle("Ahmet Kaya - Kum Gibi")

m1.sarki_ekle("Ahmet Kaya - Aglama Annem")

m1.sarki_ekle("Ahmet Kaya Oyle Bir Yerdeyim Ki")

m1.sarki_ekle("Ahmet Kaya - Aglama Annem (Konser)")

m1.sarkilistesi_goruntule()

m1.sarki_sil("Ahmet Kaya - Aglama Annem (Konser)")

m1.sonrakisarki_cal("Ahmet Kaya - Kum Gibi")

m1.oncekisarki_cal("Ahmet Kaya Oyle Bir Yerdeyim Ki")

m1.sarkilistesi_goruntule()
m1.karisik_cal()
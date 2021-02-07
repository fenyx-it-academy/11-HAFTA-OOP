class TelefonRehberi():
    marka = ""
    model = ""
    uretimYili = ""
    telNo = ""
    rehber = []

    def rehberEkle(self, numara):
        print("\n", numara, "eklendi..")
        self.rehber.append(numara)

    def rehberSil(self, numara):
        if numara not in self.rehber:
            print("rehberde böyle bir numara yok")
        else:
            print("\n", numara, "siliniyor..")
            self.rehber.pop(self.rehber.index(numara))

    def rehberGoruntule(self):
        print("rehber goruntuleniyor:")
        for i in self.rehber:
            print(i)

    def rehberAra(self, numara):
        if numara not in self.rehber:
            print("böyle bir numara yok")
        else:
            print("\n rehberdeki", numara, "aranıyor..")


r1 = TelefonRehberi()

r1.rehberEkle("1")
r1.rehberEkle("2")
r1.rehberEkle("3")
r1.rehberGoruntule()

r1.rehberSil("3")

r1.rehberGoruntule()

r1.rehberAra("2")
class TelefonRehberi():
    marka = ""
    model = ""
    uretimYili = ""
    telNo = ""
    rehber = []

    def rehberEkle(self,numara):
        print("\n", numara , "eklendi.")
        self.rehber.append(numara)

    def rehberSil(self,numara):
        for i in self.rehber:
            if i == numara:
                print("\n", numara, "numara silindi.")
                self.rehber.pop(self.rehber.index(numara))


    def rehberGoruntule(self):
        for i in self.rehber:
            print(i)


    def rehberAra(self,ad):
        for i in self.rehber:
            if i == numara:
                print("\n", numara, "araniyor..." )

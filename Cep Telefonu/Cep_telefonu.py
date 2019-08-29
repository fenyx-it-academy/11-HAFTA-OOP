class telefon():
    rehber=[]
    #rehbere no ekleme, silme, rehberi goruntuleme
    def __init__(self,marka,model,uretim_yili,tel_no):
        self.marka = marka
        self.model = model
        self.uretim_yili = uretim_yili
        self.tel_no = tel_no
    def No_ekleme(self,no):
        self.rehber.append(no)
    def No_silem(self,no):
        for i in self.rehber:
            if i==no:
                self.rehber.remove(i)
    def rehberi_goruntule(self):
        print(self.rehber)
    def no_ara(self,no):
        for i in self.rehber:
            if i == no:
                print("{} nosu araniyor.....".format(i))


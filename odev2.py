class telrehber(object):
    def __init__(self,name,marka,model,uretimyil,telno):
        self.name=name
        self.marka=marka
        self.model=model
        self.uretimyil=uretimyil
        self.telno=telno
        self.rehber=[]
    def persongoruntule(self):
        print("""         telsahibi   :{}
        tel_marka    :{}
        tel_model    :{}
        tel_urtimyil :{}
        tel_no       :{}""".format(self.name,self.marka,self.model,self.uretimyil,self.telno))
    def rehbernoekle(self,number):
        self.number=number
        if self.number in self.rehber:
            print("bu {} numara zaten daha once girilmis".format(self.number))
        else:
            self.rehber.append(self.number)
    def rehbersilme(self,number):
        self.number=number
        if self.number in self.rehber:
            self.rehber.remove(self.number)
        else:
            print("silmek istediginiz {} numara listede yoktur: ".format(self.number))
    def rehbergoruntuleme(self):
        return print(self.rehber)
    def noarama(self,number):
        self.number=number
        if self.number in self.rehber:
            print("Aradiginiz {} numara listede vardir:".format(self.number))
        else:
            print("aradiginiz {} numara listede yoktur ".format(self.number))
def sorgu():
    sorgu=input("""                         Lutfen numara eklemek icin: 1
     Lutfen numara silmek icin:                      2
     Lutfen numara sorgulamak icin:                  3
     Lutfen rehberi goruntulemek icin:               4
     Lutfen Telefon Bilgilerini goruntulemek icin:   5
     Cikmak icin:                                    6
     basiniz""")
    return sorgu
person=input("Lutfen telefonun sahibinin adini giriniz: ")
marka=input("Lutfen telefon markasini giriniz: ")
model=input("Lutfen telefon modelini giriniz: ")
yil=input("lutfen telefon uretim yilini giriniz: ")
telno=input("Lutfen telefona ait hattin numarasini yaziniz")
person=telrehber(person,marka,model,yil,telno)
while True:
    sorguu=sorgu()
    if sorguu=="1":
        numara = input("eklemek istediginiz numarayi giriniz: ")
        person.rehbernoekle(numara)
    elif sorguu=="2":
        numara = input("silmek istediginiz numarayi giriniz: ")
        person.rehbersilme(numara)
    elif sorguu=="3":
        numara = input("sorgulamak istediginiz numarayi giriniz: ")
        person.noarama(numara)
    elif sorguu=="4":
        person.rehbergoruntuleme()
    elif sorguu=="5":
        person.persongoruntule()
    elif sorguu=="6":
        quit()

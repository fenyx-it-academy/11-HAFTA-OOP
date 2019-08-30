##Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
##Telefonun
##marka,
##model,
##uretim yili,
##tel nosu
##ve rehber gibi obje ozelliklerinin(instance attributes) olmasini bekliyoruz.
##Ayrica bu objenin
##rehbere no ekleme,
##silme,
##rehberi goruntuleme,
##rehberden secilen bir noyu arama(gostermelik)
##gibi ozelliklerinin
##(class methods) olmasini istiyoruz.
class telefon_rehberi():
    "telefon rehberi"
    def __init__(self,marka, model, uretim_yili, telno, isim, numara):
        self.marka=marka
        self.model=model
        self.uretim_yili=uretim_yili
        self.telno=telno
        self.isim=isim
        self.numara=numara
    def bilgi(self):
        print("""
        telefon Bilgisi:
        marka: {}
        model: {}
        uretim_yili: {}
        telno: {}
        isim: {}
        numara:{}""".format( self.marka, self.model, self.uretim_yili, self.telno, self.isim, self.numara))
    def rehberigoruntule(self):
        print("isim:",self.isim,"numarasi:",self.numara)
    def kisiekle(self, ad, numara):
        print("kisi ekleniyor..")
        self.isim.append(ad)
        self.numara.append(numara)
        
    def kisisil(self, adim, numaram):
        print("kisi siliniyor..")
        self.isim.remove(adim)
        self.numara.remove(numaram)
        
    def arama(self,ad):
        print(ad,"araniyor".format(self.isim))
rehberim=telefon_rehberi ("huwai","mate 20 lite", 2018,+3163285456+25, [""],[""])
print("telefon bilgileri icin 0'a basiniz\nrehberi goruntulemek icin 1'e basiniz\nkisieklemek icin 2'ye basiniz\nkisi silmek icin 3'e basiniz\narama yapmak icin 4'e basiniz\ncikmak icin 5'e basiniz:")
while True:
    secim=input("seciminiz:")
    if secim =="0":
        rehberim.bilgi()
    if secim =="1":
        rehberim.rehberigoruntule()
    elif secim =="2":
        a=input("kaydedilcek kisinin adini giriniz:")
        b=int(input("kaydedilcek kisinin numarasini giriniz:"))
        rehberim.kisiekle(a,b)
    elif secim =="3":
        c=input("silinecek kisinin adi:")
        d=int(input("silinecek kisinin nosu:"))
        rehberim.kisisil(c,d)
        
        
    elif secim =="4":
       ab=input("aranacak kisyi giriniz:")
       rehberim.arama(ab)
    elif secim =="5":
        print("cikiliyor...")
        break
        
    
        
        
        
##kisi=telefon_rehberi("seyma,", 216285162)
##kisi1=telefon_rehberi("rukiye,",252624)
##
##
##kisi.rehberigoruntule()
##kisi1.rehberigoruntule()

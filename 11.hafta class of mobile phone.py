##Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
##Telefonun marka, model, 
##uretim yili, tel nosu ve rehber ozelliklerinin(class attributes)
##olmasini bekliyoruz. 
##Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme,
##rehberden secilen bir noyu 
##arama(gostermelik) gibi ozelliklerinin (class methods) olmasini
##istiyoruz.

class CepTelefonu():        #Class tanimlayip kensi bilgi girecek sekilde __init__kullaniyoruz
    def __init__(self,marka,model,uretim_yili,tel_no,rehber=[]):
        self.marka=marka
        self.model=model
        self.uretim_yili=uretim_yili
        self.tel_no=tel_no
        self.rehber=rehber
    def bilgilerigoster(self):  #bu metodla tum ozellikleri yazdirmasini istiyoruz
        print("""
        Telefonun Ozellikleri:
        
        Marka: {}

        Model: {}

        Uretim Yili: {}

        Tel No: {}

        Rehber: {}
        """.format (self.marka,self.model,self.uretim_yili,
                    self.tel_no,self.rehber))
    def rehbere_ekle(self,yeni_no): #bu metod rehbere yeni no eklemeyi sagliyor. Rehber listeydi eklemede append kullaniliyor
        self.rehber.append(yeni_no)
        print("Rehbere yeni no eklendi...\n")
        
    def rehber_sil(self,sil_no):        #rehberden no siliyor
        self.rehber.pop(sil_no)
        print(sil_no,"\tRehberden silindi...")
    def rehberigoster(self):            #rehberin son halini cikti veriyor
        print("""
        Rehber: {}""".format(self.rehber))
    def arama(self,ara_no):     #rehberden bir no'yu aramayi sagliyor
        for i in self.rehber:
            if i==ara_no:
                print(ara_no,"numarasi araniyor...")
                print("Baglaniyor...")
telefon=CepTelefonu("Samsung","A20",2017,345)                    
print("""
        Yapmak İstediginiz islemi seciniz:

        1. Telefonun Ozelliklerini Goruntulemek

        2. Rehbere No Eklemek

        3. Rehberden No Silmek

        4. Rehberi Goruntulemek

        5. Rehberden No Arama

        6. Cikis

        """)

while True:                     #while ile kurulan menuden seceneklerle istedigimizi yapiyoruz
    islem=int(input("Yapmak İstediginiz İslemi Seciniz: "))
    if 1>islem>7:
        print("Yanlis bir tusa bastiniz.Tekrar deneyiniz...")
        continue
    elif islem==6:
        print("Programdan cikiliyor...\n")
        break
    elif islem==1:
        telefon.bilgilerigoster()
    elif islem==2:
        yeni_no=input("10 hanelik yeni tel no giriniz: ")
        if len(yeni_no)!=10:
            print("Lutfen 10 haneli bir numara giriniz...\n")
            continue
        else:
            telefon.rehbere_ekle(yeni_no)
    elif islem==3:
        sil_no=int(input("Silmek istediginiz 10 hanelik no'yu giriniz: "))
        telefon.rehber_sil(sil_no)
    elif islem==4:
        telefon.rehberigoster()
    elif islem==5:
        telefon.rehberigoster()
        ara_no=input("Aramak istediginiz numarayi seciniz: ")
        telefon.arama(ara_no)
    else:
        print("Yanlis islem secimi yaptiniz... Tekrar deneyiniz...\n")
        continue
        
        


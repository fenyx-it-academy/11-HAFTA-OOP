#Odev 2:
#Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, 
#uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) 
#olmasini bekliyoruz. Ayrica bu objenin rehbere no ekleme, silme, 
#rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik) 
#gibi ozelliklerinin (class methods) olmasini istiyoruz. 
import random
class ceptelefonu():
    def __init__(self,marka,model,uretimyili,numaralar,isimler):
        self.marka = marka
        self.model = []
        self.uretimyili = uretimyili
        self.numaralar = []
        self.isimler = []
    def isim_ekle(self,isim):
        aa=self.isimler.append(isim)
        print('{} adlı kişi eklendi'.format(self.isimler))
        return aa
    def isim_silme(self,isim):
        bb=self.isimler.remove(isim)
        print('{} adlı kişi silindi'.format(self.isimler))
        return bb
    def rehber_goruntule(self):
        print('Kisi listesi:')
        for kisi in self.isimler:
            print(kisi)
    def numara_ekle(self,numara):
        self.numaralar.append(numara)
        print('{} numarasi eklendi'.format(self.numaralar))
        
    def model_ekle(self, modeli):
        cc=self.model.append(modeli)
        return cc
    def model_goruntule(self):
        print('{} marka telefonlarin modelleri:'.format(self.model))
        for Model in self.model:
            print(Model)
    def uretim_yili(self): 
        print(self.uretimyili) 
    def numara_arama(self):
        dd=random.choice(self.numaralar)
        print("{} nolu numara araniyor..".format(dd))
        
cep1 = ceptelefonu('IPHONE','Iphone7','20.09.2019','o9o5o58765432','Ensar Baltas')
cep2 = ceptelefonu('IPHONE','Iphone6','20.09.2015','o9o5o52345678','Erkan Sen')
cep3 = ceptelefonu('IPHONE','Iphone5','20.09.2010','o9o5o59876543','Ahmet Sahin')
cep1.isim_ekle('Ali Kaya')
cep1.isim_ekle('Ayse Sahin')
cep1.isim_silme('Ali Kaya')
cep1.numara_ekle('050599999999')
cep2.model_ekle('IphoneX')
print(cep1.isimler)
print(cep3.marka)
print(cep2.model)
print(cep1.uretimyili)
print(ceptelefonu.rehber_goruntule(cep1))
print(cep1.numara_arama())



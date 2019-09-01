#Odev 2:
#Bir cep telefonu objesi yapmanizi istiyoruz. Telefonun marka, model, 
#uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) 
#olmasini bekliyoruz. Ayrica bu objenin rehbere no ekleme, silme, 
#rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik) 
#gibi ozelliklerinin (class methods) olmasini istiyoruz. 

class ceptelefonu():
    rehber = []
    def __init__(self,marka,model,uretimyili,numaralar,rehber):
        self.marka = 'IPHONE'
        self.model = []
        self.uretimyili = ()
        self.numaralar = ()
        self.rehber = []
    def isim_ekle(self):
        self.rehber.append(self.isim)
        print('{} adlı kişi eklendi'.format(self.isim))
    def isim_silme(self):
        self.rehber.pop(self.isim)
        print('{} adlı kişi silindi'.format(self.isim))
    def rehber_goruntule(self):
        print('Kisi listesi:')
        for kisi in self.rehber:
            print(kisi)
    def model_ekle(self, Model):
        self.model.append(Model)
    def model_goruntule(self):
        print('{} marka telefonlarin modelleri:'.format(self.model))
        for Model in self.model:
            print(Model)
    def uretim_yili(self): 
        print(self.uretimyili)
        
cep1 = ceptelefonu('IPHONE','Iphone7','20.09.2019','o9o5o58765432','Ensar Baltas')
cep2 = ceptelefonu('IPHONE','Iphone6','20.09.2015','o9o5o52345678','Erkan Sen')
cep3 = ceptelefonu('IPHONE','Iphone5','20.09.2010','o9o5o59876543','Ahmet Sahin')
print(ceptelefonu.cep1)


  



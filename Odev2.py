# Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
# Telefonun marka, model, uretim yili, tel nosu ve rehber
# ozelliklerinin(class attributes) olmasini bekliyoruz.
# Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme,
# rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin
# (class methods) olmasini istiyoruz.


class telefon():
    def __init__(self, marka, model, uretimYili, telNo, rehber):
        self.marka = marka
        self.model = model
        self.uretimYili = uretimYili
        self.telNo = telNo
        self.rehber = rehber

    def rehbereEkle(self, isim, numara):
        isim = isim.lower()
        self.rehber.append([isim, numara])
        print('{} rehbere Eklendi...'.format(isim))
    def rehberdenSil(self,isim):
        isim = isim.lower()
        for i in self.rehber:
            if isim in i:
                self.rehber.remove(i)
                print('Rehberden Silindi...')
                break
            else:
                print('Rehberde boyle bir kayit bulunamadi!')
                break

    def rehberiGoruntule(self):
        if len(self.rehber) == 0:
            print('Rehberiniz bos..')
        else:
            for i in self.rehber:
                print("""
                      Isim : {}                
                      Numara : {}               
                      -----------
                      """.format(i[0], i[1]))
    def numaraAra(self, isim):
        isim = isim.lower()
        for i in self.rehber:
            if isim in i:
                print('{} Araniyor...'.format(isim))
            else:
                print('Rehberde boyle bir kayit bulunamadi!')




zeydinTelefonu = telefon('General Mobile', 'GM8', '2018', '053215484',[])
print('''
Zeydin Telefonu olusturuldu..

Marka: {}
Model: {}
Uretim Yili: {}
Numara: {}
Rehber: {}

'''.format(zeydinTelefonu.marka, zeydinTelefonu.model, zeydinTelefonu.uretimYili,
           zeydinTelefonu.telNo, zeydinTelefonu.rehber))

while True:
    print('*' * 30 + '\n\n' + 'Telefon Rehberi'.rjust(
        22) + '\n\n' + '1.Rehbere Ekle\n' + '2.Rehberden Sil\n' + '3.Numara Ara\n'
          + '4.Rehberi Goruntule\n'+ 'Cikis icin "q" ya basin!\n\n' + '*' * 30 + '\n')

    islem = input('Lutfen yapmak istediginiz islemi secin:')

    if islem == '1':
        isim = input('Isim Girin: ')
        numara = input('Numara Girin: ')
        if numara.isdigit() == True:
            zeydinTelefonu.rehbereEkle(isim, numara)
        else:
            print('Lutfen sadece numara girin!')
    elif islem == '2':
        isim = input('Silmek istediginiz ismi girin: ')
        zeydinTelefonu.rehberdenSil(isim)
    elif islem == '3':
        isim = input('Aramak istediginiz ismi girin: ')
        zeydinTelefonu.numaraAra(isim)
    elif islem == '4':
        zeydinTelefonu.rehberiGoruntule()
    elif islem == 'q':
        print('Programdan cikiliyor...')
        break
    else:
        print('Gecersiz islem! tekrar deneyin..')
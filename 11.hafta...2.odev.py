print('b.')
'''
Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz. 
Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz. 
Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, 
rehberden secilen bir noyu arama(gostermelik) gibi ozelliklerinin (class methods) olmasini istiyoruz.
'''
import time
class Telefon:


    def __init__(self,marka,model,uretim_yili,seri_no,rehber):
        self.marka=marka
        self.model=model
        self.uretim_yili=uretim_yili
        self.seri_no=seri_no
        self.rehber=rehber
        self.rehber={}


    def yazdir(self):
        print(f'markasi :{self.marka}\nmodeli :{self.model}\nuretim yili :{self.uretim_yili}\nseri_no :{self.seri_no}\n'
              f'rehber :{self.rehber}')


    def rehbere_no_ekleme(self, isim, tel):
        self.rehber[isim]=tel


    def reh_goster(self):
        for isim, tel in self.rehber.items():
            print(isim, ':', tel)


    def rehberden_no_silmek(self,isim):
        if isim in self.rehber:
           print(f'{isim} siliniyorrrrr')
           time.sleep(5)
           print('\nbasariyla silindi')
        else:
            print('girmis oldugunuz isim rehberde yok')


    def no_arama(self):
        isim=input('>>>>>....lutfen aramak istediginiz kisinin ismini giriniz\n')
        if isim in self.rehber:
            print(f'{self.rehber[isim]} araniyorrrrr....\n')
            time.sleep(5)
            print(f'{self.rehber[isim]} nolu telefon no mesgul...sonra tekrar deneyiniz')
        else:
            print('\n>>>>>....lutfen girmis oldugunuz ismi kontrol ediniz')

# classimiza telefonlari tanimladik
a_telefonu=Telefon('samsung', 'S 8', 2017, 'a2M6jkdkkD89', rehber={})
b_telefonu=Telefon('nokia', 'c 3', 2000, 'jjW2oeieCD', rehber={})
#telefon secimi yaptirdik
print('Lutfen bir telefon seciniz...\na_telefonu\nb_telefonu')
x_telefonu=input('telefon sec...>>>')

if x_telefonu== 'a_telefonu':
    x_telefonu=a_telefonu
else:
    x_telefonu=b_telefonu

def giris():
    print('''
    >>>...Menu...<<<
    1-telefon marka model goster
    2-reh kisi ekle
    3-rehberi goster
    4-kisi silme
    5-No ara
    >>>>...cikis icin bir tusa basiniz ''')
while True:
    giris()
    cvp = input('tercih yapiniz....>>>')
    if cvp not in "1,2,3,4,5":
        print('lutfen menuden dogru degerleri giriniz')
    else:
        if cvp=='1':  # model yazirma
            x_telefonu.yazdir()
        elif cvp == '2':  # kisi ekleme
            isim = input('rehbere eklemek istediginiz kisinin adini gir')
            tel = input('rehbere eklemek istediginiz kisinin tel gir')
            x_telefonu.rehbere_no_ekleme(isim, tel)
        elif cvp == '3':  # rehberi goster
            x_telefonu.reh_goster()
        elif cvp == '4':  # kisi silme
            isim = input('silmek istediginiz ismi giriniz....:')
            x_telefonu.rehberden_no_silmek(isim)
        elif cvp == '5':  # no arama
            x_telefonu.no_arama()
        else:
            print('cikiliyor....bye')
            quit()

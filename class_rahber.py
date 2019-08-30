# Odev 2: Bir cep telefonu objesi yapmanizi istiyoruz.
# Telefonun marka, model, uretim yili, tel nosu ve rehber ozelliklerinin(class attributes) olmasini bekliyoruz.
# Ayrica bu objenin rehbere no ekleme, silme, rehberi goruntuleme, rehberden secilen bir noyu arama(gostermelik)
# gibi ozelliklerinin (class methods) olmasini istiyoruz.
import time
class telephone():
    marka='SAMSUNG'
    model='FUTURE M00999'
    uretim_yili='2019'
    imei_no=876507231455600
    telefon_numarasi='+31 684 3454545'
    rehber = []
    def __init__(self,adi_soyadi,telefon_no):
        self.adi_soyadi=adi_soyadi
        self.telefon_no = telefon_no

    def kayit_ekle(self,kayit):
        self.rehber += [kayit]

    def rehberi_goster(self):

            sayac=0
            for i in self.rehber  :

                print (sayac, i.adi_soyadi , i.telefon_no )
                sayac+=1

    def arama_yap(self):
        print("arama yapiliyor")

#*******************************************************************************


while True:
    print ( """------------------------------------------
                Ana Menu

                1-Telefon Info
                2-Rehber
                3-Arama Yap
                4-Kapatmak
------------------------------------------
    """ )

    menu=input("Menu seciminizi yapiniz:")

    if menu.isdigit()==False or len(menu)!=1:
        print('yanlis tusa bastiniz..')
        continue

    elif menu=='1':
        print("""*****************************************
        Telefon Info
{}
{}
{}

imei no   ={}
telefon no={}

*****************************************
        """.format(telephone.marka,telephone.model,telephone.uretim_yili,telephone.imei_no,telephone.telefon_numarasi))
        time.sleep(2)
        print('Ana menuye yonlendiriliyorsunuz..................')
        time.sleep(2)
        continue
    elif menu == '2' :


        while True:
            try:
                print("""*****************************************
                REHBER MENU

                0-ANA MENU
                1-KISILER
                2-ARAMA
                3-KAYIT
                4-KAYIT SIL
                5-TUM KAYITLARI SIL

                *****************************************
                """)
                rehber_menu=input('Islem seciniz:')

                if rehber_menu=='0':
                    print('Ana Menu ye donuluyor....')
                    time.sleep(2)
                    break


                elif rehber_menu=='1':


                    if telephone.rehber==[]:

                       print('rehberinizde kayit bulunamadi')
                       continue
                    else:

                        telephone.rehberi_goster(kayit)
                        time.sleep(2)


                elif rehber_menu == '2' :
                    if telephone.rehber == [] :

                        print ( 'rehberinizde kayit bulunamadi' )
                        continue
                    else :

                        telephone.rehberi_goster ( kayit )

                        ara=input('Aramak istediginiz kayit sirasini giriniz: ')
                        a=telephone.rehber[int(ara)]
                        print(a.adi_soyadi,' araniyor......')
                        print(a.telefon_no,'diiiit,diiiiit........')
                        time.sleep(2)
                        print('Aranan kisye ulasilamiyor ')
                        print('Menuye donuluyor....')



                elif rehber_menu=='3':

                    isim= input ( 'Adi soyadi giriniz:' )
                    no= input ( 'numara' )
                    kayit = telephone ( isim,no )
                    kayit.kayit_ekle ( kayit )


                elif rehber_menu == '4' :
                    telephone.rehberi_goster(kayit)
                    sil=input('silmek istediginiz kaydin sirasini giriniz :')
                    telephone.rehber.pop(int(sil))
                    print ( 'kaydiniz siliniyor....' )
                    time.sleep(2)
                    print('kayit basari ile silindi. ')
                    print('menuye donduruluyorsunuz.....')
                    time.sleep(2)


                elif rehber_menu == '5' :
                    telephone.rehber.clear()
                    print('Tum kayitlar silindi')
                    time.sleep(2)

                else:
                    print('yanlis tusa bastiniz')
            except:
                print('Yanlis islem')
                continue

    elif menu=='4':
        print('Tum islemler kaydediliyor....')
        time.sleep(2)
        print('kapaniyor....')
        break

    else:
        print('yanlis islem')





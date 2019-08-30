#
# Odev 3: Bir muzik calar objesi yapmanizi istiyoruz.
# Class attribute olarak bos bir sarki listesi olusturun.
# Class methods olarak sarki listesini sifirlama,
# listeyi goruntuleme, sarki ekleme, sarki silme, sonraki parcayi cal,
# onceki parcayi cal, karisik cal ozelliklerini ekleyin.
import random
import time


class muzik_calar():
    sarki_liste=[]

    def __init__(self,sarki_isim,sarkici):
        self.sarki_isim=sarki_isim
        self.sarkici=sarkici


    def ekle(self):
        self.sarki_liste+=[self]
    def goster(self):
        print('\n',' '*19,'*'*57)
        print( ' '*22,'        SARKI LISTESI  ')
        sayac = 1
        for i in self.sarki_liste :
            print ( ' '*22, sayac ,i.sarkici,"---",i.sarki_isim )
            sayac+=1
        print('\n'*3)
    def calisma(self,parca):
        if parca==len(self.sarki_liste):
            parca=0
        if parca==-1:
            parca=len(self.sarki_liste)

        print('\n'*3,
            """                       NAIMENS MUSIC PLAYER
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                        
                                    [] Stop

                              playing.................


                    Previous <        {} {}      > Next

                                   Shuffle(S)
                    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""".format(self.sarki_liste[parca].sarkici,self.sarki_liste[parca].sarki_isim))



    def durdurma(self):
     print ( '\n'*3,
         """                             NAIMENS MUSIC PLAYER
                      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                                              (K)'KAPAMA'
                                                [] durdurma


                         onceki sarki <         <>        > sonraki sarki
                                              baslat





                         listeyi Sil (  L )              ( D ) sarki sil

                         sarki ekle  (  E )              ( S )karistir

                      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            """ )
    def karistir(self):
        random.shuffle(self.sarki_liste)
        return self.sarki_liste



parca = random.randint(0,len ( muzik_calar.sarki_liste ) )

muzik_calar.durdurma(muzik_calar)
if muzik_calar.sarki_liste == [] :
    print(' MUZIK PLAYER ILK KULLANIM ICIN HAZIRLANIYOR')
    time.sleep(2)
    print ('\n','Dikkat Sarki listeniz bos durumda lutfen sarki yukleyiniz.' )

while True:
    try:



        sec=input("""
        LISTE ISLEMLERI:


        EKLE               ----> E
                LISTEYI GOR        ----> G
                        SARKI SIL          ----> D
                                LISTE SIL          ----> L
                                        MUZIK CALARI BASLAT----> <>
                                                KAPATMA TUSU       ----> K
    --->:""").upper()
        if sec == 'E' :

            sarkici = input ( 'Sarkicinin ismini giriniz' ).upper()
            sarki = input ( 'Sarkinin ismini giriniz' ).upper()
            kayit = muzik_calar ( sarki , sarkici )
            kayit.ekle ()
            print('ekleniyor....')
            time.sleep(2)

        elif sec=='G' and muzik_calar.sarki_liste != [] :
            kayit.goster()



        elif sec=='D' and muzik_calar.sarki_liste != [] :
            kayit.goster()
            print('silmek istediginiz sarki sirasini giriniz:')
            sil=input('--->:')
            muzik_calar.sarki_liste.pop(int(sil)-1)
            print('siliniyor...')
            time.sleep(2)
        elif sec=='L' and muzik_calar.sarki_liste != [] :

            print('Tum sarkilar siliniyor...')
            muzik_calar.sarki_liste.clear()
            time.sleep(3)
        elif sec=='K':
            print('muzik calar kapaniyor....')
            time.sleep(2)
            break

        elif sec=='<>' and muzik_calar.sarki_liste != [] :
            print ( 'Listeler yukleniyor....' )
            time.sleep ( 2)
            print ( 'Muzik Calar basliyor' )
            time.sleep(3)
            parca = parca
            kayit.calisma ( parca )

            kayit.goster()
            while True:

                key=input("Muzik Player uzerindeki tuslarla komut edin").upper()

                if key == '[]':
                    print ( 'muzik calar durduruldu.' )
                    kayit.durdurma()
                    time.sleep(3)
                    print('Ana menuye gidiliyor......')
                    break

                elif key=='>':
                    print('sonraki parca caliniyor')
                    parca+=1
                    kayit.calisma ( parca )

                    kayit.goster()

                elif key == '<' :
                    print ( 'onceki parca caliniyor' )
                    parca -= 1
                    kayit.calisma ( parca )

                    kayit.goster ()
                elif key =='S':
                    print ( 'parcalar rasgele caliniyor' )
                    kayit.karistir (  )
                    kayit.calisma ( parca )
                    kayit.goster ()
        else:
            print('yanlis bir tusa bastiniz veya listeniz bos')
            continue



    except:
        print('yanlis islem')




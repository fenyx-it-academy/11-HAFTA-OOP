"""
Odev 1: Gecen hafta basladigimiz amiral batti oyununu gelistirecegiz.
Bu hafta kodunuzu Object Oriented sekline cevirmenizi istiyoruz.
Ayrica randomsuz yapanlarin random gemi yerlestirme ozelligini eklemelerini bekliyoruz.
Bonus ozellik olarak oyunun bilgisayara karsi oynanan iki kisilik versiyonunu yapabilirsiniz.
"""

import random
import time
from Akilli_Amiral_batti.AmiralBatti import Gemi
gemi=Gemi()
tablo=gemi.tablo
tahta = gemi.tahta
gemiler=gemi.gemi_olusturma()
hamle_koordinat = []
counter=0
batan_gemiler=[]
def hamle_kontrol(x):
    if [x[0],x[1]] not in hamle_koordinat:
        hamle_koordinat.append([x[0],x[1]])
        return 0
    return 1

def hamle():
    d=0
    print("                       1 2 3 4 5 6 7 8 9 10")
    for row in tablo:
        d+=1
        print("                     {}".format(d)," ".join(row))
    print("     Lutfen bir hamle de bununuz")
    x = int(input("     Yukaridan asagiya (1 den 10 a kadar):"))
    y = int(input("     Soldan saga (1 den 10 a kadar):"))
    x = x - 1
    y = y - 1

    return [x, y]


print("""         ------------AMIRAL BATTI OYUNU------------
         -----------2 Adet 4 birimlik--------------
         -----------2 Adet 3 birimlik--------------
         -----------2 Adet 2 birimlik--------------
         -----------2 Adet 1 birimlik--------------
         -----------Gemiler bulunmaktadir----------
         -Toplam 15 yanlis hakkiniz bulunmaktadir--
         ---------------BASARILAR------------------         
""")
sira=1
batan_gemi_sayisi=0
while True:
    print("Kalan yanlis hamle sayiniz:", 15-counter)
    if batan_gemi_sayisi<8:
        if counter==15:#15 hak dolma kontrolu
            print("15 hamle hakkiniz doldu. Oyunu kaybettiniz.")
            for i in gemiler:
                for j in i:
                    for k in j:
                        k=list(k)
                        tablo[k[0]][k[1]] = "X"# 15 hak dolduktan sonra bulunamayan gemiler Y harfi ile gosteriliyor.
            for i in tablo:
                print("                      ", " ".join(i))
            break
        else:
            koordinat=hamle()# kullanicinin hamleleri aliniyor.
            if hamle_kontrol(koordinat)==0:# onceden girilen bir kordinat mi diye bakiliyor
                counter += 1 #oynanan hak bir artiriliyor.
                sonuc=gemi.gemi_batirma(gemiler,koordinat)#koordinatlar herhangi bir geminin kordinati mi diye bakiliyor.
                if sonuc!=1:# kordinat bir gemiye aitse
                    gemi.gemiyi_goster(sonuc)#gemi tabloya ekleniyor ve gosteriliyor.
                    print("BU HAMLEDE BIR GEMI BATTI. TEBRIKLER. IYI GIDIYORSUNUZ..")
                    batan_gemi_sayisi+=1
                    print("Batan gemi sayisi: {}, kalan gemi sayisi:{}".format(batan_gemi_sayisi,8-batan_gemi_sayisi))
                    counter-=1#oyun hakki azalmasin diye oynanan haklar bir eksiltiliyor.
                elif sonuc==1 and tablo[koordinat[0]] [koordinat [1]] =="O":#oynan kordinat bir gemiye ait degilse ve tabloda bos alansa. B harfi ile degistiriliyor.
                    gemi.bosu_goster(koordinat)#tablo yazdiriliyor.
                    print("Bos hamle yaptiginiz icin 5 sn bekleyeceksiniz.")
                    time.sleep(5)#bos hamlede 5 sn bekletiliyor.
                    print ("Oyun devam ediyor.")
                elif sonuc==1 and tablo[koordinat[0]] [koordinat [1]] =="X":#kordinat onceden bulunan bir gemiye ait mi kontrolu yapiliyor.
                    print("Bu alan batirilan bir geminin parcasi.")
                    counter-=1#onceden bulunan bir gemiye aitse hakki azalmasin diye eksiltme yapiliyor.
            elif hamle_kontrol(koordinat)==1:
                print("     !!!!BU HAMLEYI ONCEDEN YAPMISTINIZ!!!")
    else:
        print("     BUTUN GEMILER BATIRILDI....TEBRIKLER")
        break

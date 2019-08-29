print('b.')
import random as r
import time
print('>>>>>>>>>>>>>>>>>>>>...Amiral batti oyununa HOSGELDINIZ...s<<<<<<<<<<<<<<<<<<<<\n'
      '>>>>>>>>>>>>>>>>>>>>>>>>>>>>.......2.0.......<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
      '2 tane 4 birim \t( * * * * )\n2 tane 3 birim\t(  * * *  )\n'
      '2 tane 2 birim \t(   * *   )\n2 tane 1 birim \t(    *    )  sekillerinden olusan 8 tane gemi vardir \n'
      'tablodaki dogru kordinatlari girerek 15 tahminde bulmaya calisiniz...Basarilar')

tahta =  [[' '," 1","2","3","4","5","6","7","8","9","10"],
          ['1 ',"-","-","-","-","-","-","-","-","-","-"],
          ['2 ',"-","-","-","-","-","-","-","-","-","-"],
          ['3 ',"-","-","-","-","-","-","-","-","-","-"],
          ['4 ',"-","-","-","-","-","-","-","-","-","-"],
          ['5 ',"-","-","-","-","-","-","-","-","-","-"],
          ['6 ',"-","-","-","-","-","-","-","-","-","-"],
          ['7 ',"-","-","-","-","-","-","-","-","-","-"],
          ['8 ',"-","-","-","-","-","-","-","-","-","-"],
          ['9 ',"-","-","-","-","-","-","-","-","-","-"],
          ['10',"-","-","-","-","-","-","-","-","-","-"]]

def tablo():
    print('-'*70)
    for i in tahta:
       print(*i)
    print("-"*70,'\n( dogru hamleler "*", yanlis hamleler "X" isareti ile belirtilmistir )\n',"-"*70)
print('>>>>>>  Lutfen bekleyiniz gemiler olusturuluyor....')
tablo()

gemiler=[]      # bos gemiler listesi olusturduk
gemi1=[]
gemi2=[]
gemi3=[]
gemi4=[]
gemi5=[]
gemi6=[]
gemi7=[]
gemi8=[]
# gemilerin kordinatlarini belirledik
# while ile 8 tane rastgele gemi urettirdik
gemi_sayisi=0
gemi_noktalari=[]   # gemi noktalarini bir listede toplayip cakisma olmasini onledik
while gemi_sayisi<=8:
    gemi_sayisi += 1
    #gemi1  (* * * *)
    if gemi1 not in gemiler:
        x=r.randint(1,10)
        y=r.randint(3,9)
        gemi1=[[x,y-2],[x,y-1],[x,y],[x,y+1]]
        gemiler.append(gemi1)
        for i in gemi1:                      # gemilerin cakismamasi icin butun noktalari bir yerde topladik.
            gemi_noktalari.append(i)          # sonraki gemileride buna gore olusturduk
    #gemi 2 (* * * *)
    elif gemi2 not in gemiler:
        anahtar = 1
        while anahtar == 1:     # while ile gemilerin noktalarinda cakisma oldugunda tekrar gemi olusturmada kullandik
            x = r.randint(3, 9)
            y = r.randint(1, 10)
            gemi2 = [[x - 2, y], [x - 1, y], [x, y], [x + 1, y]]
            for i in gemi2:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0     # while dongusunden cikmak icin kullandik
        gemiler.append(gemi2)   # 8 gemiye ulasmak icin olusan gemileri bir yerde topladik
        for i in gemi2:         # olusan gemi noktalarini for ile gemi_noktalari list ekledik
            gemi_noktalari.append(i)
    # gemi 3    (* * *)
    elif gemi3 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(1, 10)
            y = r.randint(2, 9)
            gemi3 = [[x, y - 1], [x, y], [x, y + 1]]
            for i in gemi3:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi3)
        for i in gemi3:
            gemi_noktalari.append(i)
    #gemi 4     (* * *)
    elif gemi4 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(2, 9)
            y = r.randint(1, 10)
            gemi4 = [[x - 1, y], [x, y], [x + 1, y]]
            for i in gemi4:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi4)
        for i in gemi4:
            gemi_noktalari.append(i)
    # gemi 5    (* *)
    elif gemi5 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(1, 10)
            y = r.randint(2, 10)
            gemi5 = [[x, y - 1], [x, y]]
            for i in gemi5:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi5)
        for i in gemi5:
            gemi_noktalari.append(i)
    # gemi 6    (* *)
    elif gemi6 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(1,9)
            y = r.randint(1, 10)
            gemi6 = [[x, y], [x + 1, y]]
            for i in gemi6:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi6)
        for i in gemi6:
            gemi_noktalari.append(i)
    # gemi 7    (*)
    elif gemi7 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(1, 10)
            y = r.randint(1, 10)
            gemi7 = [[x, y]]
            for i in gemi7:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi7)
        for i in gemi7:
            gemi_noktalari.append(i)
    # gemi 8    (*)
    elif gemi8 not in gemiler:
        anahtar = 1
        while anahtar == 1:
            x = r.randint(1, 10)
            y = r.randint(1, 10)
            gemi8 = [[x, y]]
            for i in gemi8:
                if i in gemi_noktalari:
                    break
            else:
                anahtar = 0
        gemiler.append(gemi8)
        for i in gemi8:
            gemi_noktalari.append(i)
gemi1_hamleler=[]
gemi2_hamleler=[]
gemi3_hamleler=[]
gemi4_hamleler=[]
gemi5_hamleler=[]
gemi6_hamleler=[]
gemi7_hamleler=[]
gemi8_hamleler=[]
#yapilan hamleleri toplamak icin bos yapilan hamleler listesi olusturduk
yapilan_hamleler = []
dogru_gemiler=[]
hak=15
while hak>0:
    try:        # try-except ile sayidan farkli deger girilmesini kontrol ettik
        print(f'>>>>>>>> {hak} . hakkiniz....basarilar') #kac hakki kaldigini bildirdik
        print('\n>>>>>>>>',8 - len(dogru_gemiler),' gemi kaldi <<<<<<<<<') #kac gemi kaldigini bildirdik
        # kullanicidan input ile kordinatlari aldik
        x = int(input('\nyukaridan asagiya "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))
        y = int(input('soldan sağa...... "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))

        if 1 <= x <= 10 and 1 <= y <= 10:       # girilen sayilarin 0 ile 11 arasinda olmasini kontrol ettik
            hamle = [x,y]                       # girilen kordinatlari listeye cevirdik
            if hamle in yapilan_hamleler:       # if ile yapilan hamle kontrolu yaptik
                print('\n!!!...UYARI...BU HAMLE DAHA ONCE YAPILDI \n')
                continue
            else:
                yapilan_hamleler.append(hamle)      # yapilan hamleleri listemizde ekledik
                tahta[x][y] = 'X'                   # 'X' isareti ile oyun tahtamizda yapilan hamleleri belirttik
# if'ler ile gemilere isabetetme durumlarini inceledik
                if hamle in gemi1:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi1_hamleler.append(hamle)
                    if len(gemi1_hamleler) == 4:
                        print('\n>>>>>>....Tebrikler...( * * * * ) 4 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi1)
                if hamle in gemi2:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi2_hamleler.append(hamle)
                    if len(gemi2_hamleler) == 4:
                        print('\n>>>>>>....Tebrikler...( * * * * ) 4 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi1)

                if hamle in gemi3:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi3_hamleler.append(hamle)
                    if len(gemi3_hamleler) == 3:
                        print('\n>>>>>>....Tebrikler...( * * * ) 3 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi3)
                if hamle in gemi4:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi4_hamleler.append(hamle)
                    if len(gemi4_hamleler) == 3:
                        print('\n>>>>>>....Tebrikler...( * * * ) 3 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi4)
                if hamle in gemi5:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi5_hamleler.append(hamle)
                    if len(gemi5_hamleler) == 2:
                        print('\n>>>>>>....Tebrikler...( * * ) 2 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi5)
                if hamle in gemi6:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi6_hamleler.append(hamle)
                    if len(gemi6_hamleler) == 2:
                        print('\n>>>>>>....Tebrikler...( * * ) 2 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi6)
                if hamle in gemi7:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi7_hamleler.append(hamle)
                    if len(gemi7_hamleler) == 1:
                        print('\n>>>>>>....Tebrikler...( * ) 1 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi7)
                if hamle in gemi8:
                    hak += 1
                    # gemilere isabet ettigini '*' isareti kullanarak belirledik
                    tahta[x][y] = '*'
                    yapilan_hamleler.append(hamle)
                    gemi8_hamleler.append(hamle)
                    if len(gemi8_hamleler) == 1:
                        print('\n>>>>>>....Tebrikler...( * ) 1 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                        # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                        dogru_gemiler.append(gemi8)
                time.sleep(5)       # 5 saniye bekleme koyduk
                tablo()     # fonksiyon ile oyun tahtamizi ekrana yazdirdik
                hak -= 1    # hakkimizi 1 azalttik
        else:
            print('\n!!!...UYARI..."1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz\n')
            continue
        if len(dogru_gemiler) == 8:  # dogru hamleler sayisi ile kazanma durumunu kontrol ettik
            print('\nTEBRIKLER OYUNU KAZANDINIZ')
            quit()
    except ValueError:
        print('\nLutfen "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz')
print(f'\n{hak} hak...hakkiniz bitti.....KAYBETTINIZ')

#oyun bittiginde butun gemileri oyun tahtasina yazdirdik
        #gemi1
tahta[gemi1[0][0]][gemi1[0][1]] = '*'
tahta[gemi1[1][0]][gemi1[1][1]] = '*'
tahta[gemi1[2][0]][gemi1[2][1]] = '*'
tahta[gemi1[3][0]][gemi1[3][1]] = '*'
        #gemi2
tahta[gemi2[0][0]][gemi2[0][1]] = '*'
tahta[gemi2[1][0]][gemi2[1][1]] = '*'
tahta[gemi2[2][0]][gemi2[2][1]] = '*'
tahta[gemi2[3][0]][gemi2[3][1]] = '*'
        #gemi3
tahta[gemi3[0][0]][gemi3[0][1]] = '*'
tahta[gemi3[1][0]][gemi3[1][1]] = '*'
tahta[gemi3[2][0]][gemi3[2][1]] = '*'
        #gemi4
tahta[gemi4[0][0]][gemi4[0][1]] = '*'
tahta[gemi4[1][0]][gemi4[1][1]] = '*'
tahta[gemi4[2][0]][gemi4[2][1]] = '*'
        #gemi5
tahta[gemi5[0][0]][gemi5[0][1]] = '*'
tahta[gemi5[1][0]][gemi5[1][1]] = '*'
        #gemi6
tahta[gemi6[0][0]][gemi6[0][1]] = '*'
tahta[gemi6[1][0]][gemi6[1][1]] = '*'
        #gemi7
tahta[gemi7[0][0]][gemi7[0][1]] = '*'
        #gemi8
tahta[gemi8[0][0]][gemi8[0][1]] = '*'

tablo()         #oyun bitince gemileri oyun tahtasina yazdirdik
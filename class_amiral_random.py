
import random
import time as zaman


#*******************OYUN TABLOSU CLASS I*********************************  
class amiral_oyun_tablosu():



    def __init__(self):

        self.sanal_tahta = [["---" for b in range ( 10 )] for a in range ( 10 )]

        self.koordinat_x_y = [(a , b) for b in range ( 10 ) for a in range ( 10 )]
        self.depo = []
        self.torba = []
        self.emi_yatay = []
        self.gemi_dikey = []
        self.kaclik_gemi = []
#********************************************************************************
    def gemi_hazirlama(self):


        self.gemi = random.randint ( 1 , 5 ) #KACLIK GEMI OLACAGINI AYARLAYAN RANDOM
        self.sec = random.randint ( 0 , 1 )  #DIKEY YATAY OLMA DURUMUNU AYARLAYAN RANDOM
        if self.sec == 0 :
            self.gemi_yatay = [[(a , b + c) for b in range ( self.gemi )] for a in range ( 10 ) for c in
                          range ( 10 - self.gemi + 1 )]
            return self.gemi_yatay
        if self.sec == 1 :
            self.gemi_dikey = [[(b + c , a) for b in range ( self.gemi )] for a in range ( 10 ) for c in
                          range ( 10 - self.gemi + 1 )]
            return self.gemi_dikey
#************************************************************************************
    def temizle(self,secime_git): #X DEGERLERININ CEVRESINI BOSALTAN FONKSIYON


        silme = []
        asagi_sil = [[((a + 1) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        yukari_sil = [[((a + 9) % 10 , b) for b in range ( 10 )] for a in range ( 10 )]
        sag_sil = [[(a , b + 1) for b in range ( 10 )] for a in range ( 10 )]
        sol_sil = [[(a , b - 1) for b in range ( 10 )] for a in range ( 10 )]
        for i in secime_git :

            if 0 < i[0] < 9 and i in self.koordinat_x_y :
                silme += [asagi_sil[i[0]][i[1]]]
                silme += [yukari_sil[i[0]][i[1]]]
            if 0 < i[1] < 9 and i in self.koordinat_x_y :
                silme += [sag_sil[i[0]][i[1]]]
                silme += [sol_sil[i[0]][i[1]]]
            if i[0] == 0 and i in self.koordinat_x_y :
                silme += [asagi_sil[i[0]][i[1]]]
            if i[0] == 9 and i in self.koordinat_x_y :
                silme += [yukari_sil[i[0]][i[1]]]
            if i[1] == 0 and i in self.koordinat_x_y :
                silme += [sag_sil[i[0]][i[1]]]
            if i[1] == 9 and i in self.koordinat_x_y :
                silme += [sol_sil[i[0]][i[1]]]

        silme.extend ( secime_git )


        for i in set ( silme ) :

            if i in self.koordinat_x_y :

                self.koordinat_x_y.remove ( i )

        return
#********************************************************************************
    def screen(self) :


        for i in self.depo :
            self.kaclik_gemi += [len ( i )]
            for yaz in i :
                self.sanal_tahta[yaz[0]][yaz[1]] = ('X').center ( 3 )

        print('\n'*3)
        for i in self.sanal_tahta :
            print ( ' ' * 40 , *i , '\n' )
#********************************************************************************
    def gemi_ekrani(self) :    #KAC ADET KACLIK GEMI OLDUGUNU GOSTEREN FONKSIYON
        print ( """
                            GEMILER(8 ADET)

    {} adet 5 lik  Ucak gemisi          {} adet 4 luk  Kruvazor

    {} adet 3 luk  Denizalti            {} adet 2 lik  mayin gemisi {} adet 1 lik  hucum bot
    """.format ( self.kaclik_gemi.count ( 5 ) , self.kaclik_gemi.count ( 4 ) , self.kaclik_gemi.count ( 3 ) ,
                          self.kaclik_gemi.count ( 2 ) , self.kaclik_gemi.count ( 1 ) ) ,'\n')


gemiadeti = 0
gemi_imalat=amiral_oyun_tablosu()
while gemiadeti < 8 :   #8 ADET GEMI YAPMA DONGUSU


    gemi_imalat.gemi_hazirlama()
    for i in gemi_imalat.gemi_hazirlama () :

        if set ( i ).issubset ( set ( gemi_imalat.koordinat_x_y ) ) :  # tahtanin icinde alt kume olarak varmi
            gemi_imalat.torba += [i]

    if gemi_imalat.torba != [] :
        secime_git = random.choice ( gemi_imalat.torba )
    gemi_imalat.torba = []
    gemi_imalat.depo.append ( secime_git )

    gemi_imalat.temizle ( secime_git )

    gemiadeti += 1

gemi_imalat.screen()



#*******************OYUN  CLASS I*********************************
class amiral_oyun():



    def __init__(self):
        self.bos = []
        self.tam_isabet = []
        self.hamle = 14
        self.tahta = [["---" for b in range ( 10 )] for a in range ( 10 )]
#*************************************************************************        
    def hedef(self,nisan) :

        isabet = list ( nisan )

        if self.tahta[int ( isabet[0] )][int ( isabet[1] )] == ('X').center ( 3 ) :
            print ( 'Hey... iyimisin buraya daha once ates ettin' )
            return

        else :

            if gemi_imalat.sanal_tahta[int ( isabet[0] )][int ( isabet[1] )] == ('X').center ( 3 ) :
                self.tam_isabet = [isabet]
                return self.tam_isabet
    # ****************************************************************************************
    #                       BOS ATISLAR ICIN FONKSIYON
    def iska(self,bosa) :
        global bos
        global hamle

        iska = list ( bosa )

        if self.tahta[int ( bosa[0] )][int ( bosa[1] )] == ('!!!').center ( 3 ) :
            print ( 'Hey... iyimisin buraya daha once ates ettin' )
            return

        else :

            if gemi_imalat.sanal_tahta[int ( iska[0] )][int ( iska[1] )] == ('---').center ( 3 ) :
                self.bos = [iska]
                self.hamle -= 1  #
                # Hamle sayisi bosa giderse 1 azalir
                return self.bos  # bos listesi fonksiyonun cagirildigi yere dondurulur

    # ****************************************************************************************
    # EKRANA YAZDIRMA FONKSIYONU
    def ekran(self) :
        gemi_imalat.gemi_ekrani()

        print ( ' ' * 30 , self.hamle + 1 , 'Hamleniz kaldi' , '\n' * 1 )  # hamle sayisi gosterme


        print ( '\n' , ' ' * 36 ,
                ' [Y] -->   [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}] [{}]'.format ( 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 ,
                                                                                        8 ,
                                                                                        9 ) , '\n' )
        sayac = 0
        for i in self.tahta :
            print ( ' ' * 38 , '[X][' , sayac , '] ' , *i , '\n' )
            sayac += 1

# ****************************************************************************************
oyun=amiral_oyun()
oyun.ekran ()

while True :
    # ***********************************************************************
    #      INPUT ALMA VE HATALARI DUZELTME

    oku = input ( '\n'"""Konum  xy (01) giriniz,
[cikis=Q]--> :""" )

    if oku.upper () == 'Q' :
        print ( 'oyundan cikiliyor............' )
        zaman.sleep ( 2 )
        break
    elif oku.isdigit () == False or len ( oku ) != 2 :
        print ( 'lutfen x ve y degerini xy (93) seklinde giriniz' )
        continue
    # *****************************************************************************

    elif oyun.hamle == 0 :

        print ( 'uzgunum ahbap yine iskaladin hamle hakkin kalmadi ne yazik ki kaybettin' )

        gemi_imalat.screen ()
        print ( '\n''Bu sefer olmadi bir dahakine bol sanslar byeee........' )

        zaman.sleep ( 2 )
        break
    # **********************************************************************************

    elif oyun.hedef ( oku ) ==oyun.tam_isabet :


        for x in oyun.tam_isabet :
            oyun.tahta[int ( x[0] )][int ( x[1] )] = gemi_imalat.sanal_tahta[int ( x[0] )][int ( x[1] )]
            print ( 'bravo hedefi 12 den vurdun ' )
            zaman.sleep(2)

        oyun.ekran ()

        if sum ( [oge.count ( ' X ' ) for satirlar in oyun.tahta for oge in satirlar] ) == \
                sum ( [oge.count ( ' X ' ) for satirlar in gemi_imalat.sanal_tahta for oge in satirlar] ) :
            print ( """
            **********************************************************
                         TEBRIKLER        KAZANDINIZ

            **********************************************************


            Game over.................................................
            """ )
            zaman.sleep ( 2 )
            break
        continue
    # ************************************************************************

    elif oyun.iska ( oku )==oyun.bos:

        for i in oyun.bos :
            oyun.tahta[int ( i[0] )][int ( i[1] )] = '!!!'.center ( 3 )
        print ( 'ne yazik ki iska gectin..' )
        zaman.sleep(2)
        oyun.ekran ()
        continue

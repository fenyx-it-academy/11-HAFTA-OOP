# coding=utf-8
import random
from time import sleep
class AmiralBattı:
    def __init__(self):
        self.satır_sozluk = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'K': 8, 'L': 9}

        self.oyuncu_tahta = [['A', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['B', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['C', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['D', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['E', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['F', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['G', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['H', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['K', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['L', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        self.toshiba_tahta = [['A', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['B', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['C', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['D', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['E', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['F', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['G', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['H', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['K', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                      ['L', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        self.oyuncu_gemiler = [['A', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['B', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['C', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['D', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['E', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['F', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['G', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['H', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['K', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                              ['L', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        self.toshiba_gemiler = [['A', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['B', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['C', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['D', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['E', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['F', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['G', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['H', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['K', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                               ['L', "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        self.gemiler = [['<', '=', '=', '>'],
                        ['<', '=', '=', '>'],
                        ['<', '=', '>'],
                        ['<', '=', '>'],
                        ['<', '>'],
                        ['<', '>'],
                        ['O'],
                        ['O']]

        self.oyuncu_isabet = 0
        # oyuncunun toplam yapabilecegi bos atis sayısı
        self.toshiba_isabet = 0
        # Bütün gemilerin vurulup-vurulmadığını kontrol eder
        self.atis=''
        self.satir = ''
        self.sutun=''
        self.konum_satir = ''
        self.konum_sutun=''
        self.kontrol=''
        self.gemi_ekran_oyuncu={}
        self.gemi_ekran_toshiba = {}
        self.atıs_list = []
        self.son_atıs=''
        self.sıra=''
        self.hamle_liste=[]

        for i in self.satır_sozluk.keys():
            for j in self.satır_sozluk.values():
                self.hamle_liste.append(i+str(j))
        # biligsayar icin hamle listesi olusturma

    def ekrana_yazdirma(self,veri,gemi_ekran,oyuncu_isim,oynama_sırası):
        # veri olarak girilecek listeyi ekrana yazdıran foksiyon
        print("\t".expandtabs(50), f'Oynama sırası={oynama_sırası}')
        print("\t".expandtabs(50), ' _ _ _ _ _ _ _ _ _ _')
        for i in veri:
            print("\t".expandtabs(50), end='')
            print(*i, '', sep='|')
        print("\t".expandtabs(50), ' 0 1 2 3 4 5 6 7 8 9')
        print("\t".expandtabs(53),f'{oyuncu_isim}-GEMİLER')
        print ("\t".expandtabs(40),*gemi_ekran.values(),sep=' ')

    def tahta_kontrol(self,tahta2):
        # Gemileri yerlestirilecek yerin bos oldup-olmadıgının kontrolu
        for j in range(len(self.i)):
            # 58.satırdaki i-ler gemilerdir. gemilerin uzunlugu boyunca dongu
            if tahta2[self.konum_satir][self.konum_sutun + j] != '_':
                # tahtadan random secilen bir noktadan itibaren
                # gemi karakter sayısınca tahtanın bos olup olmadıgının kontrolu
                self.konum_satir = random.randint(0, 9)
                self.konum_sutun = random.randint(1, 11 - len(self.i))
                # if bloguna girdiginde yani tahta,gemi karakterlerinin denk geldigi
                # yerler boyunca bos degilse random olarak yeni bir koordinat secilir
                self.kontrol = 0
                # donguden cıkmak icin kontrol degiskeni
                return
            else:
                self.kontrol = 1

    def gemi_yerlestirme(self,tahta2,gemi_ekran):
        for self.i in self.gemiler:
            #gemi listesinden herbir gemi icin dongu
            self.konum_satir=random.randint(0,9)
            self.konum_sutun=random.randint(1,11-len(self.i))
            #random satir ve sutun belirleme
            while True:
                self.tahta_kontrol(tahta2)
                #fonksiyon ile gemilerin yerlestirilecegi yerin uygunlugunun kontrolu
                if self.kontrol==1:
                    #foksiyon icinde kullanılan ve global yapılan kontrol degiskeni 1
                    #ise gemilerin icin random secilen koordinatlar uygundur aksi
                    #halde gemiler icin foksiyon ile yeni koordinat belirlenir.
                    break
                    #while dongusunden cıkılır
            for j in range(len(self.i)):
                #gemi uzunlugu kadar dongu
                tahta2[self.konum_satir][self.konum_sutun+j]=self.i[j]
                #tahta_gemiler listesine koorninat biligleriyle gemileri yerlestirme
                gemi_ekran[str(self.konum_satir+1) + str(self.konum_sutun+j-1)] = self.i[j]

    def oyuncu_hamle(self,tahta1,tahta2,gemi_ekran,isabetli_atis):
        # oyuncunun yaptıgı hamleleri isleyen fonksiyon
        while True:
            if self.sıra == 0:
                self.atis = input('Atışınızı yapınız.')
                # oyuncudan atis icin veri girisi
            else:
                self.toshiba_atıs()
                # bilgisayar atıs modulunun calıstırılması
            self.satir = self.atis[0].upper()
            # girilen verinin ilk karakteri satir degiskenine upper yapılıp atanır
            self.sutun = int(self.atis[1]) + 1
            # girilen verinin ikinci karakteri int yapılıp bir fazlası sutun degiskenine atnır
            # bu degerin bir artırılma sebebi tahtanın ilk sutununda harflerin yer almasıdır
            if len(self.atis) != 2 or self.atis[0].upper() not in self.satır_sozluk.keys() \
                    or self.atis[1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                # oyuncu uyugun olmayan bir veri girdiginde uyarı
                print('Yanlış veri girdiniz. Yeniden ', end='')
            elif tahta2[self.satır_sozluk[self.satir]][self.sutun] == '_':
                # tahta uzerinde koordinatları girilen yer bos ise
                tahta1[self.satır_sozluk[self.satir]][self.sutun] = 'X'
                tahta2[self.satır_sozluk[self.satir]][self.sutun] = 'X'
                # isabetsiz atis ifadesi 'X'in iki tahtaya da islenmesi
                break
            elif tahta1[self.satır_sozluk[self.satir]][self.sutun] in ['X', '+']:
                # oyuncu aynı yere atis yaparsa uyarı ver
                print('Aynı hedefe atış yaptınız. Yeniden ',end='')
            else:
                print('\t'*43,'İSABETLİ ATIŞ...')
                isabetli_atis += 1
                # isabetli atıs yapan oyuncunun sayacını bir artırma
                tahta1[self.satır_sozluk[self.satir]][self.sutun] = '+'
                tahta2[self.satır_sozluk[self.satir]][self.sutun] = '+'
                # yukardaki durumlar gecerli degilse isabetli bir atis vardır
                # isabetli atis uyarısı'+'nın tataya islenmesi
                if str(self.satır_sozluk[self.satir]+1)+str(self.sutun-1) in gemi_ekran.keys():
                    #yapılan hamle gemilere isabet edip-etmediginin kontrolu
                    gemi_ekran[str(self.satır_sozluk[self.satir]+1)+str(self.sutun-1)]='+'
                    #ekrana yazdırılan gemilerin isabet aldıgının gosterilmesi
                break

    def oyuncu(self,tahta1,tahta2,gemi_ekran,oyuncu_isim,oynama_sırası,isabetli_atis):
        self.ekrana_yazdirma(tahta1,gemi_ekran,oyuncu_isim,oynama_sırası)
        # ilk defa tahtanın ekrana yazdırılması
        self.oyuncu_hamle(tahta1, tahta2,gemi_ekran,isabetli_atis)
        # oyuncunun hamlesinin foksiyonla islenmesi
        sleep(1)
        print('\n' * 8)
        self.ekrana_yazdirma(tahta1,gemi_ekran,oyuncu_isim,oynama_sırası)

        if isabetli_atis == 20:
            print(f'{oynama_sırası} kazandı.')
            # toplam 20 hedefin vurulması durumunda oyundan cıkıs
            quit()

    def toshiba_atıs(self):
        for i in range(50):
            print('-',end='',sep='')
            sleep(0.03)
        print('>')
        # bilgisayar hamlesi belirten ekran suslemesi -------->
        if self.son_atıs!='':
            # bilgisayarın isabetli atısı bu degiskene atanır. yani bu degisken veri varsa bloga girer
            self.satir=self.son_atıs[0]
            self.sutun=int(self.son_atıs[1])+1
            # satır ve sutun icin son_atıstan veri alma
            for i in range(1,4):
                # vurulan hedefin 3br sag ve sol tarafını kontrol etme
                if self.sutun+i<11 and self.toshiba_gemiler[self.satır_sozluk[self.satir]][self.sutun+i] in ['=','>']:
                    # tahtanın dısına tasmaması icin kontrol ve
                    #  3 br'e kadar sag tarafta hedefin devaminın olup-olmadıgının kontrolu
                    self.atis=(self.satir)+str(self.sutun+i-1)
                    # hedefin devamı yakalanırsa atıs degiskenine verinin girilmesi
                    self.son_atıs=self.atis
                    # yeni isabetli atısın son_atıs degiskenine atanması
                    break

                elif self.sutun-i>0 and self.toshiba_gemiler[self.satır_sozluk[self.satir]][self.sutun-i] in ['<','=']:
                    # tahtanın dısına tasmaması icin kontrol ve
                    #  3 br'e kadar sol tarafta hedefin devaminın olup-olmadıgının kontrolu
                    self.atis = (self.satir) + str(self.sutun-i-1)
                    self.son_atıs = self.atis
                    break
                else:
                    self.son_atıs=''
                    # atıs isabetli degilse son_atıs degiskenideki veriyi kaldırma
        else:
            # son atıs isabetli degilse yukardaki bloga giremeyeceginden atıs listesinden
            # random yeni bir atıs yapılır
            self.atis =random.choice(self.hamle_liste)
            self.hamle_liste.remove(self.atis)
            if self.toshiba_gemiler[self.satır_sozluk[self.atis[0]]][int(self.atis[1])+1] in ['<','=','>']:
                self.son_atıs=self.atis
            # yeni yapılan atıs isabetli ise bu atıs son_atıs degiskenine atanır
            else:
                self.son_atıs=''
            # yeni atıs isabetsiz ise son_atıs degiskeni bos tutulur

    def calıstır(self):
        self.gemi_yerlestirme(self.oyuncu_gemiler,self.gemi_ekran_oyuncu)
        self.gemi_yerlestirme(self.toshiba_gemiler,self.gemi_ekran_toshiba)
        # oyuncu ve bilgisayar icin gemileri tahaya yerlestiren modul calıstırılır
        self.sıra=random.randint(0,1)
        # ilk oyun sırası random belirlenir
        while True:
            if self.sıra==0:
                self.oyuncu(self.oyuncu_tahta,self.oyuncu_gemiler,self.gemi_ekran_oyuncu,'TOSHIBA','OYUNCU',self.oyuncu_isabet)
                # oyuncu icin oyun modulu calıstırılır
                self.sıra=1
                sleep(3)
            else:
                self.oyuncu(self.toshiba_tahta, self.toshiba_gemiler,self.gemi_ekran_toshiba,'OYUNCU','TOSHIBA',self.toshiba_isabet)
                # bilgissyar icin oyun modulu calıstırılır
                self.sıra=0
                sleep(3)
            print('\n' * 8)

yenioyun=AmiralBattı()
yenioyun.calıstır()
# class icin instance yapılıp oyun calıstırılır
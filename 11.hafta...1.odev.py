print('b.')
import random as r
class Oyun():

    def __init__(self):
        self.Giris_yazisi()
        self.tahta = [[' ', " 1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                      ['1 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['2 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['3 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['4 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['5 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['6 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['7 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['8 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['9 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                      ['10', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        # bos gemiler listesi olusturduk
        self.gemiler = []
        self.gemi1 = []
        self.gemi2 = []
        self.gemi3 = []
        self.gemi4 = []
        self.gemi5 = []
        self.gemi6 = []
        self.gemi7 = []
        self.gemi8 = []
        self.gemi1_hamleler = []
        self.gemi2_hamleler = []
        self.gemi3_hamleler = []
        self.gemi4_hamleler = []
        self.gemi5_hamleler = []
        self.gemi6_hamleler = []
        self.gemi7_hamleler = []
        self.gemi8_hamleler = []
        # yapilan hamleleri toplamak icin bos yapilan hamleler listesi olusturduk
        self.yapilan_hamleler = []
        self.dogru_gemiler = []
        self.gemi_sayisi = 0
        self.gemi_noktalari = []  # gemi noktalarini bir listede toplayip cakisma olmasini onledik
        #tahta olusturma...gemi olusturma metotlarimizi basta calistirdik
        self.tahta_olusturma()
        self.gemi_olustur()
        self.oyun_start()   # oyuna baslama metodumuz

    def Giris_yazisi(self):
        print('>>>>>>>>>>>>>>>>>>>>...Amiral batti oyununa HOSGELDINIZ...s<<<<<<<<<<<<<<<<<<<<\n'
              '>>>>>>>>>>>>>>>>>>>>>>>>>>>>.......3.0.......<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'
              '2 tane 4 birim \t( * * * * )\n2 tane 3 birim\t(  * * *  )\n'
              '2 tane 2 birim \t(   * *   )\n2 tane 1 birim \t(    *    )  sekillerinden olusan 8 tane gemi vardir \n'
              'tablodaki dogru kordinatlari girerek 15 tahminde bulmaya calisiniz...Basarilar')

    def tahta_olusturma(self):
        self.tahta = [[' ', " 1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
                 ['1 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['2 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['3 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['4 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['5 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['6 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['7 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['8 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['9 ', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
                 ['10', "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]
        print('-' * 70)
        for i in self.tahta:
            print(*i)
        print("-" * 70, '\n( dogru hamleler "*", yanlis hamleler "X" isareti ile belirtilmistir )\n', "-" * 70)
        print('>>>>>>  Lutfen bekleyiniz gemiler olusturuluyor....')

    def tahta_yazi(self):       #tahtaya hamle yazdirma metodu
        print(f'>>>>>>>> {self.hak} . hakkiniz....basarilar')  # kac hakki kaldigini bildirdik
        print('\n>>>>>>>>', 8 - len(self.dogru_gemiler), ' gemi kaldi <<<<<<<<<')  # kac gemi kaldigini bildirdik
        # kullanicidan input ile kordinatlari aldik
        self.x = int(input('\nyukaridan asagiya "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))
        self.y = int(input('soldan sağa...... "1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz : '))
        self.hamle = [self.x, self.y]  # girilen kordinatlari listeye cevirdik
        self.tahta[self.x][self.y] = 'X'


    def gemi_olustur(self):     # gemi olusturma metodu
        # gemilerin kordinatlarini belirledik
        # while ile 8 tane rastgele gemi urettirdik
        while self.gemi_sayisi <= 8:
            self.gemi_sayisi += 1
            # gemi1  (* * * *)
            if self.gemi1 not in self.gemiler:
                x = r.randint(1, 10)
                y = r.randint(3, 9)
                self.gemi1 = [[x, y - 2], [x, y - 1], [x, y], [x, y + 1]]
                self.gemiler.append(self.gemi1)
                for i in self.gemi1:  # gemilerin cakismamasi icin butun noktalari bir yerde topladik.
                    self.gemi_noktalari.append(i)  # sonraki gemileride buna gore olusturduk
            # gemi 2 (* * * *)
            elif self.gemi2 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:#while ile gemilerin noktalarinda cakisma oldugunda tekrar gemi olusturmada kullandik
                    x = r.randint(3, 9)
                    y = r.randint(1, 10)
                    self.gemi2 = [[x - 2, y], [x - 1, y], [x, y], [x + 1, y]]
                    for i in self.gemi2:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0  # while dongusunden cikmak icin kullandik
                self.gemiler.append(self.gemi2)  # 8 gemiye ulasmak icin olusan gemileri bir yerde topladik
                for i in self.gemi2:  # olusan gemi noktalarini for ile gemi_noktalari list ekledik
                    self.gemi_noktalari.append(i)
            # gemi 3    (* * *)

            elif self.gemi3 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(1, 10)
                    y = r.randint(2, 9)
                    self.gemi3 = [[x, y - 1], [x, y], [x, y + 1]]
                    for i in self.gemi3:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi3)
                for i in self.gemi3:
                    self.gemi_noktalari.append(i)
            # gemi 4     (* * *)
            elif self.gemi4 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(2, 9)
                    y = r.randint(1, 10)
                    self.gemi4 = [[x - 1, y], [x, y], [x + 1, y]]
                    for i in self.gemi4:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi4)
                for i in self.gemi4:
                    self.gemi_noktalari.append(i)
            # gemi 5    (* *)
            elif self.gemi5 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(1, 10)
                    y = r.randint(2, 10)
                    self.gemi5 = [[x, y - 1], [x, y]]
                    for i in self.gemi5:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi5)
                for i in self.gemi5:
                    self.gemi_noktalari.append(i)
            # gemi 6    (* *)
            elif self.gemi6 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(1, 9)
                    y = r.randint(1, 10)
                    self.gemi6 = [[x, y], [x + 1, y]]
                    for i in self.gemi6:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi6)
                for i in self.gemi6:
                    self.gemi_noktalari.append(i)
            # gemi 7    (*)
            elif self.gemi7 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(1, 10)
                    y = r.randint(1, 10)
                    self.gemi7 = [[x, y]]
                    for i in self.gemi7:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi7)
                for i in self.gemi7:
                    self.gemi_noktalari.append(i)
            # gemi 8    (*)
            elif self.gemi8 not in self.gemiler:
                anahtar = 1
                while anahtar == 1:
                    x = r.randint(1, 10)
                    y = r.randint(1, 10)
                    self.gemi8 = [[x, y]]
                    for i in self.gemi8:
                        if i in self.gemi_noktalari:
                            break
                    else:
                        anahtar = 0
                self.gemiler.append(self.gemi8)
                for i in self.gemi8:
                    self.gemi_noktalari.append(i)
        print(self.gemi2)

    def oyun_start(self):   #oyuna baslama metodu
        self.hak = 15
        while self.hak > 0:
            self.tahta_yazi()   #tahtaya yazi yazma metodumuzu cagirdik
            if 1 <= self.x <= 10 and 1 <= self.y <= 10:   # girilen sayilarin 0 ile 11 arasinda olmasini kontrol ettik
                self.hamle = [self.x, self.y]               # girilen kordinatlari listeye cevirdik
                if self.hamle in self.yapilan_hamleler:     # if ile yapilan self.hamle kontrolu yaptik
                    print('\n!!!...UYARI...BU HAMLE DAHA ONCE YAPILDI \n')
                    continue
                else:
                    self.yapilan_hamleler.append(self.hamle)  # yapilan hamleleri listemizde ekledik
                    self.tahta[self.x][self.y] = 'X'  # 'X' isareti ile oyun tahtamizda yapilan hamleleri belirttik
                    # if'ler ile gemilere isabetetme durumlarini inceledik
                    if self.hamle in self.gemi1:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi1_hamleler.append(self.hamle)
                        if len(self.gemi1_hamleler) == 4:
                            print(
                                '\n>>>>>>....Tebrikler...( * * * * ) 4 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                            # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi1)

                    if self.hamle in self.gemi2:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi2_hamleler.append(self.hamle)
                        if len(self.gemi2_hamleler) == 4:
                            print(
                                '\n>>>>>>....Tebrikler...( * * * * ) 4 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                            # gemiyi tamamen bulunca dogru_gemiler list. ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi2)

                    if self.hamle in self.gemi3:
                        self.hak += 1

                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi3_hamleler.append(self.hamle)
                        if len(self.gemi3_hamleler) == 3:
                            print('\n>>>>>>....Tebrikler...( * * * ) 3 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi3)
                    if self.hamle in self.gemi4:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi4_hamleler.append(self.hamle)
                        if len(self.gemi4_hamleler) == 3:
                            print('\n>>>>>>....Tebrikler...( * * * ) 3 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi4)
                    if self.hamle in self.gemi5:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi5_hamleler.append(self.hamle)
                        if len(self.gemi5_hamleler) == 2:
                            print('\n>>>>>>....Tebrikler...( * * ) 2 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi5)
                    if self.hamle in self.gemi6:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi6_hamleler.append(self.hamle)
                        if len(self.gemi6_hamleler) == 2:
                            print('\n>>>>>>....Tebrikler...( * * ) 2 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi6)
                    if self.hamle in self.gemi7:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi7_hamleler.append(self.hamle)
                        if len(self.gemi7_hamleler) == 1:
                            print('\n>>>>>>....Tebrikler...( * ) 1 birimlik 1.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi7)
                    if self.hamle in self.gemi8:
                        self.hak += 1
                        # gemilere isabet ettigini '*' isareti kullanarak belirledik
                        self.tahta[self.x][self.y] = '*'
                        self.yapilan_hamleler.append(self.hamle)
                        self.gemi8_hamleler.append(self.hamle)
                        if len(self.gemi8_hamleler) == 1:
                            print('\n>>>>>>....Tebrikler...( * ) 1 birimlik 2.gemiyi buldunuz.......<<<<<<<\n')
                            # dogru hamleleri listemize ekledik oyunu kazanma durumunu bulmak icin
                            self.dogru_gemiler.append(self.gemi8)
                    self.hak -= 1  # hakkimizi 1 azalttik
                    for i in self.tahta:
                        print(*i)
            else:
                print('\n!!!...UYARI..."1,2,3,4,5,6,7,8,9,10" arasindan bir sayi giriniz\n')
                continue
            if len(self.dogru_gemiler) == 8:  # dogru hamleler sayisi ile kazanma durumunu kontrol ettik
                print('\nTEBRIKLER OYUNU KAZANDINIZ')
                quit()
        print(f'\n{self.hak} self.hak...hakkiniz bitti.....KAYBETTINIZ')

oyun1=Oyun()

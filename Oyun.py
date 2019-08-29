
import random
import time
class Oyun():
    def bilgi(self):
        print("""Amiral Batti Oyununa Hosgeldiniz...
			Tabloda;
			4 birimlik 2 gemi,
			3 birimlik 2 gemi,
			2 birimlik 2 gemi ve
			1 birimlik 2 gemi bulunmaktadir. 
			Hedefleri harf ve sayilari kullanarak secebilirsiniz.
			15 deneme hakkiniz vardir.
			Her yanlis hedefte hakkiniz 1 azalmaktadir..
			Basarilar...""")
    def gemileriYerlestir_bilgi(self):
        print("Tablonuza,\n4 birimlik 2 gemi,\n3 birimlik 2 gemi,\n2 birimlik 2 gemi ve\n1 birimlik 2 gemi yerlestirmeniz gerekiyor. \nSira ile istediginiz Yonu (Yatay icin Y, Dikey icin D),\nSonra satir ve sutun degerlerini giriniz.")

class Oyuncu():
    hak = 15
    vurulan_gemi=0
    gemiler = [4, 3, 2, 1]
    sutun_dic = {"A": 1, "B": 2, "C": 3, "D": 4,"E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
    
    def __init__(self, hak=15, gemiler=[4, 3, 2, 1],tablo=[],tablo2=[]):
        self.hak = hak
        self.gemiler = gemiler
        self.tablo = [
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ["A", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["B", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["C", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["D", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["E", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["F", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["G", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["H", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["I", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ["J", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.tablo2 = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            ["A", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["B", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["C", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["D", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["E", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["F", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["G", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["H", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["I", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ["J", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def tablo_goster(self,tablo):
        for i in tablo:
            print("\t".expandtabs(30), *i, end="\n")

    def random_gemiyerlestir(self, birimSayisi, gemiSayisi):
        # 2 tane istenilen birimde olusturmasi icin for dongusu kurduk
        for i in range(gemiSayisi):
            # yatay dikey mi olacagini rastgele sectik
            rastgele_yatay_dikey = random.choice(["yatay", "dikey"])
            if rastgele_yatay_dikey == "yatay":  # yataysa
                while True:
                    kontrol = 0
                    rastgele = random.sample(self.tablo2[1:], 1)
                    satirindex = self.tablo2.index(rastgele[0])  
                    sutunindex = random.randint(1, len(self.tablo2) - birimSayisi)
                    for x in range(birimSayisi):
                        if self.tablo2[satirindex][sutunindex+x] == 0:
                            kontrol += 1
                    if kontrol == birimSayisi:
                        for y in range(birimSayisi):
                            self.tablo2[satirindex][sutunindex+y] = 1
                        break                      
                    else:
                        continue
            else:    # dikeyse
                while True:
                    kontrol = 0
                    rastgele = random.sample(
                        self.tablo2[1:(len(self.tablo2)-birimSayisi)+1], 1)
                    satirindex = self.tablo2.index(
                        rastgele[0]) 
                    sutunindex = random.randint(1, 10)
                    for x in range(birimSayisi):
                        if self.tablo2[satirindex+x][sutunindex] == 0:
                            kontrol += 1
                    if kontrol == birimSayisi:
                        for y in range(birimSayisi):
                            self.tablo2[satirindex+y][sutunindex] = 1
                        break
                    else:
                        continue

    def kontroll(self):
        kontrol = [x for i in self.tablo for x in i if x == "+"]
        return len(kontrol)

    def cozum_tablosu(self,oyuncu):
        print(oyuncu, " Cozum Tablosu")
        liste = []
        for satir in self.tablo2[1:]:
            satir2 = ["+" if item == 1 else item for item in satir]
            liste += [satir2]

        for x in liste:
            print("\t".expandtabs(30), *x, end="\n"*2)


            
    def gemileriYerlestir(self, birimSayisi, gemiSayisi,ihtimaller=[]):
        # 2 tane istenilen birimde olusturmasi icin for dongusu kurduk
        
        for i in range(1,gemiSayisi+1):
            if birimSayisi==1:
                konum="Y"
            else:
                a=birimSayisi,"birimlik icin Geminin konumu seciniz: (Y/D)"
                konum=input(a).upper()            
            if konum == "Y":  # yataysa
                while True:
                    kontrol = 0
                    try:
                        a=birimSayisi,"lik ",i, ". gemi icin satir seciniz: (1-10)"
                        b=birimSayisi,"lik ",i,".gemi  icin sutun seciniz: (A-J)"
                        satirindex=int(input(a))
                        sutunindex=input(b).upper()
                        sutunindex=self.sutun_dic[sutunindex]
                        for x in range(birimSayisi):
                            if self.tablo2[sutunindex][satirindex+x] == 0:
                                kontrol += 1
                        if kontrol == birimSayisi:
                            for y in range(birimSayisi):
                                self.tablo2[sutunindex][satirindex+y] = 1
                            self.tablo_goster(self.tablo2)
                            break 
                    except:
                        print("Yanlis giris yapildi. Tekrar deneyiniz..")
                        continue
                    else:
                        continue
            else:    # dikeyse
                while True:
                    kontrol = 0
                    try:
                        a=birimSayisi,"lik ",i, ". gemi icin satir seciniz: (1-10)" # Input tek parametre aldigi icin degiskene atadik
                        b=birimSayisi,"lik ",i,".gemi  icin sutun seciniz: (A-J)"  
                        satirindex=int(input(a))
                        sutunindex=input(b).upper()
                        sutunindex=self.sutun_dic[sutunindex]
                        for x in range(birimSayisi):
                            if self.tablo2[sutunindex+x][satirindex] == 0:
                                kontrol += 1
                        if kontrol == birimSayisi:
                            for y in range(birimSayisi):
                                self.tablo2[sutunindex+y][satirindex] = 1
                            self.tablo_goster(self.tablo2)
                            break 
                    except:
                        print("Yanlis giris yapildi. Tekrar deneyiniz..")
                        continue
                    else:
                        continue

    def ihtimaller(self,satir,sutun):
        if satir<10 and sutun<10 and satir>1 and sutun>1:
            ihtimaller=[[sutun,satir+1],[sutun,satir-1],[sutun+1,satir],[sutun-1,satir]]
        elif satir==10 and sutun==10:
            ihtimaller=[[sutun,satir-1],[sutun-1,satir]]
        elif satir==1 and sutun==1:
            ihtimaller=[[sutun,satir+1],[sutun+1,satir]]
        elif satir==1 and sutun!=1:
            ihtimaller=[[sutun,satir+1],[sutun+1,satir],[sutun-1,satir]]
        elif satir!=1 and sutun==1:
            ihtimaller=[[sutun,satir-1],[sutun+1,satir],[sutun,satir+1]]
        elif sutun==10 and satir!=10:
            ihtimaller=[[sutun,satir+1],[sutun,satir-1],[sutun-1,satir]]
        elif satir==10 and sutun!=10:
            ihtimaller=[[sutun,satir-1],[sutun+1,satir],[sutun-1,satir]]
        else:
            ihtimaller=[]
        return ihtimaller
        
    

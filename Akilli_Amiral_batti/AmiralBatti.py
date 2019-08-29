class Gemi:
    import random
    gemiler=[]
    tablo = [["O" for i in range(0, 10)] for j in range(0, 10)]
    tahta = [(a, b) for a in range(10) for b in range(10)]
    def random_gemi_bulma(self,gemi, adet):
        import random
        tahmin = []
        yerlesim = []
        for i in range(adet):
            for i in gemi:
                if set(i).issubset(set(self.tahta)):
                    tahmin += [i]
            if tahmin != []:
                tahmin = random.choice(tahmin)
                for a in tahmin:
                    self.tahta.remove(a)
                yerlesim += [tahmin]
                tahmin = []
        return yerlesim

    def gemi_kordinatlari(self,uzunluk):
        koordinatlar = []
        for i in range(10 - uzunluk + 1):
            for j in range(10):
                gecici_yatay = []
                gecici_dikey = []
                for k in range(uzunluk):
                    k = k + i
                    gecici_yatay += [(j, k)]
                    gecici_dikey += [(k, j)]
                koordinatlar += [gecici_yatay]
                koordinatlar += [gecici_dikey]
        return koordinatlar

    def gemi_olusturma(self):
        gemiler = []
        import random
        gemiler += [self.random_gemi_bulma(self.gemi_kordinatlari(4),2)]
        gemiler += [self.random_gemi_bulma(self.gemi_kordinatlari(3),2)]
        gemiler+=[self.random_gemi_bulma(self.gemi_kordinatlari(2), 2)]
        gemiler += [self.random_gemi_bulma(self.gemi_kordinatlari(1),2)]
        return gemiler

    def gemi_batirma(self,gemi,x):
        for i in gemi:
            for j in i:
                for k in j:
                    if list(k) == [x[0], x[1]]:
                        print(j)
                        return j  # gonderilen kordinatlar listede varsa gemiye rastgelmistir.ve geminin kordinatlari donulur
        return 1

    def gemiyi_goster(self,a):
        for i in a:
            i = list(i)
            self.tablo[i[0]][i[1]] = "X"  # gonderilen kordinatlardaki harfler X ile degistirilir
        for i in self.tablo:
            print("                      ", " ".join(i))

    def bosu_goster(self,x):
        self.tablo[x[0]][
            x[1]] = "B"  # gonderilen kordinatlardaki yerler B ile degistirilir. Alanin bos oldugu anlamina gelir
        for i in self.tablo:
            print("                      ", " ".join(i))
import random
class songlist(object):
    def __init__(self):
        self.song=[]
    def songlistreset(self):  #liste sifirlama
        self.song.clear()

    def songshow(self):      #sarki listesini goruntule
        print(self.song)

    def songclear(self,songs): #bir sarki silme
        self.songs=songs
        if self.songs in self.song:
            self.song.remove(self.songs)
        else:
            print("silmek istediginiz {} sarki listede yoktur ".format(self.songs))


    def songadd(self,songs):  #bir sarki ekleme
        self.songs=songs
        if self.songs in self.song:
            print("Aradiginiz {} sarki zaten listede vardir:".format(self.songs))
        else:
            self.song.append(self.songs)

    def songsearch(self,songs): #sarki arama
        self.songs=songs
        if self.songs in self.song:
            print("Aradiginiz {} sarki listede vardir:".format(self.songs))
        else:
            print("aradiginiz {} sarki listede yoktur ".format(self.songs))

    def nextsongplay(self,songs): # sonraki parcayi cal
        self.songs=songs
        print("Su anda {} sarkiyi dinlemeye basladiniz: ".format(self.songs))


    def lastsongplay(self,songs): # onceki parcayi cal
        self.songs=songs
        print(" Su anda {} sarkiyi dinlemeye basladiniz: ".format(self.songs))

    def mixsongplay(self):  #karisik cal
        sayi=len(self.song)
        if sayi==0:
            print("Suan listede hic sarki bulunmamaktadir")
        else:
            return print("Su anda {} sarkiyi dinliyorsunuz".format(random.choice(self.song)))


def sorgu():
    sorgu=input("""          sarki listesini sifirlamak icin: 1
     Sarki listesini goruntulemek  icin:             2
     Herhangi bir sarki silmek icin:                 3
     Sarki eklemek icin:                             4
     Sarki aramak acin:                              5
     Bir sonraki sarkiyi calmak icin:                6
     Bir onceki sarkiyi calmak icin:                 7
     Rastgele bir sarki calmak icin:                 8
     Cikmak icin:                                    9
     basiniz""")
    return sorgu

songlist1=songlist()
while True:
    sorguu=sorgu()
    if sorguu=="1":
        songlist1.songlistreset()
    elif sorguu=="2":
        songlist1.songshow()
    elif sorguu=="3":
        songs = input("silmek istediginiz sarkiyi giriniz: ")
        songlist1.songclear(songs)
    elif sorguu=="4":
        songs=input("Eklemek istediginiz sarkinin ismini giriniz")
        songlist1.songadd(songs)
    elif sorguu=="5":
        songs=input("HAngi sarkiyi aramak istediginizi seciniz")
        songlist1.songsearch(songs)

    elif sorguu=="6":
        songlist1.songshow()
        choose = input("Listedeki suan hangi sarkiyi dinlediginizi seciniz")
        try:
            songs = songlist1.song[songlist1.song.index(choose) + 1]
        except IndexError:
            songs=songlist1.song[0]
        songlist1.nextsongplay(songs)
    elif sorguu=="7":
        songlist1.songshow()
        choose = input("Listedeki suan hangi sarkiyi dinlediginizi seciniz")
        try:
            songs = songlist1.song[songlist1.song.index(choose) -1 ]
        except IndexError:
            songs=songlist1.song[-1]
        songlist1.nextsongplay(songs)
    elif sorguu=="8":
        songlist1.mixsongplay()
    elif sorguu=="9":
        quit()

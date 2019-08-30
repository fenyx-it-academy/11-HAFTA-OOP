# Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir song listesi  olusturun.
# Class methods olarak song listesini sifirlama, +listeyi goruntuleme, song ekleme, song silme,
# sonraki parcayi cal, onceki parcayi cal, +karisik cal ozelliklerini ekleyin.
import time as zaman
import random as  rastgele

class Playplay():

    def __init__(self, songs = []):
        self.songs = songs
        self. att =   1
        self.ses = 75
        self.calansong =""

################################################################
#song ekle
    def songEkle(self,song):
        self.songs.append(song)

################################################################
#song listesi
    def songListesi(self):
        print(self.songs)

################################################################
#song seç
    def songSec(self):
        sayac= 1
        for i in self.songs:
            print("{}.{}".format(sayac,i))
            sayac +=1
        sel=int(input("Enter song number: "))
        print("Song is changing")
        zaman.sleep(0.5)
        self.calansong=self.songs[sel -1]

################################################################
#rastgele song
    def rastgelesong(self):
        rastgele_sayi = rastgele.randint(0,len(self.songs))
        self.calansong = self.songs[rastgele_sayi]

################################################################
#kapat
    def shutdown(self):
        print("Mini Music Player is shutting down...")
        zaman.sleep(1)
        print("Goodbye!!")
        self.att= 0

################################################################
#song sil
    def songSil(self):
        sel= int(input("Enter the number of song to delete: "))
        self.songs.pop(sel-1)

################################################################
#liste sil
    def songListesil(self):
        print("Clearing list..")
        zaman.sleep(1)
        self.songs.clear()
        if not self.songListesi:
            self.calansong.clear()
        zaman.sleep(1)
################################################################
# ses arttır
    def sesArttir(self):
        if (self.ses >= 100):
            pass
        else:
            print("Vol increasing!")
            zaman.sleep(0.5)
            self.ses += 5
            print("Volume increased, vol is :{}".format(self.ses))

################################################################
# ses azalt
    def sesAzalt(self):
        if (self.ses <= 0):
            pass
        else:
            print("Vol decreasing!")
            zaman.sleep(2)
            self.ses -= 5
            print("Volume decreased, vol is :{}".format(self.ses))

################################################################
    #def sonrakisong(self):

################################################################
    #def oncekisong(self):

################################################################
    def menu(self):
        print(f"""___________ M e n ü ___________
Now playing.{self.calansong}
___________ ~ ~ ~ ~ ___________
1»Select    2»Random Sel   
3»Previous  4»Next   
5»Add       6»Delete
7»Del list  8»Vol +     
9»Vol -     0»Off""")


casa1 =Playplay(songs=["Bella Caio"])
print("     *Mini Music Player*")
while casa1.att:
    casa1.menu()
    sel=int(input("*Selection* "))
    if (sel==1):
        casa1.songSec()
    elif (sel == 2):
        casa1.rastgelesong()
    elif (sel == 3):
        casa1.sonrakiparcayical()
    elif (sel == 4):
        casa1.oncekiparcayical()
    elif (sel == 5):
        song=input("Type your song: ")
        casa1.songEkle(song)
    elif (sel == 6):
        casa1.songSil()
    elif (sel == 7):
        casa1.songListesil()
    elif (sel == 8):
        casa1.sesArttir()
    elif (sel == 9):
        casa1.sesAzalt()
    else:
       casa1.shutdown()

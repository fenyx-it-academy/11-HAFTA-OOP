# Odev 3: Bir muzik calar objesi yapmanizi istiyoruz. Class attribute olarak bos bir sarki listesi olusturun.
# Class methods olarak sarki listesini sifirlama, listeyi goruntuleme, sarki ekleme, sarki silme,
# sonraki parcayi cal, onceki parcayi cal, karisik cal ozelliklerini ekleyin.
import random
class MusicPlayer():

    def __init__(self,playlist={}, add={}):
        self.playlist = playlist
        self.add=add

    def delete_All(self):
        self.playlist.clear()

    def show_List(self):
        for i in self.playlist.items():
            print(*i)

    def add_song(self, add_song=""):
        self.singer = input("Please enter The singer You Add: ")
        self.song = input("Please enter song you Add: ")
        self.add[self.singer] = self.song
        self.playlist.update(self.add)
        print(self.playlist)

    def delete_list(self):
        self.singer = input("Please enter The Singer You Delete: ")
        if self.singer in self.playlist:
            self.playlist.pop(self.singer)
            print(self.playlist)
        else:
            print("The Singer You Delete Is not in the List")

    def random_play(self):
        print(random.choice(list(self.playlist.items())))

    """def next_song(self):
            for i in range(1,len(self.playlist)):
                if i ==(list(self.playlist.items())[0]):
                        print(list(self.playlist.items())[i])
            i+=1
            self.newlist = list()
            for i in self.playlist.keys():
                self.newlist.append(i)
            print(self.newlist.index([0]))
            self.newlist=(self.newlist.index([0,1,-1]))
            siradaki parcayi calmak ile ilgili bunu yapmaya calistim ama beceremedim. Listerdeki elemanlri sifirdan 
            baslatip her seferinde liste elemaninin '1' artiramadim:(
    """


list1 = MusicPlayer()

print("""Welcome to the Music Application:
    1-Clear The Music List
    2-Show The Music List
    3-Add a Song To The Music List
    4-Delete a Song From Music List
    5-Rondom Play a Song From Music List
    0-Quit      
    """)

while True:

    answer = input("Please make your choice:  ")
    if answer == "1":
        list1.delete_All()

    elif answer == "2":
        list1.show_List()

    elif answer == "3":
        list1.add_song()

    elif answer == "4":
        list1.delete_list()

    elif answer == "5":
        list1.random_play()

    elif answer == "0":
        break

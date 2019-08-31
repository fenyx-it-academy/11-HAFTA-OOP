####11.HAFTA 3. ODEV Bir muzik calar objesi yapmanizi istiyoruz.####

import random
class Musicplayer():
    songs=["say my name","loco","smack that","in my mind","day by day"]

    def clear_the_list(self):
        self.songs.clear()
    def view_the_list(self):
        for i in self.songs:
            print(i)
    def add_track(self,add_a_track):
        self.songs.append(add_a_track)
        print("Track is added in your list")
    def remove_track(self,remove_a_track):
        for i in self.songs:
            if remove_a_track==i:
                a=self.songs.index(i)
                self.songs.pop(a)
        else:
            print(remove_a_track,"The track is not in your list.")
    def previous_track(self,previous_song):
        for i in self.songs:
            if previous_song == i:
                a = self.songs.index(i)
                print("Playing...",self.songs[a-1])
    def next_track(self,next_song):
        for i in self.songs:
            if next_song == i:
                a = self.songs.index(i)
                print("Playing...", self.songs[a + 1])
    def play_random(self):
        randomm =random.choice(self.songs)
        print("Playing...",randomm)
playlist=Musicplayer()
while True:
    print("""Music Player\n                   
    Menu\n
    1 Clear the list\n
    2 View the list\n
    3 Add a track\n
    4 Remove a track\n
    5 Next track\n
    6 Previous track\n
    7 Random\n
    8 Exit""")
    try:
        option=int(input("Please choose your options between 1-8 numbers:"))
        if option==8:
            print("See yoo later...")
            quit()
        elif not option:
            print("Please make a choose between 1-8...")
            continue
        elif len(str(option))>1:
            print("Please make a choose between 1-8...")
            continue
        if option == 1:
            print("Clear the list...")
            playlist.clear_the_list()
            print("Cleared.")
        elif option==2:
            print('Your List:')
            playlist.view_the_list()
        elif option==3:
            add_a_track=input("Please add a new song:")
            playlist.add_track(add_a_track)
        elif option==4:
            remove_a_track=input("Please write your song name:")
            playlist.remove_track(remove_a_track)
        elif option==5:
            playing=input("Playing:")
            playlist.next_track(Playing)
        elif option==6:
            Playing=input("Playing:")
            playlist.previous_track(Playing)
        elif option==7:
            print("Random Mode...")
            playlist.play_random()
    except ValueError:
        print("Oooppss. Please Try again")






print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

import random
import time

class MusicPlayer:
    def __init__(self):
        self.song_list = {1: 'song A', 2: 'song B', 3: 'song C'}

    def add_song(self, number, name):
        self.song_list[number] = name

    def del_song(self, number):
        self.song_list.pop(number)

    def show_list(self):
        for i in self.song_list.items():
            print(*i)

    def play_song(self):
        global song_number
        song_number = input("Enter song number: ")
        print(f"Now {self.song_list[song_number]} is playing...")

    def del_list(self):
        self.song_list.clear()
        print("List is cleaning...")

    def mix_play(self):
        number = random.randint(1, len(self.song_list))                    # randint ile rastgele sarki secti
        print(f'{self.song_list[number]} is playing...')

    def next_play(self):
        global song_number
        song_number = input("Enter song number: ")
        print(f'Next {self.song_list[int(song_number) + 1]} is playing...')
        song_number = (int(song_number) + 1) % len(self.song_list)                        # mod alip basa dondurduk

    def previous_play(self):
        global song_number
        song_number = input("Enter song number: ")
        song_number = int(song_number) - 1                                                  # sarki no bir azaltilip onceki sarkiya geldi
        if int(song_number) == 0:                                                           # sarki no sifir olunca en sondaki sarkiya dondu
            song_number = len(self.song_list)
            print(f'Previous {self.song_list[song_number]} is playing...')
        else:
            print(f'Previous {self.song_list[song_number]} is playing...')


music_box = MusicPlayer()


def menu():
    print('''Menu:
    1. Add song
    2. Delete song
    3. Show list of the Songs
    4. Play
    5. Play mix
    6. Clean play list
    7. Play next song
    8. Play previous song
    9. Exit
    ''')


while True:
    menu()
    enter = input("Input one number: ")
    try:
        enter = int(enter)
        if enter == 1:                                                          # sarki ekle
            song_number = input('Enter song number: ')
            song_name = input('Enter song name: ')
            music_box.add_song(song_number, song_name)
        elif enter == 2:                                                        # sarki sil
            song_number = int(input('Enter song number which you want to delete: '))
            music_box.del_song(song_number)
        elif enter == 3:                                                        # listeyi goruntule
            music_box.show_list()
        elif enter == 4:                                                        # sarki cal
            music_box.play_song()
            time.sleep(5)
        elif enter == 5:                                                        # karisik cal
            music_box.mix_play()
            time.sleep(5)
        elif enter == 6:                                                        # listeyi temizle
            music_box.del_list()
            time.sleep(5)
        elif enter == 7:                                                        # sonraki sarki
            music_box.next_play()
            time.sleep(5)
        elif enter == 8:                                                        # onceki sarki
            music_box.previous_play()
            time.sleep(5)
        elif enter == 9:
            print('Exiting...')
            quit()
    except ValueError:
        print("Please enter 1,2,3,4,5,6,7,8,9...")

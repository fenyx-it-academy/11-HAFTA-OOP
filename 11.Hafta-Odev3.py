import random
import time


class MusicBox:

    def __init__(self):
        self.songList = ['Sikidim', 'Ask Guzeldir', 'Romatik Serseri', 'Falan Filan']
        global song
        song = 0

    def ShowSongList(self):
        print('\nThe Following Songs are in the Music Box:\n')
        for i in range(len(self.songList)):
            print(i+1, '. ', self.songList[i], sep='')

    def AddSong(self, song_name, index):
        print('Adding', f'{song}', 'to the music box...')
        time.sleep(2)
        self.songList.insert(index-1, song_name)
        print(f'{song} song added.')

    def DeleteSong(self, song):
        if type(song) == str:
            self.songList.remove(song)
            print('Deleting song', f'{song}', 'from the music box...')
            time.sleep(2)
            print(f'{song} deleted.')
        elif type(song) == int:
            print('Deleting song', f'{self.songList[song-1]}', 'from the music box...')
            time.sleep(2)
            print(f'{self.songList[song-1]} deleted.')
            del self.songList[song - 1]

    def PlaySong(self):
        global song
        try:
            song = input("Enter the name or the row number of the song you want to delete from the music box: ")
            if song.isdigit():
                song = int(song)
            if type(song) == str:
                print('Playing song', f'{song}...')
                time.sleep(6)
            elif type(song) == int:
                print('Playing song', f'{self.songList[song-1]}...')
                time.sleep(6)
        except ValueError:
            print('\nPlease type the name exactly you see in the song list!')
            time.sleep(5)

    def PlayNextSong(self):
        global song
        if type(song) == str:
            index = self.songList.index(song)
            index += 1
            index %= len(self.songList)
            print('Playing next song', f'{self.songList[index]}...')
            song = self.songList[index]
            time.sleep(6)
        elif type(song) == int:
            song += 1
            song %= len(self.songList)
            print('Playing song', f'{self.songList[song-1]}...')
            time.sleep(6)

    def PlayPreviousSong(self):
        global song
        if type(song) == str:
            index = self.songList.index(song)
            index -= 1
            print('Playing next song', f'{self.songList[index]}...')
            song = self.songList[index]
            time.sleep(6)
        elif type(song) == int:
            song -= 1
            print('Playing song', f'{self.songList[song]}...')
            time.sleep(6)

    def PlayShuffled(self):
        selected_song = random.choice(self.songList)
        print('Playing song', f'{selected_song}...')
        time.sleep(6)

    def EmptyMusicBox(self):
        are_you_sure = input('\n!!!Warning this action can NOT be reversed.!!!\n'
                             'You will lose all songs in the Music Box.\n'
                             'Are you sure to empty the Music Box? "y" for "Yes" and "n" for "No": ')
        if are_you_sure.lower() == 'y':
            print("\nDeleting all songs in the Music Box...")
            time.sleep(5)
            print('\nMusic Box is empty.')
            self.songList.clear()
            time.sleep(2)
        else:
            pass


music_box = MusicBox()

message = """

What would you like to do:
    1. Show Song List
    2. Add a a song to the music box 
    3. Delete a song from the music box
    4. Play a song from the music box
    5. Play Next Song
    6. Play Previous Song
    7. Play shuffled
    8. Empty the Music Box
       Press q to quit."""

action = ''

while True:
    print(message)
    action = input("\nSelect an action from the menu: ")
    if action == '1':
        music_box.ShowSongList()
    elif action == '2':
        song = input('Enter the name of the song you want to add to the music box: ')
        index = int(input('Enter the row number you want to add the song' + f'{song}: '))
        music_box.AddSong(song, index)

    elif action == '3':
        try:
            song = input("Enter the name or the row number of the song you want to delete from the music box: ")
            if song.isdigit():
                song = int(song)
            music_box.DeleteSong(song)

        except ValueError:
            print('\nPlease type the name exactly you see in the song list!')
            time.sleep(5)

    elif action == '4':
        music_box.PlaySong()

    elif action == '5':
        music_box.PlayNextSong()

    elif action == '6':
        music_box.PlayPreviousSong()

    elif action == '7':
        music_box.PlayShuffled()

    elif action == '8':
        music_box.EmptyMusicBox()

    elif action == 'q':
        print('\nMusic Box is shutting down...')
        time.sleep(5)
        print('\nGood Bye!')
        break
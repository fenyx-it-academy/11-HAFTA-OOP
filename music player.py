from random import choice
class Music_player():
    def __init__(self):
        self.music_list = []
        
    def reset_list(self):
        self.music_list.clear()
        
    def show_list(self):
        print("Musics:")
        for music in self.music_list:
            print(music)
            
    def add_music(self, music):
        self.music_list.append(music)
        print(f"{music} was added.")
        
    def del_music(self, music):
        if music in self.music_list:
            self.music_list.remove(music)
            print(f"{music} was deleted.")
        else:
            print(f"{music} is not in the list.")
            
    def play_random(self):
        self.music = choice(self.music_list)
        print(f"{self.music} is playing")
        
    def next(self):
        index = self.music_list.index(self.music) + 1
        if index == len(self.music_list):
            index = 0
        self.music = self.music_list[index]
        print(f"{self.music} is playing.")
        
    def previous(self):
        index = self.music_list.index(self.music) - 1
        self.music = self.music_list[index]
        print(f"{self.music} is playing.")
        

        
player1 = Music_player()
player1.add_music("1asd")
player1.add_music("2asdasd")
player1.add_music("3asdas")
player1.add_music("4asasdd")
player1.add_music("5asasdd")
player1.del_music("1asd")

player1.show_list()

player1.play_random()

player1.previous()
player1.next()
player1.previous()
player1.previous()



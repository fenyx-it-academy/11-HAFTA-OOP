import time
import random
class Music_Player():
    def __init__(self, play_list=["track 1","track 2","track 3","track 4","track 5"]):
        self.play_list = play_list
    def clear_playlist(self):
        print("Your playlist is clearing out!!!\n...")
        time.sleep(3)
        self.play_list.clear()
        print("Your playlist clearad out\nYour playlist is: {} (empty)".format(self.play_list))
    def display(self):
        if self.play_list==[]:
            print("!!!Your playlist is empty!!!")
        else:
            for i in self.play_list:
                print(i)
    def add_track(self):
        if self.play_list == []:
            print("Your playlist is empty!!!")
        else:
            print("Your playlist is: ")
            ipod.display()
        add = input("Please enter the name of track you would like to add\n")
        if add in self.play_list:
            while True:
                check = input("The track you would like to add is already in playlist!!!\nDo you still want to add?\nIf yes, press 'ENTER',If no, press 'N'\n")
                if not check:
                    print("The new track is being added\n...")
                    time.sleep(3)
                    self.play_list.append(add)
                    self.play_list.sort()
                    print("The new track has been added\nThe updated playlist is: ")
                    ipod.display()
                    break
                elif check.lower()=="n":
                    print("The addition operation has been cancelled")
                    break
                else:
                    print("You entered an incorrect code. Please check and read instructions!!!\n")
                    continue
        else:
            print("The new track is being added\n...")
            time.sleep(3)
            self.play_list.append(add)
            self.play_list.sort()
            print("The new track has been added\nThe updated playlist is: ")
            ipod.display()
    def track_delete(self):
        print("Your playlist is: ")
        ipod.display()
        key=0
        while key==0:
            delete_track = input("Please enter the name of track you would like to delete\n")
            if delete_track in self.play_list:
                print("The new track is being deleting\n...")
                time.sleep(3)
                self.play_list.remove(delete_track)
                self.play_list.sort()
                print("The new track has been deleted\nThe updated playlist is: ")
                ipod.display()
                key=1
            else:
                print("You entered an incorrect track name!!!\nThe track you would like to delete is not in playlist\nPlease check the track name")
                while True:
                    check = input("Would you like to continue deleting track!!!\nIf yes, press 'ENTER',If no, press 'N'\n")
                    if not check:
                        break
                    elif check.lower() == "n":
                        print("The deletion operation has been cancelled")
                        key=1
                        break
                    else:
                        print("You entered an incorrect code. Please check and read instructions!!!\n")
                        continue
    def next_track(self):
        next=now_playing
        if self.play_list.index(next)!=(len(self.play_list)-1):
            next_play= self.play_list[self.play_list.index(next)+1]
            print("The next track is: ",next_play,"\nNow next track is now playing\n")
        else:
            next_play=self.play_list[0]
            print("The next track is: ",next_play,"\nNow next track is now playing\n")
        return next_play
    def previous_track(self):
        previous=now_playing
        if self.play_list.index(previous)!= 0:
            previous_play=self.play_list[self.play_list.index(previous)-1]
            print("The previous track is: ",previous_play,"\nNow previous track is now playing\n")
        else:
            previous_play=self.play_list[len(self.play_list)-1]
            print("The previous track is: ",previous_play,"\nNow previous track is now playing\n")
        return previous_play
    def play_random(self):
        while True:
            play_ran=random.choice(self.play_list)
            if play_ran==now_playing:
                continue
            else:
                print("Music Player plays randomly the tracks.\nPlaying track is: ",play_ran)
                break
        return play_ran
ipod=Music_Player()
now_playing= random.choice(ipod.play_list)
print(type(now_playing))
print("{} is now playing...\n".format(now_playing))
key=0
while key==0:
    operation=input("""This is a Music Player program.
Please choose a operation you would like to do;

To clear the playlist, press                "1"
To display the playlist, press              "2"
To add a new track, press                   "3"
To delete a track, press                    "4"
To play the next track, press               "5"
To play the previous track, press           "6"
To play at random, press                    "7"
To exit the program, press                  "e"
""")
    if operation=="1":
        ipod.clear_playlist()
    elif operation=="2":
        print("Your playlist is: ")
        ipod.display()
    elif operation=="3":
        if ipod.play_list==[]:
            ipod.add_track()
            now_playing=ipod.play_list[0]
        else:
            ipod.add_track()
    elif operation=="4":
        if ipod.play_list==[]:
            print("Your playlist is empty!!! You can not delete the track!!!")
        else:
            ipod.track_delete()
    elif operation=="5":
        if ipod.play_list==[]:
            print("Your playlist is empty!!! Next track can not be played!!!\nPlease add a new track")
        else:
            now_playing=ipod.next_track()
    elif operation=="6":
        if ipod.play_list==[]:
            print("Your playlist is empty!!! Previous track can not be played!!!\nPlease add a new track")
        else:
            now_playing = ipod.previous_track()
    elif operation=="7":
        if ipod.play_list==[]:
            print("Your playlist is empty!!! Random play can not be played!!!\nPlease add a new track")
        elif len(ipod.play_list)==1:
            now_playing = ipod.play_list[0]
            print("Music Player plays randomly the tracks.\nPlaying track is: ", now_playing)
        else:
            now_playing = ipod.play_random()
    elif operation.lower()=="e":
        print("Music Player terminated!!!")
        key=1
    else:
        print("You entered an incorrect code. Please check and read instructions!!!\n")
        play_exit = 0
        while play_exit == 0:
            q = input("To continue the playing music player, please press: 'ENTER'\nTo exit the music player, please press: 'e'\n")
            if not q:
                play_exit = 1
                key=0
            elif q.lower() == "e":
                print("Music Player terminated!!!")
                play_exit = 1
                key = 1
            else:
                print("You entered an incorrect code. Please check and read instructions!!!\n")
                continue

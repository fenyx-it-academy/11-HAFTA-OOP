import time
import random
class Game():
    def __init__(self, table, last_table):
        self.table = table
        self.last_table = last_table
    def ships_4(self):
        w=random.randint(1,2)
        if w==1:
            a=random.randint(1,10)
            b=random.randint(0,6)
            for i in range (1,5):
                b+=1
                self.last_table[a][b]="*4*"
        else:
            a = random.randint(0,6)
            b = random.randint(1,10)
            for i in range(1, 5):
                a += 1
                self.last_table[a][b] = "*4*"
        z=random.randint(1,2)
        if z==1:
            count=1
            while count<5:
                c=random.randint(1,10)
                d=random.randint(0,6)
                for i in range(1,5):
                    d+=1
                    if self.last_table[d][c]=="___":
                        count+=1
                    else:
                        break
            for i in range(1,5):
                self.last_table[d][c]="*4*"
                d-=1
        else:
            count = 1
            while count < 5:
                c = random.randint(0,6)
                d = random.randint(1,10)
                for i in range(1, 5):
                    c += 1
                    if self.last_table[d][c] == "___":
                        count += 1
                    else:
                        break
            for i in range(1, 5):
                self.last_table[d][c] = "*4*"
                c -= 1
        return self.last_table
    def ships_3(self):
        w=random.randint(1,2)
        if w==1:
            count=1
            while count<4:
                a=random.randint(1,10)
                b=random.randint(0,6)
                for i in range(1,4):
                    b+=1
                    if self.last_table[a][b]=="___":
                        count+=1
                    else:
                        break
            for i in range(1,4):
                self.last_table[a][b]="*3*"
                b-=1
        else:
            count = 1
            while count < 4:
                a = random.randint(0, 6)
                b = random.randint(1, 10)
                for i in range(1, 4):
                    a += 1
                    if self.last_table[a][b] == "___":
                        count += 1
                    else:
                        break
            for i in range(1, 4):
                self.last_table[a][b] = "*3*"
                a -= 1
        z=random.randint(1,2)
        if z==1:
            count=1
            while count<4:
                c=random.randint(1,10)
                d=random.randint(0,6)
                for i in range(1,4):
                    d+=1
                    if self.last_table[c][d]=="___":
                        count+=1
                    else:
                        break
            for i in range(1,4):
                self.last_table[c][d]="*3*"
                d-=1
        else:
            count = 1
            while count < 4:
                c = random.randint(0,6)
                d = random.randint(1,10)
                for i in range(1, 4):
                    c += 1
                    if self.last_table[c][d] == "___":
                        count += 1
                    else:
                        break
            for i in range(1, 4):
                self.last_table[c][d] = "*3*"
                c -= 1
        return self.last_table
    def ships_2(self):
        w=random.randint(1,2)
        if w==1:
            count=1
            while count<3:
                a=random.randint(1,10)
                b=random.randint(0,6)
                for i in range(1,3):
                    b+=1
                    if self.last_table[a][b]=="___":
                        count+=1
                    else:
                        break
            for i in range(1,3):
                self.last_table[a][b]="*2*"
                b-=1
        else:
            count = 1
            while count < 3:
                a = random.randint(0,6)
                b = random.randint(1, 10)
                for i in range(1, 3):
                    a += 1
                    if self.last_table[a][b] == "___":
                        count += 1
                    else:
                        break
            for i in range(1, 3):
                self.last_table[a][b] = "*2*"
                a -= 1
        z=random.randint(1,2)
        if z==1:
            count=1
            while count<3:
                c=random.randint(1,10)
                d=random.randint(0,6)
                for i in range(1,3):
                    d+=1
                    if self.last_table[d][c]=="___":
                        count+=1
                    else:
                        break
            for i in range(1,3):
                self.last_table[d][c]="*2*"
                d-=1
        else:
            count = 1
            while count < 3:
                c = random.randint(0,6)
                d = random.randint(1,10)
                for i in range(1, 3):
                    c += 1
                    if self.last_table[d][c] == "___":
                        count += 1
                    else:
                        break
            for i in range(1, 3):
                self.last_table[d][c] = "*2*"
                c -= 1
        return self.last_table
    def ships_1(self):
        while True:
            count=0
            while count<2:
                a=random.randint(1,10)
                b=random.randint(0,6)
                if self.last_table[a][b]=="___":
                    self.last_table[a][b]="*1*"
                    count+=1
                    continue
                else:
                    continue
            break
        return self.last_table
    def print_gtable(self,args):
        for i in args:
            print("\t".expandtabs(30),*i,end="\n"*2)
    def winning_criteria(self,args):
        count=0
        for i in args:
            for k in i:
                if k=="*4*" or k=="*3*" or k=="*2*" or k=="*1*":
                    count+=1
        return count
    def player(self):
        self.print_gtable(self.table)
        print("\n"*3)
        self.ships_4()
        self.ships_3()
        self.ships_2()
        self.ships_1()
        number_of_trials=0
        count=self.winning_criteria(self.last_table)
        while number_of_trials<15:
            count1=self.winning_criteria(self.table)
            if count==count1:
                print("Congratulations, You win!!!\nYou destroyed all ships")
                self.print_gtable(self.table)
                break
            try:
                while True:
                    x=int(input("Please enter a number from 1 to 10 (from top to bottom): "))
                    if x>10 or x<1:
                        print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
                        continue
                    y=int(input("Please enter a number from 1 to 10 (from left to right): "))
                    if y>10 or y<1:
                        print("You made an incorrect entry. Please enter a number from 1 to 10 !!!\n")
                        continue
                    break
            except ValueError:
                print("You made an incorrect entry. Please check and read instructions!!!\n")
                continue
            if self.table[x][y]!="___":
                print("\nPlease be careful!!!\nYou have tried to hit this target before.\nPlease check the coordinates of the target!!!")
                number_of_trials += 1
                print("Remaining trial is:", 15 - number_of_trials)
                self.print_gtable(self.table)
                time.sleep(5)
            elif self.last_table[x][y]=="*4*":
                print("\n***Congratulations***, you hit a 4-unit ship!!!\n")
                self.table[x][y]=self.last_table[x][y]
                self.print_gtable(self.table)
            elif self.last_table[x][y]=="*3*":
                print("\n***Congratulations***, you hit a 3-unit ship!!!\n")
                self.table[x][y]=self.last_table[x][y]
                self.print_gtable(self.table)
            elif self.last_table[x][y]=="*2*":
                print("\n***Congratulations***, you hit a 2-unit ship!!!\n")
                self.table[x][y]=self.last_table[x][y]
                self.print_gtable(self.table)
            elif self.last_table[x][y]=="*1*":
                print("\n***Congratulations***, you hit a 1-unit ship!!!\n")
                self.table[x][y]=self.last_table[x][y]
                self.print_gtable(self.table)
            elif self.table[x][y]=="___":
                print("\nSorry, you missed the target!!!")
                self.table[x][y]="X".center(3)
                number_of_trials+=1
                print("Remaining trial is:", 15 - number_of_trials)
                self.print_gtable(self.table)
                time.sleep(5)
        if number_of_trials==15:
            print("You have used 15 trials and You could not destroy all ships!!!\nYOU LOST!!!\nThis is the starting table of the game where all the ships are placed!!!\n")
            self.print_gtable(self.last_table)
game_table = [["    "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","10"],
[" 1  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 2  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 3  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 4  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 5  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 6  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 7  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 8  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 9  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
["10  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],]

game_table1 = [["    "," 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 ","10"],
[" 1  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 2  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 3  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 4  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 5  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 6  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 7  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 8  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
[" 9  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],
["10  ","___", "___", "___","___", "___", "___","___", "___", "___","___"],]

battle_ship=Game(table=game_table,last_table=game_table1)
if __name__== "__main__":
    battle_ship.player()


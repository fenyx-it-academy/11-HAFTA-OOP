from random import randint,choice
from time import sleep

class battleships():
    def __init__(self):
        self.table = [["--" for a in range(10)] for b in range(10)]
        self.all_coor = [[a, b] for a in range(10) for b in range(10)]
        self.time = False
        self.play()

    def horizontal(self, unit):
        while True:
            self.ship = []
            coor = choice(self.all_coor)
            if coor[0] > 9 - unit:
                coor[0] = 9 - unit
            if coor not in self.ships:
                #to check whether 'coor' is besides other ship or not
                if [coor[0] + 1, coor[1]] not in self.ships:
                    if [coor[0] - 1, coor[1]] not in self.ships:
                        if [coor[0], coor[1] + 1] not in self.ships:
                            if [coor[0], coor[1] - 1] not in self.ships:
                                self.ship.append(coor)
                
            for i in range(unit-1):
                coor = [coor[0] + 1] + [coor[1]]
                if coor not in self.ships:
                    #to check whether 'coor' is besides other ship or not
                    if [coor[0] + 1, coor[1]] not in self.ships:
                        if [coor[0] - 1, coor[1]] not in self.ships:
                            if [coor[0], coor[1] + 1] not in self.ships:
                                if [coor[0], coor[1] - 1] not in self.ships:
                                    self.ship.append(coor)

            if len(self.ship) == unit:
                self.ships.extend(self.ship)
            else:
                continue
            return self.ships

    def vertical(self, unit):
        while True:
            self.ship = []
            coor = choice(self.all_coor)
            if coor[1] > 9 - unit:
                coor[1] = 9 - unit
            if coor not in self.ships:
                #to check whether 'coor' is besides other ship or not
                if [coor[0] + 1, coor[1]] not in self.ships:
                    if [coor[0] - 1, coor[1]] not in self.ships:
                        if [coor[0], coor[1] + 1] not in self.ships:
                            if [coor[0], coor[1] - 1] not in self.ships:
                                self.ship.append(coor)
                
            for i in range(unit-1):
                coor = [coor[0]] + [coor[1] + 1]
                if coor not in self.ships:
                    #to check whether 'coor' is besides other ship or not
                    if [coor[0] + 1, coor[1]] not in self.ships:
                        if [coor[0] - 1, coor[1]] not in self.ships:
                            if [coor[0], coor[1] + 1] not in self.ships:
                                if [coor[0], coor[1] - 1] not in self.ships:
                                    self.ship.append(coor)

            if len(self.ship) == unit:
                self.ships.extend(self.ship)
            else:
                continue
            return self.ships

    def deploy(self):
        #for ships which has 4 units
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break

            elif mark == 0:
                self.horizontal(4)

            elif mark == 1:
                self.vertical(4)
            counter += 1
        #for ships which has 3 units
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break

            elif mark == 0:
                self.horizontal(3)

            elif mark == 1:
                self.vertical(3)
            counter += 1
        #for ships which has 2 units
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break

            elif mark == 0:
                self.horizontal(2)

            elif mark == 1:
                self.vertical(2)
            counter += 1
        #for ships which has 1 unit
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break
            self.horizontal(1)
            counter += 1


    def all_ships(self):
        for ship in self.ships:
            self.table[ship[0]][ship[1]] = "XX"
        return self.table

    def print_table(self):
        for item in self.table:
            print("\n\t".expandtabs(20),*item)
        if self.time:
            sleep(1)
    
    def coordinate(self):
        global y
        global x
        while True:
            y = input("\nPlease choose the y axis:")
            if y.isdigit() == False:
                print("Please enter number between 0 - 10.")
                time = False
                continue
            else:
                y = int(y)
            y = y - 1
            if y > 9 or y < 0:
                print("Please enter number between 0 - 10.")
                continue
            
            x = input("\nPlease choose the x axis:")
            if x.isdigit() == False:
                print("Please enter number between 0 - 10.")
                time = False
                continue
            else:
                x = int(x)
            x = x - 1
            if x > 9 or x < 0:
                print("Please enter number between 0 - 10.")
                continue
            if self.table[y][x] == "  " or self.table[y][x] == "XX":
                print("You've already fire there.Please try again.")
                continue
            else:
                break

    def fire(self):
        global time
        if [y, x] not in self.ships:
            self.table[y][x] = "  "
            self.time = True
        else:
            self.table[y][x] = "XX"
            self.time = False
        for ship in self.ships[0:4]:
            if [y, x] in self.ships[0:4]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[4:8]:
            if [y, x] in self.ships[4:8]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[8:11]:
            if [y, x] in self.ships[8:11]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[11:14]:
            if [y, x] in self.ships[11:14]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[14:16]:
            if [y, x] in self.ships[14:16]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[16:18]:
            if [y, x] in self.ships[16:18]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[18:19]:
            if [y, x] in self.ships[18:19]:
                self.table[ship[0]][ship[1]] = "XX"
        for ship in self.ships[19:20]:
            if [y, x] in self.ships[19:20]:
                self.table[ship[0]][ship[1]] = "XX"
        return self.table

    def prnt(self):
        print("*"*15,"BATTLESHIPS","*"*15)
        print("""\n           WELCOME TO BATTLESHIPS\n
        There are 8 ships.Two of them has 4 unit.
                          Two of them has 3 unit.
                          Two of them has 2 unit.
                          Two of them has 1 unit.
        Ships are not besides each other.
        You can shoot them 15 times.
        You can choose the coordinates to shoot there.""")


    def play(self):
        self.prnt()
        self.turn = 0
        self.ships = []#all ships which are deployed
        self.deploy()
        try:
            while True:
                if self.turn == 15:
                    print("Game over.You lose.")
                    self.all_ships()
                    self.print_table()
                    break
                
                self.print_table()
                self.coordinate()
                self.fire()
                self.turn += 1

                counter = 0
                for items in self.table:
                    for item in items:
                        if item == "XX":
                            counter += 1
                if counter == 20:
                    self.print_table()
                    print("\nCongratulations.You've hit the each ships.")
                    break
        except:
            print("Something happened wrong, please try again")

battle1 = battleships()

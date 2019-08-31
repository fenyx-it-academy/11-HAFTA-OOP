from random import randint,choice
class Battleships():
    def __init__(self):
        self.table = [["--" for i in range(10)] for i in range(10)]
        self.all_coor = [[a, b] for a in range(10) for b in range(10)]
        self.ships = []
        self.print()
        self.deploy()
        self.play()
    def deploy(self):
        counter = 0
        #for ships which has 4 units
        while True:
            mark = randint(0,1)
            if counter == 2:
                break
            
            elif mark == 0:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[0] > 6:
                    self.first_coor[0] = 6
                self.second_coor = [self.first_coor[0] + 1] + [self.first_coor[1]]
                self.third_coor = [self.first_coor[0] + 2] + [self.first_coor[1]]
                self.fourth_coor = [self.first_coor[0] + 3] + [self.first_coor[1]]
                if self.first_coor not in self.ships and self.second_coor not in self.ships and self.third_coor not in self.ships and self.fourth_coor not in self.ships:
                    self.ships.extend([self.first_coor, self.second_coor, self.third_coor, self.fourth_coor])
                    counter += 1
                else:
                    continue
                
            elif mark == 1:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[1] > 6:
                    self.first_coor[1] = 6
                self.second_coor = [self.first_coor[0]] + [self.first_coor[1] + 1]
                self.third_coor = [self.first_coor[0]] + [self.first_coor[1] + 2]
                self.fourth_coor = [self.first_coor[0]] + [self.first_coor[1] + 3]
                if self.first_coor not in self.ships and self.second_coor not in self.ships and self.third_coor not in self.ships and self.fourth_coor not in self.ships:
                    self.ships.extend([self.first_coor, self.second_coor, self.third_coor, self.fourth_coor])
                    counter += 1
                else:
                    continue
                
        #for ships which has 3 units
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break
            
            elif mark == 0:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[0] > 7:
                    self.first_coor[0] = 7
                self.second_coor = [self.first_coor[0] + 1] + [self.first_coor[1]]
                self.third_coor = [self.first_coor[0] + 2] + [self.first_coor[1]]
                if self.first_coor not in self.ships and self.second_coor not in self.ships and self.third_coor not in self.ships:
                    self.ships.extend([self.first_coor, self.second_coor, self.third_coor])
                    counter += 1
                else:
                    continue
                
            elif mark == 1:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[1] > 7:
                    self.first_coor[1] = 7
                self.second_coor = [self.first_coor[0]] + [self.first_coor[1] + 1]
                self.third_coor = [self.first_coor[0]] + [self.first_coor[1] + 2]
                if self.first_coor not in self.ships and self.second_coor not in self.ships and self.third_coor not in self.ships:
                    self.ships.extend([self.first_coor, self.second_coor, self.third_coor])
                    counter += 1
                else:
                    continue
        #for ships which has 2 units
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break
            
            elif mark == 0:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[0] > 8:
                    self.first_coor[0] = 8
                self.second_coor = [self.first_coor[0] + 1] + [self.first_coor[1]]
                if (self.first_coor not in self.ships) and (self.second_coor not in self.ships):
                    self.ships.extend([self.first_coor, self.second_coor])
                    counter += 1
                else:
                    continue
                
            elif mark == 1:
                self.first_coor = choice(self.all_coor)
                if self.first_coor[1] > 8:
                    self.first_coor[1] = 8
                self.second_coor = [self.first_coor[0]] + [self.first_coor[1] + 1]
                if (self.first_coor not in self.ships) and (self.second_coor not in self.ships):
                    self.ships.extend([self.first_coor, self.second_coor])
                    counter += 1
                else:
                    continue
        #for ships which has 1 unit
        counter = 0
        while True:
            mark = randint(0,1)
            if counter == 2:
                break
            self.coor = choice(self.all_coor)
            if self.coor not in self.ships:
                    self.ships.extend([self.coor])
                    counter += 1
            else:
                continue
            
    def print_table(self):
        for item in self.table:
            print("\n\t".expandtabs(20),*item)

    def coordinate(self):
        global y
        global x
        y = int(input("\nPlease choose the y axis:"))
        x = int(input("\nPlease choose the x axis:"))
        y = y - 1
        x = x - 1
     
    def all_ships(self):
        for ship in self.ships:
            self.table[ship[0]][ship[1]] = "XX"
        return self.table
    def fire(self):
        if [y, x] not in self.ships:
            self.table[y][x] = "  "
        else:
            self.table[y][x] = "XX"
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
    def print(self):
        print("*"*15,"BATTLESHIPS","*"*15)
        print("""\n           WELCOME TO BATTLESHIPS\n
        There are 8 ships.Two of them has 4 unit.
                          Two of them has 3 unit.
                          Two of them has 2 unit.
                          Two of them has 1 unit.
        You can shoot them 15 times.
        You can choose the coordinates to shoot there.""")
    def play(self):
        turn = 0
        while True:    
            self.print_table()
            self.coordinate()
            self.fire()
            turn += 1
            if turn == 3:
                print("Game over.You lose.")
                self.all_ships()
                self.print_table()
                break
            counter = 0
            for items in self.table:
                for item in items:
                    if item == "XX":
                        counter += 1
            if counter == 20:
                print_table()
                print("\nCongratulations.You've hit the each ships.")
                break

battle = Battleships()        
    
    
    






        


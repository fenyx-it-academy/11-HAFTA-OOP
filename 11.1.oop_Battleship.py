print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


from random import randint, random
import time
print("\t".center(33), "~ WELCOME THE BATTLESHIP GAME ~")
time.sleep(3)

table = [[" ~ " for k in range(10)] for l in range(10)]
print("Shooting Table:\n")

class Tafel:
    def __init__(self):
        self.table = table
    def board(self):
        global table
        for t in self.table:
            print("\t".center(30), *t, end="\n")
mese = Tafel()
mese.board()


ship1 = []
ship11 = []
ship2 = []
ship22 = []
ship3 = []
ship33 = []
ship4 = []
ship44 = []
ship_number = 0
while ship_number <= 8:                             #Gemileri olusturuyoruz
    ship_number += 1
    if ship1 not in table:
        x = randint(0, 9)
        y = randint(0, 9)
        ship1 = [[x, y]]
    else:
        table.remove(ship1)
    if ship11 not in table:
        x = randint(0, 9)
        y = randint(0, 9)
        ship11 = [[x, y]]
    else:
        table.remove(ship11)
    if ship2 not in table:
        x = randint(0, 9)
        y = randint(0, 7)
        ship2 = [[x, y+1], [x, y+2]]        #koornidatlarin degerlerine ekleme yapildikca araliktan cikma ihtimaline karsi araligi azaltiyoruz
    else:
        table.remove(ship2)
    if ship22 not in table:
        x = randint(0, 7)
        y = randint(0, 9)
        ship22 = [[x+1, y], [x+2, y]]
    else:
        table.remove(ship22)
    if ship3 not in table:
        x = randint(0, 9)
        y = randint(0, 6)
        ship3 = [[x, y+1], [x, y+2], [x, y+3]]
    else:
        table.remove(ship3)
    if ship33 not in table:
        x = randint(0, 6)
        y = randint(0, 9)
        ship33 = [[x+1, y], [x+2, y], [x+3, y]]
    else:
        table.remove(ship33)
    if ship4 not in table:
        x = randint(0, 9)
        y = randint(0, 5)
        ship4 = [[x, y+1], [x, y+2], [x, y+3], [x, y+4]]
    else:
        table.remove(ship4)
    if ship44 not in table:
        x = randint(0, 5)
        y = randint(0, 9)
        ship44 = [[x+1, y], [x+2, y], [x+3, y], [x+4, y]]
    else:
        table.remove(ship44)

done_targets = []                                             #yapilan hedefleri listeye atalim
exact_shoot = []                                              #dogru tahmin edilen atislari bir listeye atalim
rights = 0                                                    #taninan haklar
while rights <= 15:
    time.sleep(1)
    guess_row = input("Please input a number for row(x): ")
    guess_column = input("Please input a number for column(y): ")
    try:
        guess_row = int(guess_row)
        guess_column = int(guess_column)
        target = [guess_row, guess_column]
        if (0 <= guess_row < 10) or (0 <= guess_column < 10):
            if target in done_targets:
                print("You choosed this coordinates before. You have to wait 5 seconds...")
                time.sleep(5)
                continue
            else:
                rights += 1
                done_targets.append(target)                                # hangi hamle yapildiysa yapilanlara eklesin
                table[guess_row][guess_column] = " X "                       # yapilan atislar tabloda 'X' olarak gorunsun
                if target in ship1:
                    table[ship1[0][0]][ship1[0][1]] = ' ⛴'
                    for i in ship1:
                        done_targets.append(i)                   #yapilan hamleler bos listeye eklensin
                    print('Congrats...you shooted first shortest ship\n')
                    exact_shoot.append(target)                    # dogru hamle yapildiginda dogru tahmin edilen listeye eklensin
                if target in ship11:
                    table[ship11[0][0]][ship11[0][1]] = ' ⛴'
                    for i in ship11:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congrats...you shooted second shortest ship\n')
                    exact_shoot.append(target)
                if target in ship2:
                    table[ship2[0][0]][ship2[0][1]] = ' ⛴'
                    table[ship2[1][0]][ship2[1][1]] = ' ⛴'
                    for i in ship2:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congrats...you shooted first short ship\n')
                    exact_shoot.append(target)
                if target in ship22:
                    table[ship22[0][0]][ship22[0][1]] = ' ⛴'
                    table[ship22[1][0]][ship22[1][1]] = ' ⛴'
                    for i in ship22:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congrats...you shooted second short ship\n')
                    exact_shoot.append(target)
                if target in ship3:
                    table[ship3[0][0]][ship3[0][1]] = ' ⛴'
                    table[ship3[1][0]][ship3[1][1]] = ' ⛴'
                    table[ship3[2][0]][ship3[2][1]] = ' ⛴'
                    for i in ship3:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congrats...you shooted first big ship\n')
                    exact_shoot.append(target)
                if target in ship33:
                    table[ship33[0][0]][ship33[0][1]] = ' ⛴'
                    table[ship33[1][0]][ship33[1][1]] = ' ⛴'
                    table[ship33[2][0]][ship33[2][1]] = ' ⛴'
                    for i in ship33:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congrats...you shooted second big ship\n')
                    exact_shoot.append(target)
                if target in ship4:
                    table[ship4[0][0]][ship4[0][1]] = ' ⛴'
                    table[ship4[1][0]][ship4[1][1]] = ' ⛴'
                    table[ship4[2][0]][ship4[2][1]] = ' ⛴'
                    table[ship4[3][0]][ship4[3][1]] = ' ⛴'
                    for i in ship4:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congratulations...you shooted first Amiral Battleship\n')
                    exact_shoot.append(target)
                if target in ship44:
                    table[ship44[0][0]][ship44[0][1]] = ' ⛴'
                    table[ship44[1][0]][ship44[1][1]] = ' ⛴'
                    table[ship44[2][0]][ship44[2][1]] = ' ⛴'
                    table[ship44[3][0]][ship44[3][1]] = ' ⛴'
                    for i in ship44:  # dogru hamle yapildiginda geminin bulundugu noktalari yapilan ham. list. ekledik
                        done_targets.append(i)
                    print('Congratulations...you shooted second Amiral Battleship\n')
                    exact_shoot.append(target)
                mese.board()
        else:
            print("OOPS...Missed ocean...You have to more carefull! Input a number between 0 - 9")

        if len(exact_shoot) == 8:
            print("CONGRATULATIONS YOU WIN...")
            quit()
    except ValueError:
        print("Please input just numbers between 0 - 9...")
print("YOUR RIGHTS OVER \n\n\n...GAME OVER...")

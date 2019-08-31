import random
import time

ocean = []
row: int = None
col: int = None
ship1 = []
ship2 = []
ship3 = []
ship4 = []
ship5 = []
ship6 = []
ship7 = []
ship8 = []
shipPositionList = []
shipsHit = 0


def gameStart():
    gameStarter ="""\n
     {}{}                                                              
    {}|{}|
    {}|                                                                   |
    {}| Enter the row and column number where you want to send a torpido  |
    {}| Row numbers and column numbers are between 1 - 10.                |
    {}|                                                                   |
    {}| {} |
     {}{}\n""".format('\t'.expandtabs(27), ('-' * 67),
                      '\t'.expandtabs(27), 'Battleship Game Playing Instructions'.center(67),
                      '\t'.expandtabs(27), '\t'.expandtabs(27), '\t'.expandtabs(27), '\t'.expandtabs(27),
                      '\t'.expandtabs(27), 'The game starts now'.center(65),
                      '\t'.expandtabs(27), ('-' * 67))

    print('\t'.expandtabs(30) + gameStarter + '\n\n')

def gameBoardMaker():
    for i in range(10):
        ocean.append(['-----'] * 10)


def gameBoardPrinter(board):
    row1 = [x for x in range(1, 11)]
    i = 1
    print('\n', '\t'.expandtabs(27), *row1, sep='     ')
    print('\n')
    for r in board:
        print('\t'.expandtabs(30), str(i), ' ', ' '.join(r))
        print('\n')
        i += 1



def positionCheck(shipPositionList, r, c):
    for ship in shipPositionList:
        for index in range(len(ship)):
            if [r, c] != ship[index]:
                return True
            else:
                return False


def positionCheckV2(shipList, ship):
    for i in range(len(shipList)):
        for index in range(len(ship)):
            if ship[index] in shipList[i]:
                return False
    else:
        return True


def shipMaker(shipList):
    isAvailable = False

    # Placing ship1 in the ocean
    row = random.randint(0, 6)
    col = random.randint(0, 6)

    ship1Vert = [[row, col], [row + 1, col], [row + 2, col], [row + 3, col]]
    ship1Hor = [[row, col], [row, col + 1], [row, col + 2], [row, col + 3]]
    global ship1
    ship1 = random.choice([ship1Hor, ship1Vert])
    shipList.append(ship1)


    isAvailable = False

    # Placing ship2 in the ocean
    while not isAvailable:
        row = random.randint(0, 6)
        col = random.randint(0, 6)

        ship2Vert = [[row, col], [row + 1, col], [row + 2, col], [row + 3, col]]
        ship2Hor = [[row, col], [row, col + 1], [row, col + 2], [row, col + 3]]
        global ship2
        ship2 = random.choice([ship2Hor, ship2Vert])

        if positionCheckV2(shipPositionList, ship2):
            isAvailable = True
            shipList.append(ship2)
        else:
            continue

    isAvailable = False
    # Placing ship3 in the ocean
    while not isAvailable:
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        ship3Vert = [[row, col], [row + 1, col], [row + 2, col]]
        ship3Hor = [[row, col], [row, col + 1], [row, col + 2]]
        global ship3
        ship3 = random.choice([ship3Hor, ship3Vert])

        if positionCheckV2(shipPositionList, ship3):
            isAvailable = True
            shipList.append(ship3)
        else:
            continue

    isAvailable = False

    # Placing ship4 in the ocean
    while not isAvailable:
        row = random.randint(0, 7)
        col = random.randint(0, 7)

        ship4Vert = [[row, col], [row + 1, col], [row + 2, col]]
        ship4Hor = [[row, col], [row, col + 1], [row, col + 2]]
        global ship4
        ship4 = random.choice([ship4Hor, ship4Vert])

        if positionCheckV2(shipPositionList, ship4):
            isAvailable = True
            shipList.append(ship4)
        else:
            continue

    isAvailable = False

    # Placing ship5 in the ocean
    while not isAvailable:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        ship5Vert = [[row, col], [row + 1, col]]
        ship5Hor = [[row, col], [row, col + 1]]
        global ship5
        ship5 = random.choice([ship5Hor, ship5Vert])

        if positionCheckV2(shipPositionList, ship5):
            isAvailable = True
            shipList.append(ship5)
        else:
            continue

    isAvailable = False

    # Placing ship6 in the ocean
    while not isAvailable:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        ship6Vert = [[row, col], [row + 1, col]]
        ship6Hor = [[row, col], [row, col + 1]]
        global ship6
        ship6 = random.choice([ship6Hor, ship6Vert])

        if positionCheckV2(shipPositionList, ship6):
            isAvailable = True
            shipList.append(ship6)
        else:
            continue

    isAvailable = False

    # Placing ship7 in the ocean
    while not isAvailable:
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        ship7Vert = [[row, col]]
        ship7Hor = [[row, col]]
        global ship7
        ship7 = random.choice([ship7Hor, ship7Vert])

        if positionCheckV2(shipPositionList, ship7):
            isAvailable = True
            shipList.append(ship7)
        else:
            continue

    isAvailable = False

    # Placing ship8 in the ocean
    while not isAvailable:
        row = random.randint(0, 9)
        col = random.randint(0, 9)

        ship8Vert = [[row, col]]
        ship8Hor = [[row, col]]
        global ship8
        ship8 = random.choice([ship8Hor, ship8Vert])

        if positionCheckV2(shipPositionList, ship8):
            isAvailable = True
            shipList.append(ship8)
        else:
            continue


def gameEnd(ocean, shiplist):
    for ships in shiplist:
        for index in range(len(ships)):
            ocean[ships[index][0]][ships[index][1]] = '*'.center(5)
    gameBoardPrinter(ocean)

def gamePlay(ocean, sankNoOfShips):
    moves = []
    rightMoves = []
    turn = 1
    while turn <= 15:
        try:  # Making sure only an integer is entered
            print('Your ' + f'{turn} . turn....')  # Remaining moves

            # Asking the player for input
            row = int(input('\nEnter the row number from the following "1,2,3,4,5,6,7,8,9,10" to send a torpedo: '))
            col = int(input('Enter the column number from the following "1,2,3,4,5,6,7,8,9,10" to send a torpedo: '))

            print('\n')
            if 1 <= row <= 10 and 1 <= col <= 10:
                move = [row-1, col-1]  # Converted the coordinates to a list
                # Checking if the move has already been made
                if move in moves:
                    print('!!!...WARNING...You have made this move before! \n')
                    continue
                else:
                    moves.append(move)  # Adding the move into the list of moves
                    ocean[row-1][col-1] = 'X'.center(5)  # Putting an 'X' if the torpedo didn't hit a ship
                    # Checking if the torpedo hit a ship

                    if move in ship1:
                        # Assuming one torpedo hit sinks any ship
                        # If torpedo hits a ship, the ship is revealed printing '*' by the length of the ship
                        ocean[ship1[0][0]][ship1[0][1]] = '*'.center(5)
                        ocean[ship1[1][0]][ship1[1][1]] = '*'.center(5)
                        ocean[ship1[2][0]][ship1[2][1]] = '*'.center(5)
                        ocean[ship1[3][0]][ship1[3][1]] = '*'.center(5)
                        print('Congratulations! You sank the 1. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)
                        for i in ship1:
                            moves.append(i)

                    if move in ship2:
                        ocean[ship2[0][0]][ship2[0][1]] = '*'.center(5)
                        ocean[ship2[1][0]][ship2[1][1]] = '*'.center(5)
                        ocean[ship2[2][0]][ship2[2][1]] = '*'.center(5)
                        ocean[ship2[3][0]][ship2[3][1]] = '*'.center(5)
                        for i in ship2:
                            moves.append(i)
                        print('Congratulations! You sank the 2. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship3:
                        ocean[ship3[0][0]][ship3[0][1]] = '*'.center(5)
                        ocean[ship3[1][0]][ship3[1][1]] = '*'.center(5)
                        ocean[ship3[2][0]][ship3[2][1]] = '*'.center(5)
                        for i in ship3:
                            moves.append(i)
                        print('Congratulations! You sank the 3. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship4:
                        ocean[ship4[0][0]][ship4[0][1]] = '*'.center(5)
                        ocean[ship4[1][0]][ship4[1][1]] = '*'.center(5)
                        ocean[ship4[2][0]][ship4[2][1]] = '*'.center(5)
                        for i in ship4:
                            moves.append(i)
                        print('Congratulations! You sank the 4. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship5:
                        ocean[ship5[0][0]][ship5[0][1]] = '*'.center(5)
                        ocean[ship5[1][0]][ship5[1][1]] = '*'.center(5)
                        for i in ship5:
                            moves.append(i)
                        print('Congratulations! You sank the 5. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship6:
                        ocean[ship6[0][0]][ship6[0][1]] = '*'.center(5)
                        ocean[ship6[1][0]][ship6[1][1]] = '*'.center(5)
                        for i in ship6:
                            moves.append(i)
                        print('Congratulations! You sank the 6. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship7:
                        ocean[ship7[0][0]][ship7[0][1]] = '*'.center(5)
                        for i in ship7:
                            moves.append(i)
                        print('Congratulations! You sank the 7. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)

                    if move in ship8:
                        ocean[ship8[0][0]][ship8[0][1]] = '*'.center(5)
                        for i in ship8:
                            moves.append(i)
                        print('Congratulations! You sank the 8. ship\n')
                        sankNoOfShips += 1
                        rightMoves.append(move)
                    gameBoardPrinter(ocean)
                    turn += 1
            else:
                print('\n!!!...WARNING...Enter an integer from the following "1,2,3,4,5,6,7,8,9,10"\n')
                continue
            if len(rightMoves) == 8:
                print('\nCONGRATULATIONS! YOU SANK ALL THE SHIPS.')
                quit()
            time.sleep(5)  # Pausing for 5 seconds
        except ValueError:
            print('Enter an integer from the following "1,2,3,4,5,6,7,8,9,10"')
    print(f'{turn - 1} Unfortunately you ran out of moves.....YOU LOST!' +
          '\nGame Report:\n'
          '\nYou sank ' + str(sankNoOfShips) + ' ships.'
          '\nThe ships were at the following positions:')
    gameEnd(ocean, shipPositionList)


gameStart()
gameBoardMaker()
gameBoardPrinter(ocean)
shipMaker(shipPositionList)
gamePlay(ocean, shipsHit)
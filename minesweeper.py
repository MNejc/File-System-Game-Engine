from engine import *
import random

dim = [16, 7]
avrgMines = 20



while 1:
    grass = dim[0] * dim[1]
    field = []
    opend = []
    mines = 0
    game = True

    for y in range(dim[1]):
        field.append([])
        for x in range(dim[0]):
            if random.randint(0,dim[0]*dim[1]) < avrgMines:
                field[y].append("X")
            else:
                field[y].append(0)

    for i,y in enumerate(field):
        for j,x in enumerate(y):
            if x != "X":
                for n in range(int(i==0)-1,2):
                    for m in range(int(j==0)-1,2):
                        try:
                            if field[i+n][j+m] == "X":
                                field[i][j] += 1
                        except:
                            pass
            else:
                mines += 1


    for y in range(dim[1]):
        for x in range(dim[0]):
            addButton(str(y) + chr(x + 97), "grass.ico", [x,y])

    while 1:
        time.sleep(.1)
        i = getInput()
        if i and game:
            y = int(i[0])
            x = ord(i[1]) - 97
            if field[y][x] == "X":
                addButton(str(y) + chr(x + 97), "mine.ico", [x,y])
                print("Game Over")
                for y in range(dim[1]):
                    for x in range(dim[0]):
                        if field[y][x] == "X":
                            addButton(str(y) + chr(x + 97), "mine.ico", [x,y])
                        else:
                            addButton(str(y) + chr(x + 97), "num"+str(field[y][x])+".ico", [x,y])
                addButton("restart","restart.ico",[5, 2])
                game = False
            elif not (x,y) in opend:
                addButton(str(y) + chr(x + 97), "num"+str(field[y][x])+".ico", [x,y])
                opend.append((x,y))
                grass -= 1
                if grass == mines:
                    print("Win")
                    for y in range(dim[1]):
                        for x in range(dim[0]):
                            if field[y][x] == "X":
                                addButton(str(y) + chr(x + 97), "trophy.ico", [x,y])
                    addButton("restart","restart.ico",[5, 2])
                    game = False
        if not game:
            if i == "restart":
                break

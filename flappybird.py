import random
from engine import *


## Const
dim = [11, 6]

while 1:
    ## Create play surface
    clear()
    for y in range(dim[1]):
        for x in range(dim[0]):
            addButton("jump", "sky.ico", [x,y])



    ## Variables
    birdPos = 3
    pipes = [[dim[0], random.randint(0, dim[1] - 2)]]
    countDownMax = 10
    countDown = countDownMax
    removeLastPipe = False
    dead = False
    birdUp = False
    game = True


    ## Game loop
    while 1:
        time.sleep(1.5)
        i = getInput()
        if game:
            addButton("jump","sky.ico",[3, birdPos])
            if i == "jump":
                birdPos -= 1
                birdUp = True
                winsound.Beep(100,500)
            else:
                birdPos += 1
                birdUp = False
            
            birdPos = max(min(birdPos, dim[1]-1), 0)


            for pipe in pipes:
                pipe[0] -= 1
                if (pipe[0] == 3 or pipe[0] == 2) and (birdPos != pipe[1] and birdPos != pipe[1] + 1):
                    dead = True
                for y in range(dim[1]):
                    if y != pipe[1] and y != pipe[1] + 1:
                        if pipe[0] >= 0:
                            if y == pipe[1]-1:
                                addButton("jump","pipeBL.ico",[pipe[0], y])
                            elif y == pipe[1]+2:
                                addButton("jump","pipeTL.ico",[pipe[0], y])
                            else:
                                addButton("jump","pipeL.ico",[pipe[0], y])
                        if pipe[0] < dim[0]-1:
                            if pipe[0]+1 >= 0:
                                if y == pipe[1]-1:
                                    addButton("jump","pipeBR.ico",[pipe[0]+1, y])
                                elif y == pipe[1]+2:
                                    addButton("jump","pipeTR.ico",[pipe[0]+1, y])
                                else:
                                    addButton("jump","pipeR.ico",[pipe[0]+1, y])
                            if pipe[0]+2 >= 0:
                                if pipe[0] < dim[0]-2:
                                    addButton("jump","sky.ico",[pipe[0]+2, y])
                            else:
                                removeLastPipe = True

                if removeLastPipe:
                    pipes.pop(0)
                    removeLastPipe = False


            countDown -= 1
            if not countDown:
                pipes.append([dim[0], random.randint(0, dim[1] - 2)])
                if countDownMax > 4:
                    countDownMax -= 1
                countDown = countDownMax




            if birdUp:
                addButton("jump","birdUp.ico",[3, birdPos])
            else:
                addButton("jump","birdDown.ico",[3, birdPos])
            if dead:
                game = False
                addButton("restart","restart.ico",[5, 2])
        else:
            if i == "restart":
                break




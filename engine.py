import shutil
import os
import winsound
import time
import win32com.client



dir = os.path.dirname(__file__)
spriteFolder = os.path.join(dir, "sprites/")
gameFolder = os.path.join(dir, "game/")
with open('engine/input.txt', "r+") as f:
    f.truncate(0)

def clear():
    for f in os.listdir(gameFolder):
        os.remove(gameFolder + f)


def addImage(img, pos):
    shutil.copyfile(spriteFolder + img, gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".png")


def removeItem(pos):
    if os.path.isfile(gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".png"):
        os.remove(gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".png")
    elif os.path.isfile(gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".lnk"):
        os.remove(gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".lnk")


def addButton(name, ico, pos):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(gameFolder + str(pos[1]) + chr(pos[0] + 97) + ".lnk")
    shortcut.Targetpath = os.path.join(dir, 'engine/input.bat')
    shortcut.Arguments  = name
    shortcut.IconLocation = os.path.join(spriteFolder, ico)
    shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()


def getInput():
    try:
        with open('engine/input.txt', "r+") as f:
            c = f.read()[:-1]
            f.truncate(0)
            return c
    except:
        return

## Snake game:
##\
## Created by Dan Buganim
import os
import time

## Handle variables in Player class
class Player:
    def __init__(self):
        pass

    def setPos(self, x, y):
        self._posY = y
        self._posX = x

    def setX(self, x):
        self._posX = x

    def setY(self, y):
        self._posY = y

    def getX(self):
        return self._posX

    def getY(self):
        return self._posY;
    
    def printPos(self):
        print(str(self._posX) + " " + str(self._posY))

player = Player()

file = open("snakeLevel.txt", 'r')
levelList = []

for i in file:
    levelList.append(i)
        

def cls():
    print('\n' * 20)


def printLevel():
    for i in levelList:
        print(i, end='')
    cls()

    
def load():        
    for y in levelList:
        for x in levelList[y]:
            _tile = levelList[y][x]

            ## Fix Postioning 
            if _tile == '@':
                player.setPos(x, y)


def gameLoop():
    while True:
        printLevel()
        time.sleep(0.15)
    
gameLoop()

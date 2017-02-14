# Imports
from turtle import *
from time import *
import random

title("Dots-N-Boxes")
screen = getscreen()
screen.listen()
hideturtle() # Hide the turtle icon, cuz it's ugly
tracer(0,0) # Used to remove turtle animation, update() to refresh screen now
screen.setworldcoordinates(0,0,500,500) # Set screen cordinates to quadrant 1 only
penup()

# There are two main variables we use here:
# 1. A seperate variable for each line, which allows easier screen drawing and checking for errors
# 2. A seperate variable for each box some belonging to more than one line, which allows for easier win checking
verticals = [0,0,0,0,0,0,0,0,0,0,0,0] # Read from bottom left to upper right
horizontals = [0,0,0,0,0,0,0,0,0,0,0,0]
#boxes = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
turn = 1

def drawDots():
    goto(100,100)
    for i in range(1,5):
        for i in range(1,5):
            dot(10)
            forward(100)
        goto((xcor() - 400),(ycor() + 100))
    update()


def getInput():
    check = onscreenclick(clickHandler)
    mainloop()
    print(check)

def clickHandler(rawx,rawy):
    x = int(rawx//1) # Round click to a full int
    y = int(rawy//1)
    for xnum in range(1,5):
        tempx = (xnum % 4) + 1
        for ynum in range(1,4):
            tempy = (ynum % 3) + 1
            if ((tempx * 100) + 10) >= x >= ((tempx * 100) - 10) and ((tempy * 100) + 90) >= y >= ((tempy * 100) + 10):
                onscreenclick(None)
                updateVariable(tempx, tempy, True)
    for xnum in range(1,4):
        tempx = (xnum % 3) + 1
        for ynum in range(1,5):
            tempy = (ynum % 4) + 1
            if ((tempx * 100) + 90) >= x >= ((tempx * 100) + 10) and ((tempy * 100) + 10) >= y >= ((tempy * 100) - 10):
                onscreenclick(None)
                updateVariable(tempx, tempy, False)
    print("Click on a space")

def updateVariable(x, y, isVertical):
    global verticals
    global horizontals
    if isVertical:
        verticals[((y - 1) * 4 + x)-1] = 1
    else:
        horizontals[((y - 1) * 3 + x)-1] = 1
    drawLines()



def drawLines():
    global turn
    for xnum in range(1,5): # 4
        for ynum in range(1,4): # 3
            if verticals[((ynum - 1) * 4 + xnum) - 1] != 0:
                goto((100 * xnum), (100 * ynum))
                pendown()
                goto((100 * xnum), (100 * (ynum + 1)))
                penup()
    for xnum in range(1,4):
        for ynum in range(1,5):
            if horizontals[((ynum - 1) * 3 + xnum) - 1] != 0:
                goto((100 * xnum), (100 * ynum))
                pendown()
                goto((100 * (xnum + 1)), (100 * ynum))
                penup()
    if turn == 1:
        turn = 2
    else:
        turn = 1
    main()

def checkForWin():
    # Might need to clean this up
    if 0 not in horizontals[1]


def main():
    print("Player " + str(turn) + " is up")
    drawDots()
    getInput()
main()

screen._root.mainloop() # Stops program from quitting while waiting for input

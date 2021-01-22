'''
Application that bounce circle from window borders
- ruch odbijania sie w x - okey
- ruch odbijania sie w y - okey
- ruch odbijania sie w x i y - okey
- tworzenie klas i obiektow - tzw. refaktoring

'''

import graphics
from random import randint
from time import sleep


def move_object_by_step(figure: graphics.Circle, dx: int = 1, dy: int = 1, repetitions: int = 10):
    while True:

        currentFigureCenter = figure.getCenter()
        print(currentFigureCenter.x, currentFigureCenter.y)

        if (currentFigureCenter.x + circleRadius >= winMain.getWidth()):
            dx = -dx
        if (currentFigureCenter.x - circleRadius <= 0):
            dx = -dx
        if (currentFigureCenter.y + circleRadius >= winMain.getHeight()):
            dy = -dy
        if (currentFigureCenter.y - circleRadius <= 0):
            dy = -dy
        figure.move(dx, dy)
        if (winMain.checkMouse()) != None:
            break
        sleep(0.03)




#window parameters
windowWidth = 400
windowHeight = windowWidth
winMain = graphics.GraphWin(
    title='Bounce', width=windowWidth, height=windowHeight)
winMainColor = graphics.color_rgb(100, 200, 100)
winMain.setBackground(winMainColor)

#picking up point for start
message = graphics.Text(graphics.Point(
    winMain.getWidth()/2, 10), 'Click on place to start bouncing ball.')
message.draw(winMain)

circleCenterPickUp = winMain.getMouse()

#circle parameters and drawing first circle
circleCenter = graphics.Point(
    randint(circleRadius, winMain.width -
            circleRadius), randint(circleRadius, winMain.height - circleRadius))
circleRadius = randint(5, 40)
circle = graphics.Circle(circleCenterPickUp, circleRadius)
circleColor = graphics.color_rgb(20, 120, 20)
circle.setFill(circleColor)
circle.draw(winMain)

#some message
message.setSize(8)
message.setText('Click anywhere in window to close window. Sometimes, click few times.')

#randomize increments in move
dx = randint(1, 10)
dy = randint(1, 10)


#moving circle around
move_object_by_step(circle, dx, dy, 250)


# program ending
winMain.close()

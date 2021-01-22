'''
Application that bounce circle from window borders
'''

import graphics
from random import randint
from time import sleep


class CircleBounce(graphics.Circle):
    """ Class inheritance from graphics.Circle, with added movement method"""

    def __init__(self, windowName: graphics.GraphWin):
        self.windowName = windowName

        self.message = graphics.Text(graphics.Point(self.windowName.getWidth()/2, 10),
                                     'Click on place to start bouncing ball.')
        self.message.draw(self.windowName)

        self.circleRadius = randint(5, 40)
        self.circleCenterPickUp = self.windowName.getMouse()

        super().__init__(self.circleCenterPickUp, self.circleRadius)
        self.setFill(graphics.color_rgb(20, 120, 20))
        self.draw(self.windowName)

        self.dx = randint(1, 10)
        self.dy = randint(1, 10)

        return print('Class initialized')

    def move_object_by_step(self):
        while True:

            currentFigureCenter = self.getCenter()
            print(currentFigureCenter.x, currentFigureCenter.y)

            if (currentFigureCenter.x + self.circleRadius >= self.windowName.getWidth()):
                self.dx = -self.dx
            if (currentFigureCenter.x - self.circleRadius <= 0):
                self.dx = -self.dx
            if (currentFigureCenter.y + self.circleRadius >= self.windowName.getHeight()):
                self.dy = -self.dy
            if (currentFigureCenter.y - self.circleRadius <= 0):
                self.dy = -self.dy
            self.move(self.dx, self.dy)
            if (self.windowName.checkMouse()) != None:
                break
            sleep(0.03)


# window parameters
windowWidth = 400
windowHeight = windowWidth
winMain = graphics.GraphWin(
    title='Bounce', width=windowWidth, height=windowHeight)
winMain.setBackground(graphics.color_rgb(100, 200, 100))


CircleBounce(winMain).move_object_by_step()


# program ending
winMain.close()

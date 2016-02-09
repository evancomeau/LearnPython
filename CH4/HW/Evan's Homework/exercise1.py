import graphics
from graphics import Rectangle
from graphics import Point
from graphics import Text
def main():
    win = graphics.GraphWin()
    shape = Rectangle(Point(75,75),Point(125,125))
    shape.setOutline('Red')
    shape.setFill('Red')
    shape.draw(win)
 
    for i in range(10):
        p = win.getMouse()
        tx = p.getX()-25
        ty = p.getY()-25
        bx = p.getX()+25
        by = p.getY()+25
 
        Rectangle(Point(tx,ty),Point(bx,by)).draw(win)
 
    Text(Point(100,180),'Click again to quit!').draw(win)
    win.getMouse()
    win.close()

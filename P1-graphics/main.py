# Render some graphics
# using this as a starting point: https://www.youtube.com/watch?v=IpiVXHcSBSw

# get the python version: python -V (or python --version)
# install "graphics" package: pip3 install --user http://bit.ly/csc161graphics
# run: python3 main.py

from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(250,250), "what's up?")
    txt.setTextColor(color_rgb(0,125,255))
    txt.setSize(30)
    txt.setFace('courier')
    txt.draw(win)

    win.getMouse()
    win.close()



main()
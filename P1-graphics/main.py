# Render some graphics
# using this as a starting point: https://www.youtube.com/watch?v=IpiVXHcSBSw

# get the python version: python -V (or python --version)
# install "graphics" package: pip3 install --user http://bit.ly/csc161graphics
# run: python3 main.py

from graphics import *

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0,0,50))

    win.getMouse()
    win.close()



main()
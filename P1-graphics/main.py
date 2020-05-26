# Render some graphics
# using this as a starting point: https://www.youtube.com/watch?v=IpiVXHcSBSw

# get the python version: python -V (or python --version)
# install "graphics" package: pip3 install --user http://bit.ly/csc161graphics
# pip3 install keyboard
<<<<<<< Updated upstream
# pip3 install opencv-python
# pylint --extension-pkg-whitelist=cv2
# run: python3 main.py

from graphics import *
import time
#import keyboard 
=======
# run: python3 main.py

from graphics import *
>>>>>>> Stashed changes
import cv2

def main():
    win = GraphWin("My Window", 500, 500)
    win.setBackground(color_rgb(0,0,0))

    txt = Text(Point(250,250), "what's up?")
    txt.setTextColor(color_rgb(0,125,255))
    txt.setSize(30)
    txt.setFace('courier')
    txt.draw(win)
    #time.sleep(2)
    txt.move(10,40)
    txt.move(13,43)
    
    
    while True: 
        key = cv2.waitKey(1) & 0xFF  #get key being pressed
        if key == 27:
            win.close()
        elif key != 255:
            print(key)
    win.getMouse()
    win.close()


main()
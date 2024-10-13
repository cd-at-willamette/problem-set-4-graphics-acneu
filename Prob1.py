############################################################
# Name: Anika Neu
# Name(s) of anyone worked with: 
# Est time spent (hr): 1.5
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 400
HEIGHT = 400

def draw_image():

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!

    #background
    rectangle = GRect(0, 290, 400, 400)
    rectangle.set_color('Black')
    rectangle.set_filled(True)
    gw.add(rectangle)

    rectangle = GRect(0, 290, 400, 60)
    rectangle.set_color('Grey')
    rectangle.set_filled(True)
    gw.add(rectangle)

    line = GLine(0, 350, 400, 350)
    line.set_color('White')
    gw.add(line)

    #handle
    oval = GOval(240, 190, 150, 120)    
    oval.set_color('Black')
    oval.set_filled(True)
    gw.add(oval)

    oval= GOval(220, 200, 150, 100)
    oval.set_color('White')
    oval.set_filled(True)
    gw.add(oval)

    # cup
    oval = GOval(150, 150, 200, 190)
    oval.set_color('Black')
    oval.set_filled(True)
    gw.add(oval)

    # coffee
    oval = GOval(155,150,190,100)
    oval.set_color('Brown')
    oval.set_filled(True)
    gw.add(oval)

    oval = GOval(170, 170, 100, 50)
    oval.set_color('White')
    oval.set_filled(True)
    gw.add(oval)

    oval = GOval(180, 165, 100, 50)
    oval.set_color('Brown')
    oval.set_filled(True)
    gw.add(oval)

    # I love coffee!!
    label = GLabel('I love coffee!!', 50, 50)
    gw.add(label)

    label = GLabel("(Who doesn't?)", 50, 70)
    gw.add(label)

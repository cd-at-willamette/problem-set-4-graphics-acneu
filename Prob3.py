########################################
# Name: Anika Neu
# Collaborators: Quad Center & Deidrik Boberg
# Estimate time spent (hrs): 2
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score


def clicky_box():
# The mouse location and what happens when the box is pressed 
    def on_mouse_down(event):
        x = squ.get_x()
        y = squ.get_y()
 # x and y coordinate of the square
        xs = random.randint(0, GW_WIDTH - SQUARE_SIZE)
        ys = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
# x and y coordinate of the mouse
        xm = event.get_x()
        ym = event.get_y()
# Comparison between the two
        if xm >= x and xm <= x + SQUARE_SIZE and ym >= y and ym <= y + SQUARE_SIZE:
            squ.set_location(xs, ys)
            gw.count += 1
            label.set_label(str(gw.count))
# Label resets to 0 if the square is not clicked
        else:
            gw.count = 0
            label.set_label(str(gw.count))

    gw = GWindow(GW_WIDTH, GW_HEIGHT)

# Making my square
    xc = GW_WIDTH/2 - SQUARE_SIZE/2
    yc = GW_HEIGHT/2 - SQUARE_SIZE/2
# Setting my square color and location
    squ = GRect(xc, yc, SQUARE_SIZE, SQUARE_SIZE)
    squ.set_color('Pink')
    squ.set_filled(True)
    gw.add(squ)

# Adding my label
    gw.count = 0
    label = GLabel(str(gw.count), SCORE_DX, GW_HEIGHT - SCORE_DY)
    label.set_font(SCORE_FONT)
    gw.add(label)

# Call mouse down function with the click
    gw.add_event_listener("click", on_mouse_down)

if __name__ == '__main__':
    clicky_box()

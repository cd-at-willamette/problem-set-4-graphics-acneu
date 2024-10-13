########################################
# Name: Anika Neu
# Collaborators: Quad Center
# Estimated time spent (hrs): 1
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

# Defining the rectangle's dimensions and making sure the outline of the bricks is black and the middle is clear
    def my_rect(x,y,w,h): 
        rect = GRect(x,y,w,h)
        rect.set_filled(False)
        gw.add(rect)

# Creating the bricks that are centered in the middle of the screen, go down by one when counting from the bottom row to the top, and have them vary by half a brick
    def n_bricks():
        for y in range(BRICKS_IN_BASE):
            for x in range(1, y+2):
                my_rect(((WIDTH/2 - BRICK_WIDTH/2) - y * BRICK_WIDTH/2 + x * BRICK_WIDTH - BRICK_WIDTH), ((HEIGHT/2 - (BRICKS_IN_BASE/2 * BRICK_HEIGHT)) + BRICK_HEIGHT * y), BRICK_WIDTH, BRICK_HEIGHT)

# Calling the function
    n_bricks()

if __name__ == '__main__':
    draw_pyramid()

import random
class Bush:
    each = []
    WIDTH = 0
    HEIGHT = 0
    orientation = 4
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #the bush will be the only one in the square 
        #but the square is bigger than the bush 
        #so there is some grass in the square
        #these allows us images with different height and width
        self.max_rabbit = 3

        #directly linked to the one on top
        self.number_of_rabbit = 0
        #states represents the number of rabbit in the bush
        #also usefull for the function display in MainActivity (same for rabbit, bush and whole)
        self.looking_state = 0



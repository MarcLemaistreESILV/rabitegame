import random
class Bush:
    each_bush = []
    def __init__(self, column, ligne, width, height):
        self.ligne = ligne #y
        self.column = column #x
        #the bush will be the only one in the square 
        #but the square is bigger than the bush 
        #so there is some grass in the square
        #these allows us images with different height and width
        self.relative_x = random.randint(0, 2*width)-width
        self.relative_y = random.randint(0, 2*height)-height
        self.width = width
        self.height = height
        self.max = 3

        #directly linked to the one on top
        self.number_of_rabbit = 0
        #states represents the number of rabbit in the bush
        #also usefull for the function display in MainActivity (same for rabbit, bush and whole)
        self.looking_state = 0



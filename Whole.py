import random
class Whole:
    each_whole =  []
    WIDTH = 0
    HEIGHT = 0
    def __init__(self, column, ligne):
        self.ligne = ligne#y
        self.column = column#x
        self.relative_x = random.randint(0, 2*self.WIDTH)-self.WIDTH
        self.relative_y = random.randint(0, 2*self.HEIGHT)-self.HEIGHT
        self.width = self.WIDTH
        self.height = self.HEIGHT
        self.max_whole = 5

        #random value that will never be exceed because to big
        self.max = 100
        self.number_of_rabbit = 0
        #directly linked to the one on top
        self.has_rabbit = False
        #two states possible dark or light whole. 
        #also usefull for the function display in MainActivity (same for rabbit, bush and whole)
        self.looking_state = 0
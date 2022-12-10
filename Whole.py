import random
class Whole:
    each =  []
    WIDTH = 0
    HEIGHT = 0
    orientation = 5
    def __init__(self, x, y):
        self.x = x
        self.y =y
        #random value that will never be exceed because to big
        self.max_rabbit = 100
        self.number_of_rabbit = 0
        #two states possible dark or light whole. 
        #also usefull for the function display in MainActivity (same for rabbit, bush and whole)
        self.looking_state = 0
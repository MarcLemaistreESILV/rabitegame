import random
class Whole:
    each_whole =  []
    def __init__(self, column, ligne, width, height):
        self.ligne = ligne#y
        self.column = column#x
        self.relative_x = random.randint(0, 2*width)-width
        self.relative_y = random.randint(0, 2*height)-height
        self.width = width
        self.height = height
        self.max_whole = 5

        #random value that will never be exceed because to big
        self.max = 100
        self.number_of_rabbit = 0
        #directly linked to the one on top
        self.has_rabbit = False
        #two states possible dark or light whole. 
        #also usefull for the function display in MainActivity (same for rabbit, bush and whole)
        self.looking_state = 0
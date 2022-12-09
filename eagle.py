import random
import pygame
class Eagle:         
#there are three possibilities in my minde
#first the screen is hidden by the eagle and rabbits disappear
#secound eagle move toward the screen but "slowly" and seek a rabbit
#third eagle move toward the screen but "slowly" in a specific direction
#fourth eagle moves at its own rapidity (futur improvments)
#let's take the third (for improvments secound is much more fun)
    each_eagle = []
    #design features
    WIDTH = 0
    HEIGHT = 0
    def __init__(self, column, ligne):
        #moving features
        self.relative_x =0
        self.relative_y =0
        self.column = 0
        self.ligne = 0
        self.target_column = 0
        self.target_ligne = 0
        self.column_increment = 0
        self.ligne_increment= 0
        self.new_target(column, ligne)        
        self.each_eagle.append(self)
    
    @staticmethod
    def set_increment(start, end):
        #return an int stating in wich way to increment
        #inputs: starting ligne/column and arrivings
        increment = 1
        if start > end:
            increment=-1
        elif start == end:
            increment = 0
        return increment
    def new_target(self, columns, lignes):
        starting_border = random.randint(0,3)
        match starting_border:
            case 0:#en haut
                self.column = random.randint(0, columns)
                self.ligne = 0
                self.target_column = random.randint(0, columns)
                self.target_ligne = lignes
                self.ligne_increment =1
                self.column_increment = Eagle.set_increment(self.column, self.target_column)
            case 1:#en bas
                self.column = random.randint(0, columns)
                self.ligne =lignes
                self.target_column = random.randint(0, columns)
                self.target_ligne = 0
                self.ligne_increment=-1
                self.column_increment = Eagle.set_increment(self.column, self.target_column)
            case 2:#à gauche
                self.column = 0
                self.ligne = random.randint(0, lignes)
                self.target_column = columns
                self.target_ligne = random.randint(0, lignes)
                self.column_increment = 1
                self.ligne_increment = Eagle.set_increment(self.ligne, self.target_ligne)
            case 3:#à droite
                self.column = columns
                self.ligne = random.randint(0, lignes)
                self.target_column = 0
                self.target_ligne = random.randint(0, lignes)
                self.column_increment = -1
                self.ligne_increment = Eagle.set_increment(self.ligne, self.target_ligne)
    def move(self):
        is_arrived = True
        if self.column != self.target_column:
            self.relative_x +=self.column_increment*10
            is_arrived = False
            if abs(self.WIDTH) < abs(self.relative_x):
                self.column +=self.column_increment
                self.relative_x=0
        if self.ligne != self.target_ligne:
            self.relative_y += self.ligne_increment*10
            is_arrived = False
            if abs(self.HEIGHT) < abs(self.relative_y):
                self.ligne +=self.ligne_increment
                self.relative_y=0
        if is_arrived:
            self.kill_eagle()
    def kill_rabbit(self, rabbits):
        rabbits_killed = []
        for rabbit in rabbits:
            if rabbit.column == self.column & rabbit.ligne == self.ligne:
                #just so they really overlapp each other
                if abs(rabbit.relative_x-self.relative_x)<20 & abs(rabbit.relative_y-self.relative_y)<20:
                    if not rabbit.hidden:
                        rabbits_killed.append(rabbit)
        return rabbits_killed
    def kill_eagle(self):
        for eagle in self.each_eagle:
            if self == eagle:
                self.each_eagle.remove(eagle)
                break
    


    



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
    def __init__(self, COLUMN, LIGNE):
        self.relative_x =0
        self.relative_y =0
        self.column = 0
        self.ligne = 0
        self.target_column = 0
        self.target_ligne = 0

        self.new_target(COLUMN, LIGNE)
        self.ligne_increment= (abs(self.ligne-self.target_ligne)/(self.ligne-self.target_ligne))
        self.column_increment = (abs(self.column-self.target_column)/(self.column-self.target_column))

        self.each_eagle.append(self)
    
    def new_target(self, columns, lignes):
        starting_border = random.randint(0,4)
        match starting_border:
            case 0:#en haut
                self.column = random.randint(0, columns)
                self.ligne = 0
                self.target_column = random.randint(0, columns)
                self.target_ligne = lignes
            case 1:#en bas
                self.column = random.randint(0, columns)
                self.ligne =lignes
                self.target_column = random.randint(0, columns)
                self.target_ligne = 0
            case 2:#à gauche
                self.column = 0
                self.ligne = random.randint(0, lignes)
                self.target_column = columns
                self.target_ligne = random.randint(0, lignes)
            case 3:#à droite
                self.column = columns
                self.ligne = random.randint(0, lignes)
                self.target_column = 0
                self.target_ligne = random.randint(0, lignes)
    def move(self):
        is_arrived = True
        if self.column != self.target_column:
            self.relative_x +=self.column_increment*10
            is_arrived = False
            if abs(self.width) < abs(self.relative_x):
                self.column +=self.column_increment
                self.relative_x=0
        if self.ligne != self.target_ligne:
            self.relative_y += self.ligne_increment*10
            is_arrived = False
            if abs(self.height) < abs(self.relative_y):
                self.ligne +=self.ligne_increment
                self.relative_y=0
        if is_arrived:
            self.kill_eagle()
    def kill_rabbit(self, rabbits):
        rabbits_killed = []
        for rabbit in rabbits:
            if rabbit.column == self.column & rabbit.ligne == self.ligne:
                if not rabbit.hidden:
                    rabbits_killed.append(rabbit)
        return rabbits_killed
    def kill_eagle(self):
        for eagle in self.each_eagle:
            if self == eagle:
                self.each_eagle.remove(eagle)
                break
    


    



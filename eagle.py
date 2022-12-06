import random
import pygame
import keyboard
import MainActivity as main
class Eagle:         
#there are three possibilities in my minde
#first the screen is hidden by the eagle and rabbits disappear
#secound eagle move toward the screen but "slowly" and seek a rabbit
#third eagle move toward the screen but "slowly" in a specific direction
#let's take the third (for improvments secound is much more fun)

    def __init__(self, columns = main.COLUMN, lignes = main.LIGNE):
        starting_border = random.randint(0,4)
        match starting_border:
            case 0:
                self.column = random.randint(0, columns)
                self.ligne = 0
                self.targt_column = random.randint(0, columns)
                self.target_ligne = lignes
            case 1:
                self.column = random.randint(0, columns)
                self.ligne =lignes
                self.targt_column = random.randint(0, columns)
                self.target_ligne = 0
            case 2:
                self.column = 0
                self.ligne = random.randint(0, lignes)
                self.targt_column = columns
                self.target_ligne = random.randint(0, lignes)
            case 3:
                self.column = columns
                self.ligne = random.randint(0, lignes)
                self.targt_column = 0
                self.target_ligne = random.randint(0, lignes)
        main.each_eagle.append(self)

    



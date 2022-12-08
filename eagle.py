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
        self.hunting = True
        self.relative_x =0
        self.relative_y =0
        match starting_border:
            case 0:
                self.column = random.randint(0, columns)
                self.ligne = 0
                self.target_column = random.randint(0, columns)
                self.target_ligne = lignes
            case 1:
                self.column = random.randint(0, columns)
                self.ligne =lignes
                self.target_column = random.randint(0, columns)
                self.target_ligne = 0
            case 2:
                self.column = 0
                self.ligne = random.randint(0, lignes)
                self.target_column = columns
                self.target_ligne = random.randint(0, lignes)
            case 3:
                self.column = columns
                self.ligne = random.randint(0, lignes)
                self.target_column = 0
                self.target_ligne = random.randint(0, lignes)
        main.each_eagle.append(self)
    def move(self):
        eagle_animation = pygame.time.Clock
        #we prepare for a fast loop
        #both are float
        number_of_column = self.column - self.target_column
        number_of_line = self.ligne - self.target_ligne
        increment_column = 1
        increment_ligne = 1
        if number_of_column <0:
            increment_column = -1
        if number_of_line <0:
            increment_ligne = -1
        #we don't have to test each we just fly till the number of columns and lines
        #if a < b
        big = 0
        small = 0
        if -number_of_column*increment_column < -number_of_line*increment_ligne:
            big = -number_of_line*increment_ligne
            small = -number_of_column*increment_column
            #we increment the missing part
            for j in range(small, big):
                #increment one square
                for i in range(0, main.WIDTH_SQUARE):
                    self.relative_y += increment_ligne*10
                    eagle_animation.tick(200)
                self.relative_y += 0
                self.ligne += increment_ligne
        else:
            small = -number_of_line*increment_ligne
            big = -number_of_column*increment_column
            for j in range(small, big):
                #increment one square
                for i in range(0, main.WIDTH_SQUARE):
                    self.relative_x += increment_column*10
                    eagle_animation.tick(200)
                self.relative_x += 0
                self.column += increment_column
        #we increment the common part
        for j in range(0, big):
            #increment one square
            for i in range(0, main.WIDTH_SQUARE):
                self.relative_x += increment_column*10
                self.relative_y += increment_ligne*10
                eagle_animation.tick(200)
            self.relative_x += 0
            self.relative_y += 0
            self.column += increment_column
            self.ligne += increment_ligne
    def eat_rabbit(self, rabbits):
        for rabbit in rabbits:
            if rabbit.column == self.column & rabbit.ligne == self.ligne:
                if not rabbit.hidden:
                    if rabbit.player == True:
                        print("looser")
                        break
                    else:
                        main.each_rabbit.remove(rabbit)
                        print("rabbit was killed")
    


    



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
    SCREEN_SIZE_X = 0
    SCREEN_SIZE_Y = 0
    def __init__(self, x, y):
        #moving features
        self.x = x
        self.y = y
        #futur improvment moove by vector
        self.x_target = 0
        self.y_target = 0
        self.new_target()        
        self.each_eagle.append(self)
        self.angle = 0
    @staticmethod
    def set_increment(start, end):
        #return an int stating in wich way to increment
        #inputs: starting y/x and arrivings
        increment = 1
        if start > end:
            increment=-1
        elif start == end:
            increment = 0
        return increment
    def new_target(self):
        starting_border = random.randint(0,3)
        match starting_border:
            case 0:#en haut
                self.x = random.randint(0, Eagle.SCREEN_SIZE_X)
                self.y = 0
                self.x_target = random.randint(0, Eagle.SCREEN_SIZE_X)
                self.y_target = Eagle.SCREEN_SIZE_Y
                self.y_increment =1
                self.x_increment = Eagle.set_increment(self.x, self.x_target)
            case 1:#en bas
                self.x = random.randint(0, Eagle.SCREEN_SIZE_X)
                self.y =Eagle.SCREEN_SIZE_Y
                self.x_target = random.randint(0, Eagle.SCREEN_SIZE_X)
                self.y_target = 0
                self.y_increment=-1
                self.x_increment = Eagle.set_increment(self.x, self.x_target)
            case 2:#à gauche
                self.x = 0
                self.y = random.randint(0, Eagle.SCREEN_SIZE_Y)
                self.x_target = Eagle.SCREEN_SIZE_X
                self.y_target = random.randint(0, Eagle.SCREEN_SIZE_Y)
                self.x_increment = 1
                self.y_increment = Eagle.set_increment(self.y, self.y_target)
            case 3:#à droite
                self.x = Eagle.SCREEN_SIZE_X
                self.y = random.randint(0, Eagle.SCREEN_SIZE_Y)
                self.x_target = 0
                self.y_target = random.randint(0, Eagle.SCREEN_SIZE_Y)
                self.x_increment = -1
                self.y_increment = Eagle.set_increment(self.y, self.y_target)
    def move(self):
        is_arrived = True
        self.angle =0
        if self.x < self.x_target:
            if self.y < self.y_target:
                self.x +=1
                self.y+=1
                self.angle = 315
            elif self.y > self.y_target:
                self.x +=1
                self.y-=1
                self.angle = 45
            else:
                self.x +=1
                self.angle = 0
        elif self.x > self.x_target:
            if self.y < self.y_target:
                self.x -=1
                self.y+=1
                self.angle = 225
            elif self.y > self.y_target:
                self.x -=1
                self.y-=1
                self.angle = 135
            else:
                self.x -=1
                self.angle = 180
        elif self.y < self.y_target:
            self.y+=1
            self.angle = 270
        elif self.y > self.y_target:
            self.y-=1
            self.angle = 90
        else:
            self.kill_eagle()
        self.angle+=90
    def kill_rabbit(self, rabbits):
        rabbits_killed = []
        for rabbit in rabbits:
                if abs(self.x-rabbit.x) < (int)(Eagle.WIDTH/5) and abs(self.y-rabbit.y) < (int)(Eagle.HEIGHT/5):
                    if rabbit.hidden <= 0:
                        rabbits_killed.append(rabbit)
        return rabbits_killed
    def kill_eagle(self):
        for eagle in self.each_eagle:
            if self == eagle:
                self.each_eagle.remove(eagle)
                break
    


    



import random
import pygame
from Eagle import Eagle
from Bush import Bush
from Whole import Whole

class Rabbit:         
    each_rabbit = []
    COLUMN = 0
    LIGNE = 0
    WIDTH =0 
    HEIGHT =0
    def __init__(self, column, ligne, fastness_mother=10, color = 1):
        #for futur improvments create gens for:
        #color, fastness, sensibility, alerting capabilities, number of child
        #feature
        self.orientation = 0#(up,down,left, right, hide, invisible)=(0,1,2,3,4,5)
        self.posture = 0
        
        #rabbit genes
        self.fastness = fastness_mother+5-random.randint(0, 10)
        self.age = 0
        self.alerting_capabilities = 3
        self.color = color#0=orange 1=blue....
        self.sensibility = 10

        #for the game
        self.hide_object = None
        self.alert = False
        self.hidden = 0#because we have a timer when he unhide
        self.pregnant = False   
        self.player = False

        #positionnal
        self.column = column
        self.ligne = ligne
        self.relative_x = 0
        self.relative_y = 0
        #targeted point
        self.target_column = 0
        self.target_ligne = 0
        self.new_target()#has to know some of its parameters (alert)
      
    def love(self):
        #check if any rabbit is avaible and love with the one he can
        for rabbit in self.each_rabbit:
            if rabbit != self:
                if rabbit.column == self.column and rabbit.ligne == self.ligne:
                    self.each_rabbit.append(Rabbit(self.column, self.ligne, self.WIDTH, self.HEIGHT, rabbit.fastness, rabbit.color))
                    break
    #----------------------alerting & hiding
    def alerted(rabbit):
        #alerts a rabbit
        if random.randint(0, rabbit.sensibility) < 100:#should be 2 or 3 in real game
            rabbit.alert = True
            rabbit.find_hide()
            print("e")
    def alerts(self): 
        #alerts every rabbits around it    
        #check rabbits around
        for rabbit in self.each_rabbit:
            if not rabbit.alert:
                if abs(rabbit.column-self.column) < self.alerting_capabilities:
                    rabbit.alerted()
        #check if sees an eagle (sometme false alert)
        if random.randint(0, (int)(self.sensibility/(len(Eagle.each_eagle)+1))) > 20:
            self.alerted()
    def find_hide(self):        
        hide = self.closest_hide()
        self.target_column = hide.column
        self.target_ligne = hide.ligne
        self.hide_object = hide
        print(self.hide_object.number_of_rabbit)
    def closest_hide(self):
        total_distance = 100
        total_hide = None
        for hides in [Whole.each, Bush.each]:
            for hide  in hides:
                distance = abs(hide.column-self.column)+abs(hide.ligne-self.ligne)
                #if equals to 0 it meens he is on the hide
                #so if he is on a hide but he can't hide, the hide is full
                if distance != 0 and total_distance > distance:
                    total_distance = distance
                    total_hide = hide
        return total_hide
    def can_hide(self):
        #find closest hide where he can hide and return it
        if self.hide_object.number_of_rabbit < self.hide_object.max_rabbit:
            return True
        else:
            return False
    def hide(self):
        if self.can_hide():
            self.hidden = 1
            self.hide_object.number_of_rabbit +=1
            self.column =  self.hide_object.column
            self.ligne =  self.hide_object.ligne
            self.relative_x = random.randint(0, self.hide_object.WIDTH)
            self.relative_y = random.randint(0, self.hide_object.HEIGHT)
            self.orientation = self.hide_object.orientation
        else:
            self.hide_object = None
            self.find_hide() 
    def unhide(self):
        #hide or unhide the rabbit, affects also the hide's object
        self.hide_object.number_of_rabbit -=1
        self.hide_object = None
        self.alert = False
        self.hidden = 0
    #----------------------end of alerting and hiding
    def new_eagle(self):
        if random.randint(0, 10) > 0:#0-> 9 //mofify just for debugging
            Eagle(self.COLUMN, self.LIGNE)
        self.alerted()
        if self.alert == True:
            self.alerts()
    def new_target(self):
        #find new target or new hide or hide
        #maybefutur improvment find if there is the place befor going?
        #set target
        self.target_column = random.randint(0, self.COLUMN-1) 
        self.target_ligne = random.randint(0, self.LIGNE-1)
    #---------------------start of positionnal block
    def direction(self):
        #finds the right direction and calls move_command
        #can also change target (if achieve)
        #to make the move more natural (not linear moves)
        if random.randint(0,1) == 0:
            self.direction_column()
        else:
            self.direction_ligne()
    def direction_column(self):
        if self.column < self.target_column:
            #we are already certain the rabbit won't leave the screen for too lang
            self.move([False, False, False, True])
        elif self.column > self.target_column:
            self.move([False, False, True, False])
        elif self.ligne != self.target_ligne:
            self.direction_ligne()
        else:
            self.arrived()
    def direction_ligne(self):
        if self.ligne > self.target_ligne:
        #we are already certain the rabbit won't leave the screen for too lang
            self.move([True, False, False, False])
        elif self.ligne < self.target_ligne:
            self.move([False,True, False, False])
        elif self.column != self.target_column:
            self.direction_column()
        else:
            self.arrived()
    def arrived(self):
        #he is arrived at the target point so we have to possibilities:
        #he stays hidden or hide
        #he finds a new target
        if self.alert == True :
            self.hide()
        else:
            self.new_eagle()
            self.new_target()
    def collision(self, object):
        #returns true if collision, false otherwise
        if abs(self.column-object.column) <= 1 and abs(self.ligne-object.ligne) <= 1:
            absolute_position_rabbit_x = self.relative_x+self.column*50
            absolute_position_rabbit_y = self.relative_y+self.ligne*50
            absolute_position_object_x = object.relative_x+object.column*50
            absolute_position_object_y = object.relative_y+object.ligne*50
            if abs(absolute_position_rabbit_x-absolute_position_object_x) < (int)(object.WIDTH/2) and abs(absolute_position_rabbit_y-absolute_position_object_y) < (int)(object.HEIGHT/2):
                return True
            else:
                return False
    #---------------------start of action
    def move(self, direction):
        #input any rabbit (even the player) with a table giving its position [true, false, false,false]
        #finds the new picture and the new position
        #enter the move section
        if direction[0]:#up
            #print("up")
            if self.relative_y-1 < 0:
                if self.ligne>=0:
                    self.relative_y = self.HEIGHT
                    self.ligne = self.ligne-1
            else:
                self.relative_y = self.relative_y-1
            self.orientation = 0
        elif direction[1]:#down
            #print("down")
            if self.relative_y+1 > self.HEIGHT:
                if self.ligne < self.LIGNE:
                    self.relative_y = 0
                    self.ligne = self.ligne+1
            else:
                self.relative_y = self.relative_y+1
            self.orientation = 1
        elif direction[2]:#left
            #print("left")
            if self.relative_x-1 < 0:
                if self.column > 0 :
                    self.relative_x = self.WIDTH
                    self.column = self.column-1
            else:
                self.relative_x = self.relative_x-1
            self.orientation = 2
        elif direction[3]:#right
            #print("right")
            if self.relative_x+1 > self.WIDTH:
                if self.column < self.COLUMN-1:
                    self.relative_x = 0
                    self.column = self.column+1
            else:
                self.relative_x = self.relative_x+1
            self.orientation = 3
    def reactions(self):
        if self.hidden == 0:
            self.direction()
        elif self.hidden > 40:
            self.unhide()
        else:
            self.hidden+=1
    def actions(self):
        #input the player and the key array
        #calls the functions for the right action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            #print("love")
            self.love()
        elif keys[pygame.K_h]:
            #print("alert")
            self.alerts()
        elif keys[pygame.K_h]:
            #print("hide")
            self.hide()
        elif keys[pygame.K_h]:
            #print("unhide")
            self.unhide()
        else:
            self.move([keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d]])
    def animate(self):
        #change the number this number will be use to change the index of the picture we display
        #=>change the posture
        if self.posture == 0:
            self.posture = 1
        else:
            self.posture = 0


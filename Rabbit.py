import random
import pygame
from Eagle import Eagle
from Bush import Bush
from Whole import Whole

class Rabbit:         
    each = []
    WIDTH =0 
    HEIGHT =0
    SCREEN_SIZE_X = 0
    SCREEN_SIZE_Y = 0

    def __init__(self, x, y, fastness_mother=10, color = 1):
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
        self.x = x
        self.y = y
        #targeted point
        self.x_target = 0
        self.y_target = 0
        self.new_target()#has to know some of its parameters (alert)
      
    def love(self):
        #check if any rabbit is avaible and love with the one he can
        mother = self.collision_list(self.each)
        if mother != None:
            self.each.append(Rabbit(self.x, self.y, mother.fastness, mother.color))
    #----------------------alerting & hiding
    def alerted(rabbit):
        #alerts a rabbit
        if random.randint(0, rabbit.sensibility) < 100:#should be 2 or 3 in real game
            rabbit.alert = True
            rabbit.find_hide()
            #print("e")
    def alerts(self): 
        #alerts every rabbits around it    
        #check rabbits around
        for rabbit in self.each:
            if not rabbit.alert:
                if abs(rabbit.x-self.x) < self.alerting_capabilities:
                    rabbit.alerted()
        #check if sees an eagle (sometme false alert)
        if random.randint(0, (int)(self.sensibility/(len(Eagle.each_eagle)+1))) > 20:
            self.alerted()
    def find_hide(self):        
        hide = self.closest_hide()
        self.x_target = hide.x
        self.y_target = hide.y
        self.hide_object = hide
    def closest_hide(self):
        final_distance = self.SCREEN_SIZE_X+self.SCREEN_SIZE_Y#to be sur it's a maximum
        final_hide = None
        for hides in [Whole.each, Bush.each]:
            for hide  in hides:
                distance = abs(hide.x-self.x)+abs(hide.y-self.y)
                #if equals to 0 it meens he is on the hide
                #so if he is on a hide but he can't hide, the hide is full
                if  final_distance > distance and Rabbit.can_hide(hide):
                    final_distance = distance
                    final_hide = hide
        return final_hide
    @staticmethod
    def can_hide(hide):
        #find closest hide where he can hide and return it
        if hide.number_of_rabbit < hide.max_rabbit:
            return True
        else:
            return False
    def hide(self):
        if Rabbit.can_hide(self.hide_object):
            self.hidden = 1
            self.hide_object.number_of_rabbit +=1
            self.x =  self.hide_object.x+random.randint(0, self.hide_object.WIDTH)
            self.y =  self.hide_object.y+random.randint(0, self.hide_object.HEIGHT)
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
            Eagle(self.x, self.y)
        self.alerted()
        if self.alert == True:
            self.alerts()
    def new_target(self):
        self.x_target = random.randint(0, self.SCREEN_SIZE_X-self.WIDTH) 
        self.y_target = random.randint(0, self.SCREEN_SIZE_Y-self.HEIGHT)
    #---------------------start of positionnal block
    def direction(self):
        #finds the right direction and calls move_command
        #can also change target (if achieve)
        #to make the move more natural (not linear moves)
        if random.randint(0,1) == 0:
            self.direction_x()
        else:
            self.direction_y()
    def direction_x(self):
        #because we are moving 2 by 2 values will never be reached so we make it aproximately
        if self.x+2 < self.x_target :
            self.move([False, False, False, True])#u,d,l,r
        elif self.x-2 > self.x_target:
            self.move([False, False, True, False])
        elif abs(self.y - self.y_target) > 10:
            self.direction_y()
        else:
            self.arrived()
    def direction_y(self):
        if self.y+2 < self.y_target:
            self.move([False, True, False, False])
        elif self.y-2 > self.y_target:
            self.move([True, False,  False, False])
        elif abs(self.x-self.x_target) > 10:
            self.direction_x()
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
    def collision_object(self, object):
        #returns true if collision, false otherwise
        if abs(self.x-object.x) <= 10 and abs(self.y-object.y) <= 10 and self != object:
            return True
        return False
    def collision_list(self, each):
        #returns the object collided
        for object in each:
            if self.collision_object(object):
                return object
        return None
    def collision_all(self, list):
        for objects in list:
            result = self.collision_list(objects)
            if result != None:
                return result
        return None
    #---------------------start of action
    def move(self, direction):
        #input any rabbit (even the player) with a table giving its position [true, false, false,false]
        #finds the new picture and the new position
        #enter the move section
        if direction[0]:#up
            if self.y >= 0:
                self.y-=2
                #else:
                #print("out of screen up")
            self.orientation = 0
        elif direction[1]:#down
            if self.y <= self.SCREEN_SIZE_Y-self.HEIGHT:
                self.y+=2
                #else:
                #print("out of screen down")
            self.orientation = 1
        elif direction[2]:#left
            if self.x >=0:
                self.x-=2
                #else:
                #print("out of screen left")
            self.orientation = 2
        elif direction[3]:#right
            if self.x <= self.SCREEN_SIZE_X-self.WIDTH:
                self.x+=2
                #else:
                #print("out of screen left")
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
            ##print("love")
            self.love()
        elif keys[pygame.K_h]:
            ##print("alert")
            self.alerts()
        elif keys[pygame.K_h]:
            ##print("hide")
            self.hide()
        elif keys[pygame.K_h]:
            ##print("unhide")
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


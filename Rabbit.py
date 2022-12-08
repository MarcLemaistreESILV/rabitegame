import random
import pygame
import keyboard
import eagle
import Bush
import Whole
import MainActivity as main
class Rabbit:         
    
    def __init__(self, column, ligne, width, height, fastness_mother=10, color = 0):
        #for futur improvments create gens for:
        #color, fastness, sensibility, alerting capabilities, number of child
        #feature
        self.width = width
        self.height = height
        self.orientation = 0
        self.posture = 0
        
        #positionnal
        self.column = column
        self.ligne = ligne
        self.relative_x = 0
        self.relative_y = 0
        #targeted point
        self.target_column = random.randint(0, 10)#betting that the screen is more than 10 square width
        self.target_ligne = random.randint(0, 10)#betting that the screen is more than 10 square heigh

        #rabbit genes
        self.fastness = fastness_mother+5-random.randint(0, 10)
        self.age = 0
        self.alerting_capabilities = 3
        self.color = color#0=orange 1=blue....
        self.sensibility = 10

        #for the game
        self.hide_object = None
        self.alert = 0 
        self.hidden = False
        self.pregnant = False   
        self.player = False
      
    def love(self):
        #check if any rabbit is avaible and love with the one he can
        for rabbit in main.each_rabbit:
            if rabbit != self:
                if rabbit.column == self.column & rabbit.ligne == self.ligne:
                    main.each_rabbit.append(Rabbit(self.column, self.ligne, self.width, self.height, rabbit.fastness, rabbit.color))
                    break
    #----------------------alerting & hiding
    def alerts(self): 
        #alerts every rabbits around it    
        #check rabbits around
        for rabbit in main.each_rabbit:
            if not rabbit.alert:
                if abs(rabbit.column-self.column) < self.alerting_capabilities:
                    rabbit.alerted()
        #check if sees an eagle
        if random.randint(0, (int)(self.sensibility/len(main.each_eagle))) > 20:
            self.alerted()
    def alerted(rabbit):
        #alerts a rabbit
        if random.randint(0, rabbit.sensibility) < 2:
            rabbit.alert = True
            rabbit.new_target()
    def unhide(self, object):
        #hide or unhide the rabbit, affects also the hide's object
        self.hidden = False
        object.number_of_rabbit -=1
    def hide(self, object):
        self.hidden = True
        object.number_of_rabbit +=1
        self.orientation = 4
        match object.__name__:
            case "Bush":
                self.relative_x = random.randint(0, main.WIDTH_BUSH)
                self.relative_y = random.randint(0, main.HEIGHT_BUSH)
            case "Whole":
                self.relative_x = random.randint(0, main.WIDTH_WHOLE)
                self.relative_y = random.randint(0, main.HEIGHT_WHOLE)   
    def can_hide(object):
        #find if it can hide
        if object.number_of_rabbit < object.max_rabbit:
            return True
        else:
            return False
    #----------------------end of alerting and hiding
    def new_eagle(self):
        if random.randint(0, 10) > 9:
            eagle()
    def new_target(self):
        #find new target or new hide or hide
        #maybefutur improvment find if there is the place befor going?
        if self.alert == True :
            #find new hide
            total_distance = 100
            temp_hid = main.map_features[0][1][0]
            #find closest hide
            #futur improvment maybe reading the map is fastier?
            for list in main.map_features:
                for hide in list:
                    distance = abs(hide.column-self.column)+abs(hide.ligne-self.ligne)
                    #if equals to 0 it meens he is on the hide
                    #so if he is on a hide but he can't hide, the hide is full
                    if distance == 0 & self.can_hide():
                        self.hide(hide)
                    elif total_distance > distance & distance != 0:
                        total_distance = distance
                        temp_hid = hide
            self.target_column = temp_hid.column
            self.target_ligne = temp_hid.ligne
        else:
            #set target
            self.target_column = random.randint(0, main.COLUMN) 
            self.target_ligne = random.randint(0, main.LIGNE)

    #---------------------start of direction block
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
            self.move([False, False, False, True], self.target_column+2, self.target_ligne+2)
        elif self.column > self.target_column:
            self.move([False, False, True, False], self.target_column+2, self.target_ligne+2)
        elif self.ligne != self.target_ligne:
            self.direction_ligne()
        else:
            #we are arrived
            print("error")
    def direction_ligne(self):
        if self.ligne < self.target_ligne:
        #we are already certain the rabbit won't leave the screen for too lang
            self.move([True, False, False, False], self.target_column+2, self.target_ligne+2)
        elif self.ligne > self.target_ligne:
            self.move([False,True, False, False], self.target_column+2, self.target_ligne+2)
        elif self.column != self.target_column:
            self.direction_column()
        else:
            #we are arrived
            print("error")
    #---------------------end of direction block
    def move(self, direction):
        #input any rabbit (even the player) with a table giving its position [true, false, false,false]
        #finds the new picture and the new position
        #enter the move section
        if direction[0]:
            print("up")
            if(self.relative_x -1 < 0):
                if self.ligne>0:
                    self.relative_y = self.height
                    self.ligne = self.ligne-1
            else:
                self.relative_y = self.relative_y-1
            self.looking_state = 4
        elif direction[1]:
            print("down")
            if self.relative_y+1 > self.height:
                if self.ligne < main.LIGNE-1:
                    self.relative_y = 0
                    self.ligne = self.ligne+1
            else:
                self.relative_y = self.relative_y+1
            self.looking_state = 5
        elif direction[2]:
            print("left")
            if self.relative_x-1 < 0:
                if self.column > 0 :
                    self.relative_x = self.width
                    self.column = self.column-1
            else:
                self.relative_x = self.relative_x-1
            self.looking_state = 1
        elif direction[3]:
            print("right")
            if self.relative_x+1 > self.width:
                if self.column < main.COLUMN-1:
                    self.relative_x = 0
                    self.column = self.column+1
            else:
                self.relative_x = self.relative_x+1
            self.looking_state == 1 
    def reactions(self):
        #else he is alerted and hidden so we have nothing to do
        if self.hidden == True & self.alerted > 2000:
            self.unhide()
        elif self.hidden == False:
            if self.column == self.target_column & self.ligne == self.target_ligne:
                self.new_eagle()
                self.new_target()
            else:
                self.direction()
    def actions(self, keys):
        #input the player and the key array
        #calls the functions for the right action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_l]:
            print("love")
            self.love()
        elif keys[pygame.K_h]:
            print("alert")
            self.alert()
        elif keys[pygame.K_h]:
            print("hide")
            self.hide()
        elif keys[pygame.K_h]:
            print("unhide")
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
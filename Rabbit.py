import random
import pygame
import keyboard
import eagle
class Rabbit:         

    """ 
    the clock is global
    for improvments
    However each rabbit should be updated on a specifice interval (starting time and duration)
    we hope it'll look like there is no global clock
    """
    #futur improvment link the interval duration to the fastness of the rabbit
    clock_animation = pygame.time.Clock

    #improvment make the color random, make the choice of color infinit, make the color close to the mother color
    def __init__(self, column, ligne, width, height, fastness_mother=10, color = 0):

        self.player = False
        #current points
        #FOR FUTUR ADVENCES CHECK IF BETTER WITH NOT SOTRING POSITION BUT ONLY DIRECTION AND AIME
        #cause the grid's squares has the same dimensions as a rabbit
        self.column = column
        self.ligne = ligne
        self.relative_x = 0
        self.relative_y = 0
        self.width = width
        self.height = height
        self.orientation = 0
        self.posture = 0
        self.color = color#0=orange 1=blue....

        """
        this numbers are linked to MainActivty because pictures are stores in a list
        0 left
        1 right 
        2 up
        3 down
        posture = up or down
        """

        #targeted point
        self.target_column = random.randint(0, 10)#betting that the screen is more than 10 square width
        self.target_ligne = random.randint(0, 10)#betting that the screen is more than 10 square heigh

        #rabbit capabilities
        self.fastness = fastness_mother+5-random.randint(0, 10)
        self.age = 0

        #rabbit powers
        
        #says the rabbit is still under alert, so will try to hide or stay hidden
        #maybe make a global eagle varaible would be more efficient?
        self.alert = True
        self.hidden = False
        self.pregnant = False
        self.sensibility = 0#for improvements, it's the ability for the rabbit to see the eagle


    #change the number this number will be use to change the index of the picture we display
    #=>change the posture
    def animate(self):
        if self.posture == 0:
            self.posture = 1
        else:
            self.posture = 0
    #finds the right direction and calls move_command
    #can also change target (if achieve)
    def move(self):
        #check if under alert
        if self.x_target == self.column & self.y_target == self.ligne:
            if self.alert:
                #stay hidden hide
                self.hidden = True
                #self.posture = 3 #thats for improvments. It should be a head in front of the bush
            else:
                #find new way
                self.arrived()
        else:
            #move
            #to make the move more natural (not linear moves)
            if random.randint(0,1) == 0:
                self.move_column()
            else:
                self.move_ligne()

    def move_column(self):
        if self.column < self.target_column:
        #we are already certain the rabbit won't leave the screen for too lang
            self.move_command([False, False, False, True], self.target_column+2, self.target_ligne+2)
        elif self.column > self.target_column:
            self.move_command([False, False, True, False], self.target_column+2, self.target_ligne+2)
        elif self.ligne != self.target_ligne:
            self.move_ligne()
        else:
            #we are arrived
            self.arrived()


    def move_ligne(self):
        if self.ligne < self.target_ligne:
        #we are already certain the rabbit won't leave the screen for too lang
            self.move_command([True, False, False, False], self.target_column+2, self.target_ligne+2)
        elif self.ligne > self.target_ligne:
            self.move_command([False,True, False, False], self.target_column+2, self.target_ligne+2)
        elif self.column != self.target_column:
            self.move_column()
        else:
            #we are arrived
            self.arrived()
    def arrived(arrived):
        #call an eagle
        eagle()
        #try if is alerted or not
        #calculate new target


    def alerted(self):
        self.alert = True
        #find closest hide and set target

    #can do every thing especially : love, hide or alert
    #calls move for movments
    #      (cf below)....keys[pygame.K_l], keys[pygame.K_h], keys[pygame.K_d], keys[pygame.K_e]]
    #(d is for alert other rabbit but no other keys availble)
    def action_command(self, keys, LIGNE, COLUMN, eagles = []):    
        #check if sees an eagle
            #check if alerts

        n=0
        


    # keys = pygame.key.get_pressed()
    # movment_command = [keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d]]


    def move_command(self, keys, LIGNE, COLUMN):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("up")
            if(self.relative_x -1 < 0):
                if self.ligne>0:
                    self.relative_y = self.height
                    self.ligne = self.ligne-1
            else:
                self.relative_y = self.relative_y-1
            self.looking_state = 4
            last_moove = "up"
        elif keys[pygame.K_a]:
            print("down")
            if self.relative_y+1 > self.height:
                if self.ligne < LIGNE-1:
                    self.relative_y = 0
                    self.ligne = self.ligne+1
            else:
                self.relative_y = self.relative_y+1
            self.looking_state = 5
            last_moove = "down"
        elif keys[pygame.K_d]:
            print("right")
            if self.relative_x+1 > self.width:
                if self.column < COLUMN-1:
                    self.relative_x = 0
                    self.column = self.column+1
            else:
                self.relative_x = self.relative_x+1
            self.looking_state == 1
            last_moove="right"
        elif keys[pygame.K_s]:
            print("left")
            if self.relative_x-1 < 0:
                if self.column > 0 :
                    self.relative_x = self.width
                    self.column = self.column-1
            else:
                self.relative_x = self.relative_x-1
            self.looking_state = 1
            last_moove="left"
        elif keys[pygame.K_l]:
            print("love")
        elif keys[pygame.K_h]:
            print("hide")
        elif keys[pygame.K_e]:
            print("exit")
            return False
        #else: 
            #print("error")
        return True
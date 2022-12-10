import random
import pygame
from Whole import Whole 
from Bush import Bush
from Eagle import Eagle
import sys
import keyboard
""" 
normal rabbit class, posses:
    -rabbit constructor
    -rabbit find direction
    -rabbit actions
WARNING: rabbit != player
"""
from Rabbit import Rabbit
"""
pygame is an open library used to code simple games easily
first you have to install latest pip and py version
then install wheel (pip install wheel)
then go to this link and find the file related to your setup (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame)
pygame‑2.1.2 = pygame version
‑cp310‑cp310 = python version (CPython 3.10)
‑win_amd64.whl = 64 bit (RAM)
then run wheel on the file dowload pip install C://Users/marcl/Downloads/pygame-2.1.2-pp38-pypy38_pp73-win_amd64.whl (use backslash instead of /)
"""

#futur improvments -> make an action be look. So when rabbit is looking it can find eagles but can't move
#when others are alerting it alows you to know if there is an ealge without looking
#resize 
""" for the futur if you want to create a new Object 
    -create new class
    -change the lists in Rabbit named availible_hides=[....]
    -don't forget to change add display in Main """


#--------------INITIALIZING
def screen_init(width, height):
    SCREEN_SIZE_X = width
    SCREEN_SIZE_Y = height
    Eagle.SCREEN_SIZE_X = SCREEN_SIZE_X
    Eagle.SCREEN_SIZE_Y = SCREEN_SIZE_Y
    Rabbit.SCREEN_SIZE_X = SCREEN_SIZE_X
    Rabbit.SCREEN_SIZE_Y = SCREEN_SIZE_Y
    #Display screen
    screen = pygame.display.set_mode((SCREEN_SIZE_X,SCREEN_SIZE_Y))
    pygame.display.set_caption("The Amazing Rabite game")
    icon = pygame.image.load('./src/images/icone.ico')
    pygame.display.set_icon(icon)
    return screen, SCREEN_SIZE_X ,SCREEN_SIZE_Y
def dimensions_init():
    AVERGAE_SCREEN_SIZE = (int)((SCREEN_SIZE_X+SCREEN_SIZE_Y)/2)
    Rabbit.X = SCREEN_SIZE_X
    Rabbit.Y = SCREEN_SIZE_Y
    Rabbit.WIDTH = (int)(AVERGAE_SCREEN_SIZE/10)
    Rabbit.HEIGHT = (int)(AVERGAE_SCREEN_SIZE/10)
    Eagle.WIDTH = (int)(AVERGAE_SCREEN_SIZE/10)
    Eagle.HEIGHT = (int)(AVERGAE_SCREEN_SIZE/10)
    Bush.WIDTH = (int)(AVERGAE_SCREEN_SIZE/10)
    Bush.HEIGHT = (int)(AVERGAE_SCREEN_SIZE/10)
    Whole.WIDTH = (int)(AVERGAE_SCREEN_SIZE/10)
    Whole.HEIGHT = (int)(AVERGAE_SCREEN_SIZE/10)
def initialization():
    #we initialize going form the most to the less restricted feature

    #for rabbit the width is not the same, so we have to load different sets of images
    rabbit_picture_files_names_moving=['up.png', 'down.png', 'left.png', 'right.png']
    rabbit_picture_file_name_extras = [["head.png", 50, 50], ["invisible.png", 0,0]]
    rabbit_picture= load_images(Rabbit.WIDTH, Rabbit.HEIGHT, "rabbit/", rabbit_picture_files_names_moving, ["blue/", "orange/"], ["up/", "down/"], rabbit_picture_file_name_extras)
    Rabbit.each = initialize_each(Rabbit, 4, 4)

    #set the player special features
    Rabbit.each[0].color = 0
    Rabbit.each[0].ligne = 5
    Rabbit.each[0].column = 5
    Rabbit.each[0].player = True
    bush_picture= load_image(Bush.WIDTH, Bush.HEIGHT, "bush/", 'bush_back.png')
    Bush.each = initialize_each(Bush, NUMBER_OF_BUSH, NUMBER_OF_BUSH, 1)
    whole_picture= load_image(Bush.WIDTH, Bush.HEIGHT, "whole/", 'terrier_1_b.png')
    Whole.each = initialize_each(Whole, NUMBER_OF_WHOLE, NUMBER_OF_WHOLE, 2)
    eagle_picture = load_image( Eagle.WIDTH, Eagle.HEIGHT, "eagle/", "eagle_flying.png")
    Eagle.each_eagle = []
    return rabbit_picture, bush_picture, whole_picture, eagle_picture
def load_images(width, height, folder, file_names, colors=[""], postures=[""], extras=[""]):
    pictures= []
    names = []
    for color in colors:
        for posture in postures:
            for file_name in file_names:
                path = str('./src/images/'+folder+color+posture+file_name)
                names.append(path)
                pictures.append(pygame.transform.scale(pygame.image.load(path), (width, height)))        
            for extra in extras:
               path = str('./src/images/'+folder+color+posture+extra[0])
               names.append(path)
               pictures.append(pygame.transform.scale(pygame.image.load(path), (extra[1], extra[2])))                
    return pictures
def load_image(width, height, folder, file_name):
    path = str('./src/images/'+folder+file_name)
    return pygame.transform.scale(pygame.image.load(path), (width, height))
def initialize_each(object_type, min_number, max_number, grid_refractor=0): 
    #parameters are displayed as (who, specificly who, to make the function work)
    #for futur improvments be able to change the objectstype number so we could initialize rabbits at
    #the same place or in bushes/wholes
    each = []
    number = random.randint(min_number, max_number)
    for i in range(number):
        x = random.randint(grid_refractor,SCREEN_SIZE_X-grid_refractor-object_type.WIDTH)
        y = random.randint(grid_refractor,SCREEN_SIZE_Y-grid_refractor)
        while(collision(x,y)):
            x = random.randint(grid_refractor,SCREEN_SIZE_X-grid_refractor-object_type.WIDTH)
            y = random.randint(grid_refractor,SCREEN_SIZE_Y-grid_refractor)
        each.append(object_type(x, y))
    return each
#------------DISPLAYING
def display_all(rabbit_picture, bush_picture, whole_picture, eagle_picture):
    #a bit tricky, only rabbit_picture is a list, the others are single surfaces
    display_background(SCREEN_SIZE_X, SCREEN_SIZE_Y)
    display_rabbit(Rabbit.each, rabbit_picture)
    display_object(Whole.each, bush_picture)
    display_object(Bush.each, whole_picture)
    display_object(Eagle.each_eagle, eagle_picture)
def display_rabbit(rabbits_list, picture):
    for rabbit in rabbits_list:
            #8 images per color -> rabbit.color*8
            #2 state per orientation -> rabbit orientation*2
            #and then the state +rabbit.posture
            #o = orange / b = blue
            #l =left / r=right / u = up / d= down / h= hidden / i = invisible
            #example: [buu, bud, bul, bur, buh, bdu, bdd, bdl, bdr, bdh, i
            #          ouu, obud, oul, our, odu, odd, odl, odr
            #          ...]
            position = rabbit.color*12+rabbit.posture*6+rabbit.orientation
            surface = picture[position]
            screen.blit(surface, (rabbit.x,rabbit.y))
def display_object(list, picture):
    #display an object
    #input: list of the object, just on picture
    for element in list:
            screen.blit(picture, (element.x,element.y))
def display_background(x, y):
    image_grass_background = pygame.image.load('./src/images/map/grass.png')    
    width = image_grass_background.get_width()
    height = image_grass_background.get_height()
    border_x = x%width
    border_y = y%height

    #global surface
    for i in range(0, x-border_x+width, width):
        for j in range(0, y-border_y+height, height):
                screen.blit(image_grass_background, (i,j))
#---------OPERATING
def operating():
    rabbit_operating()
    eagle_operating()
def eagle_operating():
    rabbits_killed = []
    for eagle in Eagle.each_eagle:
        eagle.move()
        rabbits_killed.append(eagle.kill_rabbit(Rabbit.each))
    for rabbits in rabbits_killed:
        for rabbit in rabbits:
            try:
                Rabbit.each.remove(rabbit)
            except Exception:
                pass
            
            print(len(Rabbit.each))
    if len(Rabbit.each) <= 1:#if only one rabbit won't be able to love
        print("game over")
        pygame.display.quit
        pygame.QUIT
        sys.exit() 
def rabbit_operating():
    for rabbit in Rabbit.each:
        if rabbit.player == False:
            rabbit.reactions()
def collision(x,y):
    every_objects = [Whole.each, Bush.each, Rabbit.each]
    for objects in every_objects:
        for object in objects:
            if abs(object.x-x) < object.WIDTH and abs(object.y-y) < object.HEIGHT:
                return True
    return False
#for futur improvments, create a function that creates many rabbit with infinit composition of colors
#def rabbit_collusion()
#initialize
pygame.init()
clock = pygame.time.Clock()

#SETTING FINAL DISTANCES
""" 
every thing is divided into square, a rabbit takes a whole square (because it's the one who will be often refresh)
a bush or a whole takes multiple squares
"""
NUMBER_OF_BUSH = 3
NUMBER_OF_WHOLE = 3

(screen, SCREEN_SIZE_X ,SCREEN_SIZE_Y) = screen_init(500, 500)
dimensions_init()
(rabbit_picture, bush_picture, whole_picture, eagle_picture)= initialization()

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Rabbit.each[0].actions()        
    
    operating()
    display_all(rabbit_picture, bush_picture, whole_picture, eagle_picture)    
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
exit()

        



    










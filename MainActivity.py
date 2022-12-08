import random
import pygame
from Whole import Whole 
from Bush import Bush
from Eagle import Eagle
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
def screen_init():
    #Display screen
    screen = pygame.display.set_mode((SCREEN_SIZE_X,SCREEN_SIZE_Y))

    #Shape of screen
    pygame.display.set_caption("The Amazing Rabite game")
    icon = pygame.image.load('./src/images/icone.ico')
    pygame.display.set_icon(icon)

    #initializes and places pictures
    game_grid = []
    for i in range(0, LIGNE+1):
        line = []
        for j in range(0, COLUMN+1):
            line.append(7)
        game_grid.append(line)
    return screen, game_grid
def initialization():
    #we initialize going form the most to the less restricted feature
    rabbit_picture_files_names=['up.png', 'down.png', 'left.png', 'right.png', 'head.png']
    rabbit_picture= load_images(WIDTH_RABBIT, HEIGHT_RABBIT, "rabbit/", rabbit_picture_files_names, ["blue/", "orange/"], ["up/", "down/"])
    Rabbit.each_rabbit = initialize_each(Rabbit, WIDTH_RABBIT, HEIGHT_RABBIT, 4, 11, 0,3)

    #set the player special features
    Rabbit.each_rabbit[0].color = 0
    Rabbit.each_rabbit[0].ligne = 5
    Rabbit.each_rabbit[0].column = 5
    Rabbit.each_rabbit[0].player = True
    bush_picture= load_image(WIDTH_BUSH, HEIGHT_BUSH, "bush/", 'bush_back.png')
    Bush.each_bush = initialize_each(Bush, WIDTH_BUSH, HEIGHT_BUSH, NUMBER_OF_BUSH, NUMBER_OF_BUSH, 1, 1)
    whole_picture= load_image(WIDTH_BUSH, HEIGHT_BUSH, "whole/", 'terrier_1_b.png')
    Whole.each_whole = initialize_each(Whole, WIDTH_WHOLE, HEIGHT_WHOLE, NUMBER_OF_WHOLE, NUMBER_OF_WHOLE, 1, 2)
    eagle_picture = load_image( WIDTH_EAGLE, HEIGHT_EAGLE, "eagle/", "eagle_flying.png")
    Eagle.each_eagle = []
    return rabbit_picture, bush_picture, whole_picture, eagle_picture
def load_images(width, height, folder, file_names, colors=[""], postures=[""]):
    pictures= []
    names = []
    for color in colors:
        for posture in postures:
            for file_name in file_names:
                path = str('./src/images/'+folder+color+posture+file_name)
                names.append(path)
                pictures.append(pygame.transform.scale(pygame.image.load(path), (width, height)))        
    return pictures
def load_image(width, height, folder, file_name):
    path = str('./src/images/'+folder+file_name)
    return pygame.transform.scale(pygame.image.load(path), (width, height))

def initialize_each(object_type, width, height, min_number, max_number, grid_refractor=0, object_type_number = 1): 
    #parameters are displayed as (who, specificly who, to make the function work)
    #for futur improvments be able to change the objectstype number so we could initialize rabbits at
    #the same place or in bushes/wholes
    each = []
    number = random.randint(min_number, max_number)
    for create_iteration in range(0, number):
        column = random.randint(grid_refractor,COLUMN-grid_refractor)
        ligne = random.randint(grid_refractor,LIGNE-grid_refractor)
        while(game_grid[ligne][column] != 7):
            column = random.randint(grid_refractor, COLUMN-grid_refractor)
            ligne = random.randint(grid_refractor, LIGNE-grid_refractor)
        game_grid[ligne][column] = object_type_number
        each.append(object_type(column, ligne, width,height))
    return each
#------------DISPLAYING
def display_all(rabbit_picture, bush_picture, whole_picture, eagle_picture):
    #a bit tricky, only rabbit_picture is a list, the others are single surfaces
    display_background(SCREEN_SIZE_X, SCREEN_SIZE_Y)
    display_rabbit(Rabbit.each_rabbit, rabbit_picture)
    display_object(Whole.each_whole, bush_picture)
    display_object(Bush.each_bush, whole_picture)
    display_object(Eagle.each_eagle, eagle_picture)
def display_rabbit(rabbits_list, picture):
    for rabbit in rabbits_list:
            x = (int)(rabbit.column*WIDTH_SQUARE+rabbit.relative_x)
            y = (int)(rabbit.ligne*HEIGHT_SQUARE+rabbit.relative_y)
            #8 images per color -> rabbit.color*8
            #2 state per orientation -> rabbit orientation*2
            #and then the state +rabbit.posture
            #o = orange / b = blue
            #l =left / r=right / u = up / d= down
            #example: [buu, bud, bul, bur, buh, bdu, bdd, bdl, bdr, bdh 
            #          ouu, obud, oul, our, odu, odd, odl, odr
            #          ...]
            position = rabbit.color*10+rabbit.posture*5+rabbit.orientation
            surface = picture[position]
            screen.blit(surface, (x,y))
def display_object(list, picture):
    #display an object
    #input: list of the object, just on picture
    for element in list:
            x = (int)(element.column*WIDTH_SQUARE+element.relative_x)
            y = (int)(element.ligne*HEIGHT_SQUARE+element.relative_y)
            screen.blit(picture, (x,y))
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
        rabbits_killed = eagle.kill_rabbit(Rabbit.each_rabbit)
    for rabbit in rabbits_killed:
        Rabbit.each_rabbit.remove(rabbit)
def rabbit_operating():
    for rabbit in Rabbit.each_rabbit:
        if rabbit.player == False:
            rabbit.reactions()



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
SCREEN_SIZE_X = 500
SCREEN_SIZE_Y = 500
AVERGAE_SCREEN_SIZE = (SCREEN_SIZE_Y+SCREEN_SIZE_X)/2

WIDTH_RABBIT = (int)(AVERGAE_SCREEN_SIZE/10)
HEIGHT_RABBIT = (int)(AVERGAE_SCREEN_SIZE/10)

WIDTH_WHOLE = (int)(AVERGAE_SCREEN_SIZE/10)
HEIGHT_WHOLE = (int)(AVERGAE_SCREEN_SIZE/10)

WIDTH_BUSH = (int)(AVERGAE_SCREEN_SIZE/10)
HEIGHT_BUSH = (int)(AVERGAE_SCREEN_SIZE/10)

WIDTH_EAGLE = (int)(AVERGAE_SCREEN_SIZE/10)
HEIGHT_EAGLE = (int)(AVERGAE_SCREEN_SIZE/10)

WIDTH_SQUARE = WIDTH_RABBIT
HEIGHT_SQUARE = HEIGHT_RABBIT
LIGNE = (int)(SCREEN_SIZE_Y/HEIGHT_SQUARE)-1#0,1,2,3,4,5,6,7,8,9 ->10
COLUMN = (int)(SCREEN_SIZE_X/WIDTH_SQUARE)-1#0,1,2,3,4,5,6,7,8,9 -> 10
NUMBER_OF_BUSH = 3
NUMBER_OF_WHOLE = 3
Rabbit.COLUMN = COLUMN
Rabbit.LIGNE = LIGNE

(screen, game_grid) = screen_init()
(rabbit_picture, bush_picture, whole_picture, eagle_picture)= initialization()

#Game Loop
#If I have the time I should check:
#FPS:
#UPS:

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Rabbit.each_rabbit[0].actions()        
    
    operating()
    display_all(rabbit_picture, bush_picture, whole_picture, eagle_picture)    
    pygame.display.flip()
    clock.tick(100)
    

pygame.quit()
exit()

        



    










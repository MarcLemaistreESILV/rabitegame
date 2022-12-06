import random
import pygame
from Whole import Whole
from Bush import Bush
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
from PIL import Image

def setBackground(x, y):
    image_grass_background = pygame.image.load('./src/images/map/grass.png')    
    width = image_grass_background.get_width()
    height = image_grass_background.get_height()
    border_x = x%width
    border_y = y%height

    #global surface
    for i in range(0, x-border_x+width, width):
        for j in range(0, y-border_y+height, height):
                screen.blit(image_grass_background, (i,j))

def load_images(width, height, folder, file_names, colors=[""], postures=[""]):
    pictures= []
    for color in colors:
        for posture in postures:
            for file_name in file_names:
                path = str('./src/images/'+folder+color+posture+file_name)
                pictures.append(pygame.transform.scale(pygame.image.load(path), (width, height)))        
    return pictures

#parameters are displayed as (who, specificly who, to make the function work)
#for futur improvments be able to change the objectstype number so we could initialize rabbits at
#the same place or in bushes/wholes
def initialization(object_type, width, height, min_number, max_number, grid_refractor=0, object_type_number = 1):
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

#map_features = [[each, picture], ...]
def display_grid(map_features):
    for list_of_object in map_features:
        for object in list_of_object[1]:
            x = (int)(object.column*WIDTH_SQUARE+object.relative_x)
            y = (int)(object.ligne*HEIGHT_SQUARE+object.relative_y)
            #looking state is just for futur improvments so we can 
            #add new designs of bushes etc.
            surface = list_of_object[0][object.looking_state]
            screen.blit(surface, (x,y))
def rabbits_handling(each_rabbit, picture):
    #calculte player moves
    #for every rabbits
    for rabbit in each_rabbit:
        #calculate new moves each rabbit
            #find new move (l,r,t,d)
        if not rabbit.player:
            (x,y) = rabbit.move(game_grid)
            #deduce new posture
        rabbit.animate()
            #deduce new orientation
        rabbit.orientation(x,y)
        #calculate collision
        rabbit.collision(game_grid)
            #objects modifications


        #display rabbits
            #futur improvments put this x and y in rabbit class (same for bush and whole)
        x = (int)(rabbit.column*WIDTH_SQUARE+rabbit.relative_x)
        y = (int)(rabbit.ligne*HEIGHT_SQUARE+rabbit.relative_y)
         #8 images per color -> rabbit.color*8
         #2 state per orientation -> rabbit orientation*2
         #and then the state +rabbit.posture
         #o = orange / b = blue
         #l =left / r=right / u = up / d= down
         #example: [olu,old,oru,ord,ouu,oud,odu,odd, 
         #          blu,bld,bru,brd,buu,bud,bdu,bdd
         #          ...]
        surface = picture[rabbit.color*8+rabbit.orientation*2+rabbit.posture]
        screen.blit(surface, (x,y))

#for futur imporvments, create a function that creates many rabbit with infinit composition of colors
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
WIDTH_SQUARE = WIDTH_RABBIT
HEIGHT_SQUARE = HEIGHT_RABBIT
LIGNE = (int)(SCREEN_SIZE_Y/HEIGHT_SQUARE)-1#0,1,2,3,4,5,6,7,8,9 ->10
COLUMN = (int)(SCREEN_SIZE_X/WIDTH_SQUARE)-1#0,1,2,3,4,5,6,7,8,9 -> 10
NUMBER_OF_BUSH = 3
NUMBER_OF_WHOLE = 3

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


#we initialize going form the most to the less restricted feature
rabbit_picture_files_names=['left.png', 'right.png', 'up.png', 'down.png']
rabbit_picture= load_images(WIDTH_RABBIT, HEIGHT_RABBIT, "rabbit/", rabbit_picture_files_names, ["blue/", "orange/"], ["up/", "down/"])
each_rabbit = initialization(Rabbit, WIDTH_RABBIT, HEIGHT_RABBIT, 4, 11, 0,3)

#set the player special features
each_rabbit[0].color = 1
each_rabbit[0].ligne = 5
each_rabbit[0].column = 5
each_rabbit[0].player = True
bush_picture= load_images(WIDTH_BUSH, HEIGHT_BUSH, "bush/", ['bush_back.png', 'rabbit_head_back.png'])
each_bush = initialization(Bush, WIDTH_BUSH, HEIGHT_BUSH, NUMBER_OF_BUSH, NUMBER_OF_BUSH, 1, 1)
whole_picture= load_images(WIDTH_BUSH, HEIGHT_BUSH, "whole/", ['terrier_1_b.png', 'terrier_2_b.png'])
each_whole = initialization(Whole, WIDTH_WHOLE, HEIGHT_WHOLE, NUMBER_OF_WHOLE, NUMBER_OF_WHOLE, 1, 2)
each_eagle = []

#store the values futur improvments:
#make the actions in the classes
# add rabbits to the list
# use a dictionnary
map_features = [[bush_picture, each_bush], [whole_picture,each_whole]]

#the list has differente
""" 
The list has different states:
0    -full
1    -bush
2    -whole
3    -rabbit_1
4    -rabbit_2
5    -rabbit_3
6    -rabbit_4
7    -grass
FOR FUTUR IMPROVMENTS -> OPEN WORLD
depending on the move of the player and because it's a list we juste have to add new lines and columns an
so we only shown the one close to the player
for the rabbits interaction we only look and see if the center of their image is in the same square
"""


#Game Loop
#If I have the time I should check:
#FPS:
#UPS:

running = True
pygame.time.set_timer(rabbits_handling(each_rabbit), 200)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            each_rabbit[0].move(event.key, LIGNE, COLUMN)

    #rabbits do their one display at each move
    
    clock.tick(100)
    #futur imprvoments make it only one efficient function 
    setBackground(SCREEN_SIZE_X, SCREEN_SIZE_Y)
    #display bushes and wholes
    display_grid(map_features)    
    pygame.display.flip()

pygame.quit()
exit()

        



    










import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second, the general speed of the program
fpsClock = pygame.time.Clock()
WINDOWWIDTH = 0 # size of window's width in pixels
WINDOWHEIGHT = 0 # size of windows' height in pixels
FIELDSIZE = 64
GRASS = pygame.image.load("D:\\Python\\grass.png")
MAINMENU = pygame.image.load("D:\\Python\\mainmenu.png")
SIDEMENU = pygame.image.load("D:\\Python\\sidemenu.png")
PLAYBUTTON = pygame.image.load("D:\\Python\\playbutton.png")
global FPSCLOCK, DISPLAYSURF, MAPWIDTH, MAPHEIGHT, CAMERAX, CAMERAY, GAMESTATUS

#            R    G    B
RED      = (255,   0,   0)
BLACK    = (  0,   0,   0)
BROWN    = (255, 100,   0)

fontObj = pygame.font.Font('freesansbold.ttf', 32)

playButton = fontObj.render('Play', True, BLACK, BROWN)
playRect = playButton.get_rect()
playRect.center = (840, 250)

exitButton = fontObj.render('Exit', True, BLACK, BROWN)
exitRect = exitButton.get_rect()
exitRect.center = (840, 830)

class field:
    def __init__(self,typ,spot,img):
        self.typ=typ
        self.spot=spot
        self.img=img
    
    def check_walkable(self):
        if self.typ <2:
            return True
        else:
            return False

    def check_buildable(self):
        if self.typ==2:
            return False
        else:
            return True

class Button:
    def __init__(self,img,pos):
        self.img=img
        self.pos=pos
        self.rect=img.get_rect()
        self.rect.center=pos
    
    def isClicked(x,y):
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False
    
def main():
    global FPSCLOCK, DISPLAYSURF, GAMESTATUS
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),pygame.FULLSCREEN)
    GAMESTATUS = "MAINMENU"
    

    MAPWIDTH = 50
    MAPHEIGHT = 50
    create_map(MAPWIDTH,MAPHEIGHT)
    
    while True:
        if GAMESTATUS == "MAINMENU":
            main_menu()
        elif GAMESTATUS == "GAME":
            game()
        pygame.display.update()
        fpsClock.tick(FPS)

def main_menu():
    DISPLAYSURF.blit(MAINMENU,(0,0))
    
    buttons = []
    buttons.append(playRect)
    buttons.append(exitRect)
    mousex = 0
    mousey = 0
    click=False
    
    for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex,mousey = event.pos
                click=True
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
    BUTTON=ButtonatXY(mousex,mousey,buttons)
    if BUTTON!=None:
        if BUTTON==buttons[0] and click:
            global GAMESTATUS
            GAMESTATUS="GAME"
        elif BUTTON==buttons[1] and click:
            pygame.quit()
            sys.exit()
    del buttons    
    
    DISPLAYSURF.blit(playButton,playRect)
    DISPLAYSURF.blit(exitButton,exitRect)
    

def game():
    mousex = 0
    mousey = 0
    CAMERAX = 0
    CAMERAY = 0
    movex = 0
    movey = 0    
    MAPWIDTH = 50
    MAPHEIGHT = 50
    gameruns=True
        
    while gameruns:
        DISPLAYSURF.fill(BLACK)
        draw_map(MAPWIDTH,MAPHEIGHT,CAMERAX,CAMERAY)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                _ = pygame.key.name(event.key)
                if _ == "right":
                    movex = movex+16
                if _ == "left":
                    movex = movex-16
                if _ == "up":
                    movey = movey-16
                if _ == "down":
                    movey = movey+16
                if _=="escape":
                    gameruns=False
            elif event.type == KEYUP:
                _ = pygame.key.name(event.key)
                if _ == "right":
                    movex = movex-16
                if _ == "left":
                    movex = movex+16
                if _ == "up":
                    movey = movey+16
                if _ == "down":
                    movey = movey-16
            elif event.type == MOUSEMOTION:
                mousex,mousey = event.pos
        if mousex==1919:
            CAMERAX=CAMERAX+16
        if mousex==0:
            CAMERAX=CAMERAX-16
        if mousey==1079:
            CAMERAY=CAMERAY+16
        if mousey==0:
            CAMERAY=CAMERAY-16
        CAMERAX=CAMERAX+movex
        CAMERAY=CAMERAY+movey
        pygame.display.update()
        fpsClock.tick(FPS)
    global GAMESTATUS
    GAMESTATUS="MAINMENU"
    
def draw_map(mx,my,cx,cy):
    for x in range(mx*my):
        if fields[x].spot[0]<=cx+1952 and fields[x].spot[0]>=cx-96 and fields[x].spot[1]>=cy-96 and fields[x].spot[1]<=cy+1112:
            DISPLAYSURF.blit(GRASS,(fields[x].spot[0]-cx,fields[x].spot[1]-cy))
    
    
def create_map(mx,my):
    global fields
    fields = []
    for x in range(mx):
        for y in range(my):
            fields.append(field(0,[x*FIELDSIZE,y*FIELDSIZE],"GRASS"))
            
def ButtonatXY(x,y,buttons):
    for BUTTON in buttons:
        boxRect = pygame.Rect(BUTTON.left, BUTTON.top, BUTTON.right, BUTTON.bottom)
        if boxRect.collidepoint(x, y):
            return BUTTON
    return None

if __name__ == '__main__':
    main()
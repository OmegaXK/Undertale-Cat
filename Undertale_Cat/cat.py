#Undertale Cat

import pygame, sys, random
from pygame.locals import *

pygame.init()

#Set up

basicfont = pygame.font.SysFont(None, 48)

#Set up window
WINDOWWIDTH = 900
WINDOWHEIGHT = 900
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Undertale Cat')

size = 90

#Colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 195, 0)
YELLOW = (255, 255, 0)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE =  (128, 0, 128)

player = pygame.Rect(300, 100, 40, 40)
playerimage = pygame.image.load('Resources/Cat pixel art 16x16.png')
playerstretchedimage = pygame.transform.scale(playerimage, (size, size))

TEXTCOLOR = GREEN

def drawtext(text, font, surface, x, y, color):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

mainclock = pygame.time.Clock()

moveleft = False
moveright = False
moveup = False
movedown = False

MOVESPEED = 8

pygame.mixer.music.load('Resources/Megalovania piano (1).wav')
pygame.mixer.music.play(-1, 0.0)
musicplaying = True

#Game Loop
while True:
    for event in pygame.event.get(): #Event handling loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveright = False
                moveleft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveleft = False
                moveright = True
            if event.key == K_UP or event.key == K_w:
                movedown = False
                moveup = True
            if event.key == K_DOWN or event.key == K_s:
                moveup = False
                movedown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveleft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveright = False
            if event.key == K_UP or event.key == K_w:
                moveup = False
            if event.key == K_DOWN or event.key == K_s:
                movedown = False

            if event.key == K_x: #Spawn the player in a random location
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

            #Change the speed when the player presses "f" or "r"
            if event.key == K_f:
                MOVESPEED -= 1
            if event.key == K_r:
                MOVESPEED += 1

            #Change the size whenever the player presses "q" or "z"
            if event.key == K_q:
                size += 4
                player = pygame.Rect(player.left, player.top, size, size)
                playerstretchedimage = pygame.transform.scale(playerimage, (player.width, player.height))
            if event.key == K_z:
                size -= 4
                player = pygame.Rect(player.left, player.top, size, size)
                playerstretchedimage = pygame.transform.scale(playerimage, (player.width, player.height))

            #Change the music to be on or off when the player presses "m"
            if event.key == K_m:
                if musicplaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicplaying = not musicplaying

    #Fill the screen black
    windowsurface.fill(BLACK)

    #Move the player
    if movedown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveup and player.top > 0:
        player.top -= MOVESPEED
    if moveleft and player.left > 0:
        player.left -= MOVESPEED
    if moveright and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    #Blit the player on screen
    windowsurface.blit(playerstretchedimage, player)

    #Draw the text
    drawtext('Cats are cute!', basicfont, windowsurface, 5, 5, PURPLE)
    drawtext(f'Speed: {MOVESPEED}', basicfont, windowsurface, 725, 5, GREEN) 

    #Update
    pygame.display.update()
    mainclock.tick(40)

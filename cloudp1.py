import pygame
import time
from random import *

blue = (113,170,227)
white = (255,255,255) #valeur maximale des canaux

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300


surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Ballon Volant")
horloge = pygame.time.Clock()


img = pygame.image.load('Ballon01.png')
img_nuage01 = pygame.image.load('NuageHaut.png')
img_nuage02 = pygame.image.load('NuageBas.png')



def nuages (x_nuage, y_nuages, espace):
    surface.blit(img_nuage01, (x_nuage,y_nuage))
    surface.blit(img_nuage02, (x_nuage,y_nuage + nuageW + espace))


def rejoueOuQuitte() :
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP :
            continue
        return event.key
    return None        


def creaTexteObj(texte, Police) :
    texteSurface = Police.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()


def message(texte) :
    GOTexte = pygame.font.Font('BradBunR.ttf',150)
    petitTexte = pygame.font.Font('BradBunR.ttf',20)

    GOTexteSurf, GOTexteRect = creaTexteObj(texte, GOTexte)
    GOTexteRect.center = surfaceW/2, ((surfaceH/2)-50)
    surface.blit(GOTexteSurf, GOTexteRect)


    petitTexteSurf, petitTexteRect = creaTexteObj("Game Over", petitTexte)
    petitTexteRect.center = surfaceW/2, ((surfaceH/2)+50)
    surface.blit(petitTexteSurf, petitTexteRect)
    
    pygame.display.update()    
    time.sleep(2)        

    while rejoueOuQuitte() == None :
        horloge.tick()
	
    principale()


def gameOver() :
    message("Boom!")



def ballon(x,y,image):
    surface.blit(image, (x,y))

def principale():
    x = 150
    y = 200
    y_mouvement = 0

    x_nuage = surfaceW
    y_nuage = randint(-300, 20)
    espace = ballonH*3
    nuage_vitesse = 6


    game_over = False

    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            

            if event.type == pygame.KEYDOWN :        
                if event.key == pygame.K_UP :
                    y_mouvement = -5
            
            if event.type == pygame.KEYUP :        
                y_mouvement = 5
  
        y+= y_mouvement


        surface.fill(blue)
        ballon(x,y,img)
        
        nuages(x_nuage, y_nuage, espace)        

        x_nuage -=nuage_vitesse

        if y > surfaceH -40 or y < -10:
            gameOver()
        
        if x_nuage < (-1 * nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-300,20)        
        
        pygame.display.update()


principale()
pygame.quit()
quit()




from tkinter import *
import pygame 
from force import *
from forces import *
from levels import *
import time
import math

pygame.init()

window = pygame.display.set_mode((1000, 1000))

screen = pygame.Surface((1000,1000))

clock = pygame.time.Clock()


l = level1
spaceship = l.ship
stars = l.stars
nstar = getneareststar(spaceship , stars , l)

t = 100

done = True
dm =1

n = l.number

portal = l.end_portal
coord = [0] * 4

while done:
    for e in pygame.event.get():

        if passLevel(spaceship , portal ) == 0 or distance_betwin_s_nstar(spaceship, stars , l) == 0:       # game is over 
            done = False

    screen.fill((0, 255, 30))
    window.blit(screen, (0, 0))
    
    k = int(spaceship[0])   
    b = int(spaceship[1] )    
    
    for i in range(n):                           # drawing all stars 
        star = stars[i]
        pygame.draw.circle(window, (0, 0, 0), (star[0],star[1] ), star[4])        
        pygame.display.update()  
    
                                                                                 # update it all
    
    pygame.draw.circle(window, (0, 0, 0), (k,b) , spaceship[4] )          # drawing spaceship
    pygame.display.update()  
    m = getneareststar(spaceship , stars , l)        
    star = stars[m]                                                 # find nearest star
    F = getForceProjections(spaceship[0],spaceship[1], spaceship[2], spaceship[3], star[0], star[1], star[3] )       # get projections
    coord =  getShipNextState(spaceship[0], spaceship[1], spaceship[2], spaceship[3], F[0], F[1])                  # get new coordinates and velocities
    spaceship[0] = coord[0]
    spaceship[1] = coord[1]                                                                                      # change old coordinates into new coordinates
    spaceship[2] = coord[2]
    spaceship[3] = coord[3]
    print( spaceship[2],spaceship[3])

    
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                star[3] += dm                                                # change mass if it is necessary
      
    clock.tick(60)


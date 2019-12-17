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

background_image = pygame.image.load("background.png").convert()




t = 100

done = True
dm =1




coord = [0] * 4
p = 0
while p <= 6 :
    
    l = levels[p]
    spaceship = l.ship
    stars = l.stars
    n = l.number
    portal = l.end_portal
    while done:

        for e in pygame.event.get():
           if e.type == pygame.QUIT:
                done = False

        if passLevel(spaceship , portal ) == 0 :      # game is over 
            done = False
        if distance_betwin_s_nstar(spaceship, stars , l) == 0: 
            done = False

        
        window.blit(screen, (0, 0))
        window.blit(background_image, [0, 0])

    
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
    
    
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    star[3] += dm                                                # change mass if it is necessary
      
        clock.tick(60)
        p +=1

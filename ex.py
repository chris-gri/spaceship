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

t = 0.01

done = True


n = l.number

portal = l.end_portal
F = [0] * 2
coord = [0] * 4

while done:
    for e in pygame.event.get():

        if passLevel(spaceship , portal ) or distance_betwin_s_nstar(spaceship, stars):
            done = False


    for i in range(n):
        star = stars[i]
        pygame.draw.circle(window, (0, 0, 0), (star[0],star[1] ), star[4])
            
    screen.fill((0, 255, 30))
    window.blit(screen, (0, 0))
    pygame.draw.circle(window, (0, 0, 0), (int(spaceship[0]),int(spaceship[1])) , spaceship[4] )  
    pygame.display.update()
    
    
    nstar = getneareststar(spaceship , stars , l)
    F = getForceProjections (spaceship[0],spaceship[1], spaceship[2], spaceship[3], nstar[0], nstar[1], nstar[3] )
    coord =  getShipNextState(spaceship[0], spaceship[1], spaceship[2], spaceship[3], f[0], f[1])   
    spaceship[0] = coord[0]
    spaceship[1] = coord[1]
    spaceship[2] = coord[2]
    spaceship[3] = coord[3]
    addingmass(spaceship , stars , event)


    clock.tick(60)
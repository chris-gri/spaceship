from tkinter import *
import pygame 
from force import *
from forces import *
from levels import *
import time
import math
from pygame import mixer
mixer.init()
import sys

pygame.init()

window = pygame.display.set_mode()

screen = pygame.Surface((2000,1000))


f1 = pygame.font.Font('FagoCoTf-Bold.otf', 100)
text1 = f1.render('Game Over', 0, (255, 255, 255))


clock = pygame.time.Clock()

background_image = pygame.image.load("background.png").convert()




# Описание меню
clauses = [(300, 180, u'Fly', (25, 25, 112), (99, 184, 255), 0),
           (300, 460, u'Quit', (25, 25, 112), (99, 184, 255), 1)]

# Создаем меню
class Menu:
    def __init__(self, clauses=[(200, 300, u'Clause', (25, 25, 112), (99, 184, 255), 1)]):
        self.clauses = clauses
    def render(self, surface, font, num_clause):
        for i in self.clauses:
            if num_clause == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True

        font_menu = pygame.font.Font('FagoCoTf-Black.otf', 300)

        clause = 0
        while done:
            screen.fill((0, 100, 200))
            mp = pygame.mouse.get_pos()
            for i in self.clauses:
                if i[0] < mp[0] and mp[0] < i[0] + 550 and mp[1] > i[1] and mp[1] < i[1] + 200:
                    clause = i[5]
            self.render(screen, font_menu, clause)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()


levels = [level1 , level2 , level3 , level4 , level5 , level6]
t = 100
dm =100000
dr = 1
coord = [0] * 4
p = 0
done = True
finish = True
while p <= 5 :

    l = levels[p]
    spaceship = l.ship
    stars = l.stars
    n = l.number
    portal = l.end_portal
    done = True
    click = 0 
    while done and finish :
        finish = True

        Dist = dist(spaceship, portal)
        for e in pygame.event.get():
           if e.type == pygame.QUIT:
                finish = False


        if Dist < portal[2] + spaceship[4]:
                # game is over

            done = False
            p += 1
            print(p)
        if distance_betwin_s_nstar(spaceship, stars , l) == 0:
            print("Game over")
            pygame.draw.circle(window, (255, 0, 0), (700, 500), 400)
            window.blit(text1,(400, 300))
            pygame.display.update()
            time.sleep(5)
            sys.exit()

        
        window.blit(screen, (0, 0))
        window.blit(background_image, [0, 0])

    
        k = int(spaceship[0])   
        b = int(spaceship[1])
    
        for i in range(n):                           # drawing all stars 
            star = stars[i]
            pygame.draw.circle(window, (32, 178, 170), (star[0],star[1] ), star[4])
            pygame.display.update()
    
                                                                                 # update it all
    
        pygame.draw.circle(window, (0, 0, 0), (k,b) , spaceship[4] )     
             # drawing spaceship

        pygame.draw.circle(window, (0, 120 , 30), (portal[0], portal[1]),  portal[2])

        pygame.display.update()
        m = getneareststar(spaceship, stars, l)
        star = stars[m]                                                 # find nearest star
        F = getForceProjections(spaceship[0],spaceship[1], spaceship[2], spaceship[3], star[0], star[1], star[3] )       # get projections
        coord = getShipNextState(spaceship[0], spaceship[1], spaceship[2], spaceship[3], F[0], F[1])                  # get new coordinates and velocities
        spaceship[0] = coord[0]
        spaceship[1] = coord[1]                                                                                      # change old coordinates into new coordinates
        spaceship[2] = coord[2]
        spaceship[3] = coord[3]
    
    
        if findcursorposition(spaceship, stars, l):
            for i in pygame.event.get():
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        star[3] += dm
                        star[4] += dr
                        click += 1 
                    elif i.button == 3:
                        star[3] -= dm
                        star[4] -= dr
                        click +=1                                              # change mass if it is necessary
      
        clock.tick(60)



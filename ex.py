from tkinter import *
import pygame 
from force import *
from forces import *
from levels import *
import time
import math
import sys
import random 
from pygame import mixer
mixer.init()


pygame.init()

window = pygame.display.set_mode((1530,830))

screen = pygame.Surface((1530,830))

f1 = pygame.font.Font('FagoCoTf-Black.otf', 100)
text1 = f1.render('Game Over', 0, (255, 255, 255))


clock = pygame.time.Clock()


image1 = pygame.image.load("planet1.png")
image2 = pygame.image.load("planet2.png")
image3 = pygame.image.load("planet3.png")
image4 = pygame.image.load("planet4.png")
image5 = pygame.image.load("planet5.png")
images = [image1, image2, image3, image4 , image5, image1, image2, image3, image4, image5]

pygame.display.set_caption('Space Oddity')



# Menu Description
clauses = [(100, 0, u'Fly', (25, 25, 112), (99, 184, 255), 0),
           (150, 250, u'Quit', (25, 25, 112), (99, 184, 255), 1),
           (120, 500, 'Levels', (25, 25, 112), (99, 184, 255), 2)]
states = [(100, 50, u'Level 1', (25, 25, 112), (99, 184, 255), 0),
          (120, 120, u'Level 2', (25, 25, 112), (99, 184, 255), 1),
          (140, 190, 'Level 3', (25, 25, 112), (99, 184, 255), 2),
          (160, 260, 'Level 4', (25, 25, 112), (99, 184, 255), 3),
          (180, 330, 'Level 5', (25, 25, 112), (99, 184, 255), 4),
          (100, 400, 'Level 6', (25, 25, 112), (99, 184, 255), 5),
          (120, 470, 'Level 7', (25, 25, 112), (99, 184, 255), 6),
          (140, 540, 'Level 8', (25, 25, 112), (99, 184, 255), 7),
          (160, 610, 'Level 9', (25, 25, 112), (99, 184, 255), 8),
          (180, 680, 'Level 10', (25, 25, 112), (99, 184, 255), 9),
          (390, 365,'Menu', (25, 25, 112), (99, 184, 255), 10)]


t = 100
dm =100000
dr = 1
coord = [0] * 4
p = 0

def chooselevel(p):
    background_image = pygame.image.load("background.png").convert()

    while p <= 9:
        done = True
        l = levels[p]
        spaceship = l.ship[:]
        stars = l.stars[:]
        stars = l.stars
        n = l.number
        portal = l.end_portal
        ship_image = l.ship_image

        click = 0
        while done:

            Dist = dist(spaceship, portal)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()

            if Dist < portal[2] + spaceship[4]:
                background_image = pygame.image.load("background.png").convert()
                done = False
                p += 1
                print(p)

            if distance_betwin_s_nstar(spaceship, stars, l) == 0:
                background_image = pygame.image.load("background.png").convert()
                for i in range(n):
                    m = l.m
                    star = stars[i]
                    star[3] = m[i]
                    star[2] = 50
                    star[4] = 20


                done = False

            window.blit(screen, (0, 0))
            window.blit(background_image, [0, 0])

            k = int(spaceship[0])
            b = int(spaceship[1])
            xy = ((spaceship[2]) ** 2 + (spaceship[3]) ** 2) ** 0.5
            ux = spaceship[2] / xy
            uy = spaceship[3] / xy

            for i in range(n):  # drawing all stars
                star = stars[i]
                image = images[i]
                image = pygame.transform.scale(image, (star[2], star[2]))
                imageT = image.get_rect(center=(star[0], star[1]))
                window.blit(image, imageT)

            image = l.ship_image
            imageI = pygame.image.load(image)
            imageI = pygame.transform.scale(imageI, (40, 40))
            imageT = imageI.get_rect(center=(spaceship[0], spaceship[1]))

            window.blit(window, (0, 0))
            window.blit(imageI, imageT)

            # drawing spaceship
            pygame.draw.circle(window, (0, 120, 30), (portal[0], portal[1]), portal[2])
            pygame.draw.line(window, (255, 255, 0), (spaceship[0], spaceship[1]),
                             (spaceship[0] + 3 * ux * xy ** 0.6, spaceship[1] + 3 * uy * xy ** 0.6), 3)
            pygame.draw.line(background_image, (255, 102, 0), (spaceship[0], spaceship[1]),
                             (spaceship[0] + ux, spaceship[1] + uy))

            pygame.display.update()
            m = getneareststar(spaceship, stars, l)
            star = stars[m]  # find nearest star
            F = getForceProjections(spaceship[0], spaceship[1], spaceship[2], spaceship[3], star[0], star[1],
                                    star[3])  # get projections
            coord = getShipNextState(spaceship[0], spaceship[1], spaceship[2], spaceship[3], F[0],
                                     F[1])  # get new coordinates and velocities
            spaceship[0] = coord[0]
            spaceship[1] = coord[1]  # change old coordinates into new coordinates
            spaceship[2] = coord[2]
            spaceship[3] = coord[3]

            if findcursorposition(spaceship, stars, l):
                for i in pygame.event.get():
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            star[3] += dm
                            star[4] += dr
                            star[2] += 5
                            click += 1
                        elif i.button == 3:
                            star[3] -= dm
                            if star[4] >= 20:
                                star[4] -= dr
                                star[2] -= 5
                            click += 1  # change mass if it is necessary

            clock.tick(60)

# Menu
class Menu:
    def __init__(self, clauses=[(150, 250, u'Clause', (25, 25, 112), (99, 184, 255), 1)], states = [(100, 0, u'Level 1', (25, 25, 112), (99, 184, 255), 0)]):
        self.clauses = clauses
        self.states = states
    def rendermenu(self, surface, font, num_clause):
        for i in self.clauses:
            if num_clause == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        Planet_surf = pygame.image.load('Planet-Blue.bmp')
        done = True

        font_menu = pygame.font.Font('FagoCoTf-Black.otf', 300)

        clause = 0
        while done:
            screen.fill((0, 100, 200))
            mp = pygame.mouse.get_pos()
            for i in self.clauses:
                if i[0] < mp[0] and mp[0] < i[0] + 550 and mp[1] > i[1] and mp[1] < i[1] + 300:
                    clause = i[5]
            self.rendermenu(screen, font_menu, clause)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if clause == 0:
                        chooselevel(0)
                    elif clause == 1:
                        sys.exit()
                    elif clause == 2:
                        game.levels()
            Planet_rect = Planet_surf.get_rect(bottomright=(1700, 900))
            window.blit(screen, (0, 0))
            window.blit(Planet_surf, Planet_rect)
            pygame.display.flip()
#Levels in menu
    def renderlevels(self, surface, font, num_states):
        for i in self.states:
            if num_states == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def levels(self):
        end = True
        font_menu = pygame.font.Font('FagoCoTf-Black.otf', 70)
        Planet2 = pygame.image.load('Planet-White.bmp')
        state = 0
        while end:
            screen.fill((255, 255, 255))
            mp = pygame.mouse.get_pos()
            for i in self.states:
                if i[0] < mp[0] and mp[0] < i[0] + 200 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    state = i[5]
            self.renderlevels(screen, font_menu, state)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    for i in states:
                        if state == i[5] and state != 10:
                            p = i[5]
                            chooselevel(p)
                        if state == 10:
                            game.menu()

            Planet1 = Planet2.get_rect(bottomright=(1500, 900))
            window.blit(screen, (0, 0))
            window.blit(Planet2, Planet1)
            pygame.display.flip()

#Настройка звука
pygame.mixer.pre_init(44100, -16, 1, 100)
pygame.mixer.init()

sound = pygame.mixer.Sound('Oddity.ogg')
sound.play(-1)


game = Menu(clauses, states)
game.menu()

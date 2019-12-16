import pygame, math
from levels import *
import pygame 
from force import *
from forces import *
import time
import tkinter as tk
dL = 3;

pygame.init()

window = pygame.display.set_mode((1000, 1000))

screen = pygame.Surface((1000,1000))

clock = pygame.time.Clock()
root = tk.Tk()
img = tk.PhotoImage(file="background.PNG")
image = canvas.create_image(10, 10, anchor=tk.NW, image=img)

stars =  level4.stars
n =  level4.number
ship =  level4.ship
l =  level4
a =0
while done:
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            done = False
    screen.fill((0, 255, 30))
    window.blit(screen, (0, 0))
    for i in range(n):
        star = stars[i]
        a = star[0]
        b = star[1]
        pygame.draw.circle(window, (0, 0, 0), (a,b ), 20)
        

   
    a = getneareststar(ship , l.stars ,l) 

    print(a)   

    pygame.display.update()

    clock.tick(60)
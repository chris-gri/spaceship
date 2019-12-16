import pygame, math
from levels import *
import pygame 
from force import *
from forces import *
import time
dL = 3;

pygame.init()

window = pygame.display.set_mode((1000, 1000))

screen = pygame.Surface((1000,1000))

clock = pygame.time.Clock()

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
        
'''   
    
    pygame.draw.circle(window, (0, 0, 0), (ix, iy), R)
    

    if 1:
        x += Vx * dt
        y += Vy * dt
        r = ((x - sx) * (x - sx) + (y - sy) * (y - sy)) ** 0.5
        f = M / (r * r)
        fx = f / r * (sx - x)
        fy = f / r * (sy - y)

        x = x + Vx * dt + fx * dt * dt / 2
        y = y + Vy * dt + fy * dt * dt / 2
        Vx = Vx + fx * dt
        Vy = Vy + fy * dt

        ix = int(ship[0])
        iy = int(ship[1])
'''        
    a = getneareststar(ship , l.stars ,l) 

    print(a)   

    pygame.display.update()

    clock.tick(60)
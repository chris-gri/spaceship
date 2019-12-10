from tkinter import *
import pygame 
from force import *
from forces import *
from levels import *
import time
dL = 3;
dM = 3;
t = 0.01;
tk = Tk()

height = 700
width = 700 

canvas = Canvas(tk, width = width, height = height)
tk.title("space")
canvas.pack()

l = level1
spaceship = l.ship
obj_ship = canvas.create_oval(l.ship[0]-l.ship[4],l.ship[1]-l.ship[4],l.ship[0]+l.ship[4],l.ship[1]+l.ship[4],fill='yellow')
 
coords = [spaceship[0], spaceship[1], spaceship[2], spaceship[3]]

class main :
	findcursorposition(spaceship ,stars)
	Vx = coords[2]
	Vy = coords[3]
	f = getForceProjections (spaceship[0], spaceship[1], coords[2], coords[3], nstar[0], nstar[1], nstar[3])
	coords = getShipNextState(spaceship[0], spaceship[1], Vx, Vy, f[0], f[1])



while passLevel(spaceship , l.end_portal ) == 0 and distance_betwin_s_nstar(spaceship, stars) == 0:
	
	

	canvas.move(obj_ship,coords[2],coords[3])

	tk.update()
	time.sleep(0.1)
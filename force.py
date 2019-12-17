import pygame
def getDist(x1, y1, x2, y2):
	
	return ((y2-y1)**2 + (x2-x1)**2)**0.5
def dist(a, b):
	r = ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))**0.5
	return r

def getneareststar(spaceship , stars ,l):
	 
	n = 0                    # number of stars 
	for i in range(l.number):
	
		
		if dist(spaceship , stars[i]) <= dist(spaceship , stars[n]):
			n = i
		

	return n

def distance_betwin_s_nstar(spaceship, stars , l):    #finding distance between spaceship and nearest star 
     
                                                   #and return false if crash otherwise true   
	nstar = getneareststar(spaceship , stars , l)
	n = stars[nstar]
	d = dist(spaceship , n)
	if d <= n[4] + spaceship[4]:
		return False 
	else:
		return True 	

def findcursorposition(spaceship ,stars , l ):         #finding cursors position 

	nstar = getneareststar(spaceship , stars , l)       #if curor is on the nearest star return true otherwise false      
	n = stars[nstar]
	cursor = pygame.mouse.get_pos()
	r = dist(cursor, n)
	if r <= n[4]:
		return True
	else:
		return False	

def addingmass(spaceship , stars , l):         #adding to nearest star if cursor is presed 

	nstar = getneareststar(spaceship , stars , l )
	n = stars[nstar]
	for i in pygame.event.get():
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_LEFT:
				n[3] += dm
			

def passLevel(l):  #if spaceship rеaches portal return true otherwise false
	port = l.end_portal
	ship = l.ship
	if ship[0] > port[0] and ship[0] < port[2] and ship[1] > port[1] and ship[1] < port[3]:
		return True
	else:
		return False

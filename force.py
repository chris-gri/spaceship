def getDist(x1, y1, x2, y2):
	
	return ((y2-y1)**2 + (x2-x1)**2)**0.5
def dist(a, b):
	r = ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))**0.5
	return r

def getneareststar(spaceship , stars ,l):
	 
	A = [0] * l.number 
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

	nstar = getneareststar(spaceship , star , l)       #if curor is on the nearest star return true otherwise false      
	cursor = canvas.get_mouse_coords()
	r = getDist(cursor.x, cursor.y, spaceship[0] , spaceship[1])
	if r <= nstar.r:
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
	

def passLevel(spaceship , portal ):  #if spaceship rеaches portal return true otherwise false 
	
	if ((spaceship[0] - portal[0])**2)**0.05 <= (portal[2])/2 and  ((spaceship[1] - portal[1])**2)**0.05 <= (portal[3])/2 :
		return True
	else:
		return False

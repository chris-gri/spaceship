def getDist(x1, y1, x2, y2):
	
	return ((y2-y1)**2 + (x2-x1)**2)**0.5
def dist(a, b):
	r = ((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))**0.5
	return r

def getneareststar(spaceship , stars ,l):
	 
	A = [0] * l.number                        # number of stars 
	for i in range(l.number):
		A[i] = dist(spaceship , stars[i])  # distance between ith star and spaceship 
	A.sort()
	nstar = A[0]
	return nstar

def distance_betwin_s_nstar(spaceship, stars):    #finding distance between spaceship and nearest star 
                                                    #and return false if crash otherwise true   
	nstar = getneareststar(spaceship , stars)
	d = dist(spaceship , nstar)
	if d <= nstar[4]:
		return False 
	else:
		return True 	

def findcursorposition(spaceship ,stars):         #finding cursors position 
	
	nstar = getneareststar(spaceship , stars)       #if curor is on the nearest star return true otherwise false      
	cursor = canvas.get_mouse_coords()
	r = getDist(cursor.x, cursor.y, spaceship[0] , spaceship[1])
	if r <= nstar.r:
		return True
	else:
		return False	

def addingmass(spaceship , stars , event):         #adding to nearest star if cursor is presed 
	
	button = pygame.mouse.get_pressed()
	nstar = getneareststar(spaceship , stars)
	if findcursorposition(spaceship , stars) == true and button[0] == true :
		nstar[3] += dm
	elif findcursorposition(spaceship , stars) == true and button[1] == true :
		nstar[3] -= dm 

def passLevel(spaceship , portal ):  #if spaceship rеaches portal return true otherwise false 
	
	if ((spaceship[0] - portal[0])**2)**0.05 <= (portal[2])/2 and  ((spaceship[1] - portal[1])**2)**0.05 <= (portal[3])/2 :
		return True
	else:
		return False

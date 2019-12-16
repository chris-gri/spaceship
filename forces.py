t = 0.01


def getForceProjections (x, y, vx, vy, sx, sy, M ):
	x += vx * t 
	y += vy * t 
	r = ((x - sx) * (x - sx) + (y - sy) * (y - sy))**0.5
	f =  M / (r*r)
	fx = f / r * (-x + sx)
	fy = f / r * (-y + sy)
	return fx , fy


def  getShipNextState(x, y, Vx, Vy, fx, fy):    # Vx and vx are different 
                                                 #give him everithig and he will give you what you need 
	x = x + Vx * t + fx * t * t / 2
	y = y + Vy * t + fy * t * t / 2
	vx =  Vx + fx * t
	vy =  Vy + fy * t
	return x, y, vx, vy 



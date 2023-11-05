from sense_hat import SenseHat
import time
 
s = SenseHat()
s.low_light = True
 
yellow = (255, 255, 0)
nothing = (0,0,0)
 
def S():
	Y = yellow
	O = nothing
	logo = [
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, O, O, O, O,
	O, Y, Y, Y, O, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, O, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	]
	return logo
	
def R():
	Y = yellow
	O = nothing
	logo = [
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, O, O, Y, Y, O,
	O, Y, Y, O, O, Y, Y, O,
	O, Y, Y, Y, Y, O, O, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, O, O, Y, Y, Y,
	O, Y, Y, O, O, O, Y, Y,
	]
	return logo	

def M():
	Y = yellow
	O = nothing
	logo = [
	Y, Y, O, O, O, O, Y, Y,
	Y, Y, Y, O, O, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, O, Y, Y, O, Y, Y,
	Y, Y, O, O, O, O, Y, Y,
	Y, Y, O, O, O, O, Y, Y,
	Y, Y, O, O, O, O, Y, Y,
	]
	return logo
	
def I():
	Y = yellow
	O = nothing
	logo = [
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	]
	return logo
	
def S():
	Y = yellow
	O = nothing
	logo = [
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, O, O, O, O,
	O, Y, Y, Y, O, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, O, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	O, Y, Y, Y, Y, Y, Y, O,
	]
	return logo
	
def T():
	Y = yellow
	O = nothing
	logo = [
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	Y, Y, Y, Y, Y, Y, Y, Y,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	O, O, O, Y, Y, O, O, O,
	]
	return logo
	
images = [S, R, M, I, S, T]
count = 0
 
while True:
    s.set_pixels(images[count % len(images)]())
	time.sleep(.75)
	count += 1

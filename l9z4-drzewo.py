from turtle import *
import random
tracer(0, 1)
lt(90)
dlugosc = 50
fd(dlugosc)
def drzewo(dlugosc):
	if dlugosc >= 10:
		kat = random.randint(10,20)
		lt(kat)
		dlugosc -= 5
		fd(dlugosc)
		drzewo(dlugosc)
		lt(180)
		fd(dlugosc)
		x = 180-2*kat
		lt(x)
		fd(dlugosc)
		drzewo(dlugosc)
		lt(180)
		fd(dlugosc)
		rt(180-kat)
	
	
drzewo(dlugosc)
input()
		

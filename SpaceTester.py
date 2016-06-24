from Space import *
import time

r1 = Vector(0, 0)
v1 = Vector(0, 0)
m1 = 100
p1 = Particle(r1, v1, m1)

r2 = Vector(4, 0)
v2 = Vector(0, 0)
m2 = 100
p2 = Particle(r2, v2, m2)

space = Space([p1, p2])

while True:
	print space
	space.evolve()
	time.sleep(1)
	





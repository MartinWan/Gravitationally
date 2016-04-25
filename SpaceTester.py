from Space import *

'''
space = Space([])

p1 = Particle(Vector())
p2 = Particle(Vector(1, 1))

print space.inSameQuadrant(p1, p2)
'''

particles = []
# sw
for i in range(-2, 2):
	for j in range(-2, 2):
		r = Vector(i , j)
		particles.append(Particle(r))


for i in particles:
	print i

particles.sort(cmp = quadrantOrder)
print 'SORTED \n \n \n '

for i in particles:
	print i

'''
space = Space(particles)
print space

for i in particles:
	print i
'''
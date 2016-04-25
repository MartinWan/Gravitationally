from Particle import *

def quadrantOrder(particle0, particle1):
	W = 800 # display size parameters from interface 
	H = 640
	
	# create primed coordinates in quadrants
	x0 = particle0.r.x - W/2
	x1 = particle1.r.x - W/2
	y0 = particle0.r.y - H/2
	y1 = particle1.r.y - H/2

	particle0quadrant = -1
	particle1quadrant = -1

	if x0 >= 0 and y0 >= 0:
		particle0quadrant = 1
	elif x0 < 0 and y0 >= 0:
		particle0quadrant = 2
	elif x0 < 0 and y0 < 0:
		particle0quadrant = 3
	elif x0 >= 0 and y0 < 0:
		particle0quadrant = 4

	if x1 >= 0 and y1 >= 0:
		particle1quadrant = 1
	elif x1 < 0 and y1 >= 0:
		particle1quadrant = 2
	elif x1 < 0 and y1 < 0:
		particle1quadrant = 3
	elif x1 >= 0 and y1 < 0:
		particle1quadrant = 4

	if particle1quadrant == particle0quadrant:
		return 0
	else:
		return (particle0quadrant - particle1quadrant) / abs(particle0quadrant - particle1quadrant)

class Error:
	''' Provide exception class for Space with string message
	'''
	def __init__(self, message):
		self.message = message

class Space:
	''' A set of particles and a time t. All attributes are private.
	'''
	def __init__(self, particles = []):
		if type(particles) != list:
			raise Error('Parameter "particles" illegal.')
		if not all(isinstance(particle, Particle) for particle in particles):
			raise Error('All elements of list must be of type "Particle".')
		
		
		self.t = 0.0
		self.p = Vector(0, 0)

		# arrange particles into barnes hut tree 
		'''
		N = len(particles)
		for i in range(N):
			for j in range(i + 1, N):
				if self.inSameQuadrant(particles[j], particles[i]):
					particles[i + 1], particles[j] = particles[j], particles[i + 1] #swap(particles[i + 1], particles[j])
					i = i + 1
		'''
		# inititialize total momentum to test accuracy of numerical integration (check momentum conserved)
		for particle in particles:
			self.p += particle.m * particle.v

		self.particles = particles

	def evolve(self):
		''' Update velocities and positions due to mutual gravitation using euler's method
		'''
		dt = 0.04
		p = Vector(0, 0)
		particleVelocityChanges = {}

		# compute dv for each particle
		for particle in self.particles:
			g = Vector(0, 0)
			p += particle.m * particle.v

			for otherParticle in self.particles:
				R = otherParticle.r - particle.r
				if R.length() == 0: # same particle
					continue
				elif R.length() < (particle.d + otherParticle.d) / 2.5: # totally inelastic collision
					particle.v = ( particle.m * particle.v + otherParticle.m * otherParticle.v ) / ( particle.m + otherParticle.m ) # conservation of momentum
					particle.m += otherParticle.m
					particle.d = ( particle.d ** 3 + otherParticle.d ** 3 ) ** (1.0 / 3.0) # new diameter computed using conservation of volume
					i = self.particles.index(otherParticle)
					del self.particles[i]
					continue

				g += ( otherParticle.m * R ) / ( R.length() ** 3)

			particleVelocityChanges[particle] = g * dt

		# update all particles velocity from dv
		for particle in self.particles:
			particle.v += particleVelocityChanges[particle]
			particle.r += particle.v * dt

		print 'momentum =', self.p 
		self.p = p
		self.t += dt

	def addParticle(self, particle):
		''' add new particle to space 
		'''
		if not isinstance(particle, Particle):
			raise Error('Parameter "particle" illegal.')
		self.particles.append(particle)

	def getParticles(self):
		''' return list of particles 
		'''
		return self.particles

	def clearSpace(self):
		''' delete all particles
		'''
		self.particles = []
		self.t = 0.0
	
	def __str__(self):
		s = "Space at t = {} with total momentum p = {} \n".format(self.t, self.p)
		for particle in self.particles:
			s += particle.__str__()
			s += '\n'

		return s		
		
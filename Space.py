from Particle import *

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
		self.particles = particles
		self.t = 0.0
		self.p = Vector(0, 0)

		for particle in particles:
			self.p += particle.m * particle.v
	
	def evolve(self):
		''' Update velocities and positions due to mutual gravitation using numerical integration
		'''
		dt = 0.04
		particleChanges = {}
		p = Vector(0, 0)

		for particle in self.particles:
			g = Vector(0, 0)
			p += particle.m * particle.v

			for otherParticle in self.particles:
				R = otherParticle.r - particle.r
				if R.length() == 0: # same particle
					continue
				elif R.length() < (particle.d + otherParticle.d) / 2: # totally inelastic collision
					particle.v = ( particle.m * particle.v + otherParticle.m * otherParticle.v ) / ( particle.m + otherParticle.m ) # conservation of momentum
					particle.m += otherParticle.m
					particle.d = ( particle.d ** 3 + otherParticle.d ** 3 ) ** (1.0 / 3.0) # new diameter computed using conservation of volume
					i = self.particles.index(otherParticle)
					del self.particles[i]
					continue

				g += ( otherParticle.m * R ) / ( R.length() ** 3)

			delta_v = g * dt
			delta_r = particle.v * dt
			particle.v += delta_v
			particle.r += delta_r

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
		
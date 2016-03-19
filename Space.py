from Particle import *

class Error:
	''' Provide exception class for Space with string message
	'''
	def __init__(self, message):
		self.message = message

class Space:
	''' A set of particles and a time t. 
	'''
	def __init__(self, particles):
		if type(particles) not in (list, tuple):
			raise Error('Parameter "particles" illegal.')
		if not all(isinstance(particle, Particle) for particle in particles):
			raise Error('All elements of list must be of type "Particle".')
		self.particles = particles
		self.t = 0.0
	
	def evolve(self):
		''' Update velocities and positions due to mutual gravitation
		'''
		dt = 0.4
		numParticles = len(self.particles)
		
		# update velocities and positions of particles due to mutual gravitation
		for i in range(numParticles):
			particle = self.particles[i]
			otherParticles = self.particles[:i] + self.particles[i + 1:]
			
			# compute gravitaional acceleration g for particle due to other particles
			for otherParticle in otherParticles:
				g = Vector(0, 0)
				R = otherParticle.r - particle.r 
				if R.length() < 0.001:
					continue # TODO implement elastic collisions
				g += ( otherParticle.m * R ) / ( R.length() ** 3 ) # newton's gravitation
			
			# update particle velocity and position
			particle.v += g * dt
			particle.r += particle.v * dt

		# update time
		self.t += dt 
	
	def __str__(self):
		s = "Space at t = {} with ... \n".format(self.t)
		for i in self.particles[0 : -1]: # all particles except last one
			s += i.__str__()
			s += "\n"
		s += self.particles[-1].__str__() # print last one without trailing new line
		return s		
		
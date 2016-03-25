from Particle import *

class Error:
	''' Provide exception class for Space with string message
	'''
	def __init__(self, message):
		self.message = message

class Space:
	''' A set of particles and a time t. 
	'''
	def __init__(self, particles = []):
		if type(particles) != list:
			raise Error('Parameter "particles" illegal.')
		if not all(isinstance(particle, Particle) for particle in particles):
			raise Error('All elements of list must be of type "Particle".')
		self.particles = particles
		self.t = 0.0
	
	def evolve(self):
		''' Update velocities and positions due to mutual gravitation
			returns dictionary of position changes made to particles
		'''
		dt = 0.05
		numParticles = len(self.particles)
		particleChanges = {}
		epsilon = 1 # for singularity softening

		# update velocities and positions of particles due to mutual gravitation
		for i in range(numParticles):
			particle = self.particles[i]
			otherParticles = self.particles[:i] + self.particles[i + 1:]
			g = Vector(0, 0)
			
			collision = False

			# compute gravitaional acceleration g for particle due to other particles
			for otherParticle in otherParticles:
				g = Vector(0, 0)
				R = otherParticle.r - particle.r 
				if R.length() < 1: # TEST OF TOTALLY INELASTIC COLLISION
					g = Vector(0, 0)
					collision = True
					break
				g += ( otherParticle.m * R ) / ( R.length() ** 3 + epsilon ) # newton's gravitation with singularity softening
			
			# update particle velocity and position
			if not collision:
				delta_v = g * dt
				delta_r = particle.v * dt
				particle.v += delta_v
				particle.r += delta_r
				particleChanges[particle] = delta_r
			else: # collision
				#particle.v = Vector(0, 0)
				particleChanges[particle] = Vector(0, 0)

		self.t += dt 
		return particleChanges
		

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
		s = "Space at t = {} with ... \n".format(self.t)
		if self.particles:
			for i in self.particles[0 : -1]: # all particles except last one
				s += i.__str__()
				s += "\n"
			s += self.particles[-1].__str__() # print last one without trailing new line
		else:
			s += 'Nothing'
		return s		
		
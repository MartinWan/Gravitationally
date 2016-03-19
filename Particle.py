from Vector import *

class Error(Exception):
	''' Provide exception class for Vector with string message
	'''
	def __init__(self, message):
		self.message = message

class Particle:
	''' A point particle that exists in space with position and velocity vectors and mass 
	'''
	
	def __init__(self, r, v, m):
		''' Initialize particle with vectors position r and velocity v and mass m
		'''
		if not isinstance(r, Vector):
			raise Error('Parameter "r" illegal')
		if not isinstance(v, Vector):
			raise Error('Parameter "v" illegal')
		if type(m) not in (int, float):
			raise Error('Parameter "m" illegal')
		self.r = r
		self.m = m
		self.v = v
	
	def __str__(self):
		return 'Particle: r = {}, v = {}, m = {}'.format(self.r, self.v, self.m)
	
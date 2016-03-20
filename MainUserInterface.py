import Space
import time
import random

from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

import EntryBox

class MainUserInterface:
	
	def __init__(self, master):
		self.master = master

		# create null space attribute
		self.space = Space.Space([]) 

		# config paned window with master Tk
		self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL)
		self.panedwindow.pack(fill = BOTH, expand = True)

		# add canvas and sidebar to paned window
		self.canvas = Canvas(self.panedwindow, width = 480, height = 320)
		#self.sidebar = ttk.Frame(self.panedwindow, width = 150, height = 300, relief = SUNKEN)
		#self.panedwindow.add(self.sidebar)
		self.panedwindow.add(self.canvas)

		# set up mouse clicking on canvas
		self.canvas.bind('<ButtonPress>', self.canvasPress)

		# Many random particles button TODO: Smoother animation for large number of particles
		# ttk.Button(self.sidebar, text = 'Random', command = self.runRandomSimulation).grid(row = 1, column = 0) 

	def runSimulation(self):
		# run simulation		
		while True:
			for particle in self.space.particles:
				oval = self.canvas.create_oval(particle.r.x, particle.r.y, particle.r.x + 3, particle.r.y + 3)
				self.canvas.itemconfigure(oval, fill = 'black')
				self.master.update()
				self.space.evolve()
				self.canvas.delete('all')

	def canvasPress(self, event):
		popup = EntryBox.EntryBox(self.master, self, event)
		self.master.wait_window(popup.textPrompt)
		self.runSimulation()

	
	def runRandomSimulation(self):
		pass 
		''' 
		self.space.particles = []

		for i in range(100):
			m = random.uniform(0, 10)
			rx = random.uniform(0, 300) 
			ry = random.uniform(0, 300) 
			vx = random.uniform(-3, 3) 
			vy = random.uniform(-3, 3) 

			r = Space.Vector(rx, ry)
			v = Space.Vector(vx, vy)
			particle = Space.Particle(r, v, m)

			self.space.addParticle(particle)
		'''


def main():
	root = Tk()
	MainUserInterface(root)
	mainloop()

if __name__ == '__main__': 
	main()
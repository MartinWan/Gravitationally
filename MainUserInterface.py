import Space
import time
import random

from Tkinter import *
import ttk
import tkMessageBox 
import ParticleEntryBox



class MainUserInterface:
	
	def __init__(self, master):
		''' Main user interface for the application with the following master-slave relationship:
			
			master
				panedwindow
					canvas
					sidebar
						random button
		'''

		master.title("Martin's N-body Simulation")
		master.resizable(False, False)

		# create empty space attribute
		self.space = Space.Space() 

		# config master and panedwindow
		self.master = master
		self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL)
		self.panedwindow.pack(fill = BOTH, expand = True)

		# config sidebar and canvas
		self.canvas = Canvas(self.panedwindow, width = 800, height = 640, background = 'black')
		self.sidebar = ttk.Frame(self.panedwindow, width = 150, height = 300)
		self.panedwindow.add(self.sidebar)
		self.panedwindow.add(self.canvas)

		# config mouse button press on canvas
		self.canvas.bind('<ButtonPress>', self.canvasPress)

		# config random button
		ttk.Button(self.sidebar, text = 'Random', command = self.runRandomSimulation).grid(row = 1, column = 0, padx = 3, pady = 3) 
		ttk.Button(self.sidebar, text = 'Clear', command = self.clear).grid(row = 10, column = 0, padx = 3, pady = 3) 

	def runSimulation(self):
		''' clear canvas and run simulation
		'''
		self.canvas.delete('all')

		while True:
			self.space.evolve()
			self.canvas.delete('all')

			for particle in self.space.getParticles():
				self.canvas.create_oval(particle.r.x, particle.r.y, particle.r.x + particle.d, particle.r.y + particle.d, fill = 'yellow')
			
			self.canvas.update()
		
	def canvasPress(self, event):
		''' Create popup entry box to add new particle onto canvas
		'''
		popup = ParticleEntryBox.ParticleEntryBox(self.master, self, event)
		self.master.wait_window(popup.textPrompt)
		self.runSimulation()

	def runRandomSimulation(self):
		''' run random simulation of n particles
		'''
		self.space.clearSpace()
		n = 140

		for i in range(n):
			m = random.uniform(100, 200)
			d = m / 50.0
			rx = random.uniform(100, 700) 
			ry = random.uniform(80, 540) 
			vx = random.uniform(-3, 3) 
			vy = random.uniform(-3, 3) 

			r = Space.Vector(rx, ry)
			v = Space.Vector(vx, vy)
			particle = Space.Particle(r, v, m, d)

			self.space.addParticle(particle)

		self.runSimulation()

	def clear(self):
		self.space.clearSpace()
		self.runSimulation()


def main():
	root = Tk()
	MainUserInterface(root)
	mainloop()

if __name__ == '__main__': 
	main()
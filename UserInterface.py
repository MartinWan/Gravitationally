import Space
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

class UserInterface:
	
	def __init__(self, master):
		self.master = master
		# create null space attribute
		self.space = None 

		# config main paned window with master Tk
		self.panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL)
		self.panedwindow.pack(fill = BOTH, expand = True)

		# create self.canvas and sidebar
		self.canvas = Canvas(self.panedwindow, width = 480, height = 320)
		sidebar = ttk.Frame(self.panedwindow, width = 150, height = 300, relief = SUNKEN)
		self.panedwindow.add(sidebar)
		self.panedwindow.add(self.canvas)
		
		# particle 1 position
		ttk.Label(sidebar, text = 'Particle 1 Position').grid(row = 0, column = 0)
		self.p1x = Entry(sidebar, width = 8)
		self.p1y = Entry(sidebar, width = 8)
		self.p1x.grid(row = 1, column = 0)
		self.p1y.grid(row = 1, column = 1)

		# particle 1 velocity 
		ttk.Label(sidebar, text = 'Particle 1 Velocity').grid(row = 2, column = 0)
		self.v1x = Entry(sidebar, width = 8)
		self.v1y = Entry(sidebar, width = 8)
		self.v1x.grid(row = 3, column = 0)
		self.v1y.grid(row = 3, column = 1)

		# particle 1 mass
		ttk.Label(sidebar, text = 'Particle 1 Mass').grid(row = 4, column = 0)
		self.m1 = Entry(sidebar, width = 8)
		self.m1.grid(row = 5, column = 0)

		# particle 2 position
		ttk.Label(sidebar, text = 'Particle 2 Position').grid(row = 6, column = 0)
		self.p2x = Entry(sidebar, width = 8)
		self.p2y = Entry(sidebar, width = 8)
		self.p2x.grid(row = 7, column = 0)
		self.p2y.grid(row = 7, column = 1)

		# particle 2 velocity 
		ttk.Label(sidebar, text = 'Particle 2 Velocity').grid(row = 8, column = 0)
		self.v2x = Entry(sidebar, width = 8)
		self.v2y = Entry(sidebar, width = 8)
		self.v2x.grid(row = 9, column = 0)
		self.v2y.grid(row = 9, column = 1)

		# particle 2 mass
		ttk.Label(sidebar, text = 'Particle 2 Mass').grid(row = 10, column = 0)
		self.m2 = Entry(sidebar, width = 8)
		self.m2.grid(row = 11, column = 0)		

		# Run Simulation button
		ttk.Button(sidebar, text = 'Run Simulation', command = self.runSimulation).grid(row = 14, column = 0)

		# set test case button
		ttk.Button(sidebar, text = 'Set Test', command = self.setTest).grid(row = 14, column = 1)

	def runSimulation(self):
		try:
			p1x = float(self.p1x.get())
			p1y = float(self.p1y.get())
			v1x = float(self.v1x.get())
			v1y = float(self.v1y.get())
			m1 = float(self.m1.get())

			p2x = float(self.p2x.get())
			p2y = float(self.p2y.get())
			v2x = float(self.v2x.get())
			v2y = float(self.v2y.get())
			m2 = float(self.m2.get())
		except:
			messagebox.showinfo(message = 'Please enter numbers in all fields')
			return

		# create position and velocity vectors
		r1 = Space.Vector(p1x, p1y)
		r2 = Space.Vector(p2x, p2y)
		v1 = Space.Vector(v1x, v1y)
		v2 = Space.Vector(v2x, v2y)

		# init particles
		particle1 = Space.Particle(r1, v1, m1)
		particle2 = Space.Particle(r2, v2, m2)
		
		particlelist = [particle1, particle2]

		# init space
		self.space = Space.Space(particlelist)

		# run simulation
		messagebox.showinfo(message = '{p1} \n {p2}'.format(p1 = particle1, p2 = particle2))
		self.canvas.delete('all')		
		while True:
			for particle in self.space.particles:
				self.canvas.create_oval(particle.r.x, particle.r.y, particle.r.x + 3, particle.r.y + 3)
				self.master.update()
				self.space.evolve()
				self.canvas.delete('all')

	def setTest(self):
		self.p1x.delete(0, 'end')
		self.p1y.delete(0, 'end')
		self.v1x.delete(0, 'end')
		self.v1y.delete(0, 'end')
		self.m1.delete(0, 'end')

		self.p2x.delete(0, 'end')
		self.p2y.delete(0, 'end')
		self.v2x.delete(0, 'end')
		self.v2y.delete(0, 'end')
		self.m2.delete(0, 'end')

		self.p1x.insert(0, '200')
		self.p1y.insert(0, '200')
		self.m1.insert(0, '1000')
		self.v1x.insert(0, '0')
		self.v1y.insert(0, '0')

		self.p2x.insert(0, '250')
		self.p2y.insert(0, '200')
		self.m2.insert(0, '10')
		self.v2x.insert(0, '0')
		self.v2y.insert(0, '3')

def main():
	root = Tk()
	UserInterface(root)
	mainloop()

	'''
		for i in range(1000000000):
			for particle in self.particles:
				self.canvas.create_oval(500 + particle.r.x, 500 + particle.r.y, particle.r.x + 505, particle.r.y + 505)
				animation.update()
				self.evolve()
		'''

if __name__ == '__main__': 
	main()
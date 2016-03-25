from Tkinter import *
import ttk
import tkMessageBox
import Space

class ParticleEntryBox:
	
	def __init__(self, master, parentInterface, event):
		''' A field particle entry box spawned by clicking on a canvas parent widget
		'''
		self.master = master
		self.parentInterface = parentInterface
		self.event = event
		
		self.textPrompt = Toplevel(master)
		self.textPrompt.wm_title('New Particle Entry')
		
		Label(self.textPrompt, text = 'Enter new particle mass:').grid(row = 0, column = 0, padx = 3, pady = 3)
		self.mass = Entry(self.textPrompt, width = 8)
		self.mass.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = 'sw')

		# config ok button
		ttk.Button(self.textPrompt, text = 'Ok', command = self.ok).grid(row = 3, column = 0, padx = 3, pady = 3)
		self.textPrompt.bind('<Return>', self.ok)
		
	def ok(self):
		try:
			mass = float(self.mass.get())
		except ValueError:
			tkMessageBox.showinfo('Value Error', message = 'Your was invalid. \nPlease enter a number')
			self.textPrompt.destroy()
			return

		particle = Space.Particle(Space.Vector(self.event.x, self.event.y), Space.Vector(0, 0), mass)
		self.parentInterface.space.addParticle(particle) 
		self.textPrompt.destroy()
		
		
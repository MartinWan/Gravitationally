from tkinter import *
from tkinter import ttk

import Space

class EntryBox:
	
	def __init__(self, master, parentInterface, event):
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
		
	def ok(self):
		particle = Space.Particle(Space.Vector(self.event.x, self.event.y), Space.Vector(0, 0), float(self.mass.get()))
		self.parentInterface.space.addParticle(particle)
		self.textPrompt.destroy()
		
		
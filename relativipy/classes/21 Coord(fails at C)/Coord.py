# -*- coding: utf-8 -*-
from relativipy import *

class Coord(object):
	def __init__(self, x0, x1, x2, x3):
		self.x0 = Symbol('%s' %x0)
		self.x1 = Symbol('%s' %x1)
		self.x2 = Symbol('%s' %x2)
		self.x3 = Symbol('%s' %x3)
		
	def coord(self):
		return (self.x0, self.x1, self.x2, self.x3)
	
	def printing(self):
		pprint(self.coord())
		
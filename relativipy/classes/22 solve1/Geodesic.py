# -*- coding: utf-8 -*-
from relativipy import *

class Geodesic(object):
	def __init__(self, tau, C ):
		self.x = C.x
		self.tau = Symbol('tau')
		self.C = C
		
		
	def value(self,i):
		x = self.x
		tau = self.tau
		C = self.C
		r = diff(x[i](tau), tau, tau)
		s=0
		for j in range(4):
				for k in range(4):
					s += C.udd(i,j,k)*( diff(x[j](tau), tau))*( diff(x[k](tau), tau))
		return r+s
	
	def printing(self):
		print('Geodesic equations:')
		for i in range(4):
			r = pprint(Eq(Symbol('Eq(%i)= 0' %i), self.value(i)))
		return r
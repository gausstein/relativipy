# -*- coding: utf-8 -*-
from relativipy import *

class Einstein(Tensor):
    def __init__(self, Ric, g, Rs, dim=4, tensortype=(0,2), symbol='G'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.g = g
		self.Ric = Ric
		self.Rs = Rs
		self.dim = dim

    def dd(self, i, j):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        r=0
        for i in range(self.dim):
            for j in range(self.dim):
                r += Ric.dd(i,j) - 0.5*Rs.value()*g.dd(i,j)
        return r
    
    def ddsimplified(self, i, j):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        r=0
        for i in range(self.dim):
            for j in range(self.dim):
                r += Ric.ddsimplified(i,j) - 0.5*Rs.valuesimplified()*g.dd(i,j)
        return apart(self.dd(i, j), self.Ric.x[1])
        
    def printing(self, i, j):
		return pprint(Eq(Symbol('G_%i%i' % (i,j)), self.dd(i,j)))

    def nonzero(self):
		print'-'*40
		print'Einstein tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.dd(i,j) !=0:#create a method named value
					self.printing(i,j)
		print'-'*40
	
    def nonzerosimplified(self):
		check = 0
		print'-'*40
		print'Einstein tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.ddsimplified(i,j) !=0:#create a method named value
					self.printing(i,j)
					check = self.ddsimplified(i,j)
		if check == 0: print 'All Einstein tensor components are zero'
		print'-'*40





# -*- coding: utf-8 -*-
from relativipy import *

class EFE(Tensor):
    def __init__(self, G, T, dim=4, tensortype=(0,2), symbol='EFE'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.G = G
		self.T = T
	
    def equation(self):
		G = self.G
		T = self.T
		r= G.matrixvalue() - 8*pi*T.matrix()
		return r
	
    def nonzero(self):
		check = 0
		print'-'*40
		print'EFE:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.equation()[i,j] != 0: #create a method named value
					print 'Eq(%i %i)' %(i,j)
					pprint(self.equation()[i,j])
					check = self.equation()[i,j]
		if check == 0: print 'All EFE are zero'
		print'-'*40
    
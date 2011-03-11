# -*- coding: utf-8 -*-
from relativipy import *

class EFE(Tensor):
    def __init__(self, G, T, dim=4, tensortype=(0,2), symbol='EFE'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.G = G
		self.T = T
	
    def matrix(self):
		G = self.G
		T = self.T
		return G.matrix() - 8*pi*T.matrix()


    def nonzero(self):
		check = 0
		print'-'*40
		print'EFE:'
		for i in range(self.dim):
			for j in range(self.dim):
				if simplify(self.matrix()[i,j]) != 0: #create a method named value
					print 'Component (%i %i)' %(i,j)
					pprint(simplify(self.matrix()[i,j]))
					check = self.matrix()[i,j]
		if check == 0: print 'All EFE are zero'
		print'-'*40
    
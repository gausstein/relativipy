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
# -*- coding: utf-8 -*-
from sympy import *
from Tensor import *
#from Metric import *
#from Ricci import *
#from Rscalar import *

class ET(Tensor):
    def __init__(self, Ric, g, Rs, dim=4, tensortype=(0,2), symbol='G'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.g = g
		self.Ric = Ric
		self.Rs = Rs
		self.dim = dim

    def dd(self):
        r=0
        for i in range(self.dim):
            for j in range(dim):
                r += Ric.dd(i,j) - 0.5*R*g.dd(i,j)
        return r
        
    def printing(self, i, j):
		self.i = i
		self.j = j
		return pprint(Eq(Symbol('G_%i%i' % (i,j)), self.dd(i,j)))

    def nonzero(self):
		print'-'*40
		print'Einstein tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.dd(i,j) !=0:#create a method named value
					self.printing(i,j)
		print'-'*40





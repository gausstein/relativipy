# -*- coding: utf-8 -*-
from relativipy import *
from sympy import *
class Einstein(Tensor):
    def __init__(self, Rs, dim=4, tensortype=(0,2), symbol='G'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.Rs = Rs
		self.Ric = Rs.Ric
		self.g = Rs.Ric.g
		self.dim = dim

    def dd(self, i, j):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        r=0
        for i in range(self.dim):
            for j in range(self.dim):
                r += Ric.dd(i,j) - 0.5*simplify(Rs.value())*g.dd(i,j)
        return simplify(r)
        
    def matrix(self):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        return Ric.matrix() - 0.5*Rs.value()*g.matrix()
        
    
    def printing(self, i, j):
		return pprint(Eq(Symbol('G_%i%i' % (i,j)), simplify(self.matrix()[i,j])))

    def nonzero(self):
		check = 0
		print'-'*40
		print'Einstein tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if simplify(self.matrix()[i,j]) !=0:#create a method named value
					self.printing(i,j)
					check = self.matrix()[i,j]
		if check == 0: print 'All Einstein tensor components are zero'
		print'-'*40





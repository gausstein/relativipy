# -*- coding: utf-8 -*-
from sympy import *
from Tensor import *
class Christoffel(Tensor):
    def __init__(self,g,x, dim=4, tensortype=(1,2), symbol='Gamma'):
        Tensor.__init__(self, symbol, tensortype, dim) 
        self.g = g
        self.x = x
        self.dim = dim

    def udd(self,i,k,l):
        g=self.g
        x=self.x
        r=0
        for m in range(self.dim):
            r+=g.uu(i,m)/2 * (g.dd(m,k).diff(x[l])+g.dd(m,l).diff(x[k]) \
                    - g.dd(k,l).diff(x[m]))
        return r
     
    def printing(self, i,k,l):
		self.i= i
		self.k = k
		self.l = l
		return pprint(Eq(Symbol('Gamma^%i_%i%i' % (i,k,l)) , self.udd(i,k,l)))
     
    def nonzero(self):
		print '-'*40
		print 'Christoffel symbols:'
		for i in range(self.dim):
			for k in range(self.dim):
				for l in range(self.dim):
					if self.udd(i,k,l) != 0 :
						self.printing(i,k,l)
		print'-'*40
# -*- coding: utf-8 -*-
from relativipy import *

class EFE(Tensor):
    def __init__(self,G, x, dim=4, tensortype=(0,2), symbol='EFE'):
        Tensor.__init__(self, symbol, tensortype, dim) 
        self.R = R
        self.x = x
        self.g = R.G.g
        self.dim = dim

    def dd(self,mu,nu):
        R=self.R
        x=self.x
        r=0
        for lam in range(self.dim):
            r+=R.uddd(lam,mu,lam,mu)
        return r

    def ud(self,mu,nu):
        r=0
        for lam in range(self.dim):
            r+=self.g.uu(mu,lam)*self.dd(lam, mu)
        return r.expand()
        
    def printing(self, i, j):
		self.i = i
		self.j = j
		return pprint(Eq(Symbol('R_%i%i' % (i,j)), self.dd(i,j)))

    def nonzero(self):
		print'-'*40
		print'Ricci tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.dd(i,j) !=0:#create a method named value
					self.printing(i,j)
		print'-'*40

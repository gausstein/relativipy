# -*- coding: utf-8 -*-
from relativipy import *

class Ricci(Tensor):
    def __init__(self,Rmn, x, dim=4, tensortype=(0,2), symbol='Ric'):
        Tensor.__init__(self, symbol, tensortype, dim) 
        self.Rmn = Rmn
        self.x = x
        self.g = Rmn.C.g
        self.dim = dim

    def dd(self,mu,nu):
        Rmn=self.Rmn
        x=self.x
        r=0
        for lam in range(self.dim):
            r+=Rmn.uddd(lam,mu,lam,nu)
        return r
        
    def ddsimplified(self, i, j):
        return apart(self.dd(i, j), self.x[1])

    def ud(self,mu,nu):
        r=0
        for lam in range(self.dim):
            r+=self.g.uu(mu,lam)*self.dd(lam, mu)
        return r
        
    def printing(self, i, j):
		self.i = i
		self.j = j
		return pprint(Eq(Symbol('R_%i%i' % (i,j)), self.dd(i,j)))

    def nonzero(self):
		print'-'*40
		print'Ricci tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.dd(i,j) !=0:
					self.printing(i,j)
		print'-'*40
	
    def nonzerosimplified(self):
		check = 0
		print'-'*40
		print'Ricci tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.ddsimplified(i,j) !=0:#create a method named value
					self.printing(i,j)
					check = self.ddsimplified(i,j)
		if check == 0: print 'All Ricci tensor components are zero'
		print'-'*40

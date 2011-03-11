# -*- coding: utf-8 -*-
from relativipy import *

class Riemann(Tensor):
    def __init__(self,G,x, dim=4, tensortype=(0,2), symbol='Rn'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.G = G
        self.x = x
        self.dim = dim

    def uddd(self,rho,sigma,mu,nu):
        G=self.G
        x=self.x
        r=-G.udd(rho,nu,sigma).diff(x[mu])+G.udd(rho,mu,sigma).diff(x[nu])
        for lam in range(self.dim):
            r+=-G.udd(rho,mu,lam)*G.udd(lam,nu,sigma) \
                +G.udd(rho,nu,lam)*G.udd(lam,mu,sigma)
        return r

    def printing(self, i, j, k,l):
		self.i = i
		self.j = j
		self.k = k
		self.l = l
		return pprint(Eq(Symbol( 'R^%i_%i%i%i' % (i,j,k,l)) , self.uddd(i,j,k,l) ))
		
    def nonzero(self):
		print '-'*40
		print 'Riemann tensor' 
		for i in range(self.dim):
			for j in range(self.dim):
				for k in range(self.dim):
					for l in range(self.dim):
						if self.uddd(i,j,k,l) != 0 :
							self.printing(i,j,k,l)
		print '-'*40

# -*- coding: utf-8 -*-
from relativipy import *

class Riemann(Tensor):
    def __init__(self,C,x, dim=4, tensortype=(0,2), symbol='Rn'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.C = C
        self.x = x
        self.dim = dim

    def uddd(self,rho,sigma,mu,nu):
        C=self.C
        x=self.x
        r=C.udd(rho,nu,sigma).diff(x[mu])-C.udd(rho,mu,sigma).diff(x[nu])
        for lam in range(self.dim):
            r+=C.udd(rho,mu,lam)*C.udd(lam,nu,sigma) \
                -C.udd(rho,nu,lam)*C.udd(lam,mu,sigma)
        return r

    def udddsimplified(self,i,j, k, l):
		return apart( self.uddd(i,j, k, l) , self.x[1])
    
    def printing(self, i, j, k,l):
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
		
    def nonzerosimplified(self):
		print '-'*40
		print 'Riemann tensor' 
		for i in range(self.dim):
			for j in range(self.dim):
				for k in range(self.dim):
					for l in range(self.dim):
						if self.udddsimplified(i,j,k,l) != 0 :
							self.printing(i,j,k,l)
							check = self.udddsimplified(i,j, k, l)
		if check == 0: print 'All Ricci tensor components are zero'
		print'-'*40
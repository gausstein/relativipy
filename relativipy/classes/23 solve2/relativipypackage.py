# -*- coding: utf-8 -*-
from sympy import *
from scipy import *
from numpy import *

class Tensor:
	def __init__(self, symbol, tensortype, dim ):
		self.symbol = Symbol('symbol')
		self.dimM = dim
		self.tensortype = tensortype
		#self.shape = shape

#************************************************************************************************************************************************************************
class Metric(Tensor):
    def __init__(self,m, dim=4, tensortype=(0,2), symbol='g'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.m = Matrix(m)
        self.gdd=Matrix(m)
        self.guu=Matrix(m).inv()
        
    def matrix(self):
		return Matrix(self.m)
#convert to string for printing
    def __str__(self):
        return 'g_dd =\n' + str(self.gdd)

    def dd(self,i,j):
        return self.gdd[i,j]

    def uu(self,i,j):
        return self.guu[i,j]

#************************************************************************************************************************************************************************

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
		
		


#************************************************************************************************************************************************************************
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
		
		
#************************************************************************************************************************************************************************

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

#************************************************************************************************************************************************************************

class Rscalar(object):
	def __init__(self, Ric):
		self.Ric = Ric
		
	def value(self):
		Ric = self.Ric
		return Ric.ud(0,0)+Ric.ud(1,1)+Ric.ud(2,2)+Ric.ud(3,3)

	def printing(self):
		print 'Scalar curvature:'
		return pprint(Eq(Symbol( 'R') , self.value() ))
	
	def valuesimplified(self):
		Ric = self.Ric
		return apart( self.value(), Ric.x[1] )

	def printingsimplified(self):
		print 'Scalar curvature:'
		return pprint(Eq(Symbol( 'R') , self.valuesimplified() ))

#************************************************************************************************************************************************************************

class Einstein(Tensor):
    def __init__(self, Ric, g, Rs, dim=4, tensortype=(0,2), symbol='G'):
		Tensor.__init__(self, symbol, tensortype, dim )
		self.g = g
		self.Ric = Ric
		self.Rs = Rs
		self.dim = dim

    def dd(self, i, j):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        r=0
        for i in range(self.dim):
            for j in range(self.dim):
                r += Ric.dd(i,j) - 0.5*Rs.value()*g.dd(i,j)
        return r
    
    def ddsimplified(self, i, j):
        g = self.g
        Ric = self.Ric
        Rs = self.Rs
        r=0
        for i in range(self.dim):
            for j in range(self.dim):
                r += Ric.ddsimplified(i,j) - 0.5*Rs.valuesimplified()*g.dd(i,j)
        return apart(self.dd(i, j), self.Ric.x[1])
        
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
	
    def nonzerosimplified(self):
		check = 0
		print'-'*40
		print'Einstein tensor:'
		for i in range(self.dim):
			for j in range(self.dim):
				if self.ddsimplified(i,j) !=0:#create a method named value
					self.printing(i,j)
					check = self.ddsimplified(i,j)
		if check == 0: print 'All Einstein tensor components are zero'
		print'-'*40

#************************************************************************************************************************************************************************


class EM(Tensor):
    def __init__(self,m, dim=4, tensortype=(0,2), symbol='T'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.m = Matrix(m)
        self.Tdd=Matrix(m)
        self.Tuu=Matrix(m).inv()
        
    def matrix(self):
		return Matrix(self.m)
#convert to string for printing
    def __str__(self):
        return 'T_dd =\n' + str(self.Tdd)

    def dd(self,i,j):
        return self.Tdd[i,j]

    def uu(self,i,j):
        return self.Tuu[i,j]

#************************************************************************************************************************************************************************

#EFE
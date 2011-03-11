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
					pprint(Eq(Symbol('Equation(%i) = 0 ' %i), simplify(self.matrix()[i,j])) )
					check = self.matrix()[i,j]
		if check == 0: print 'All EFE are zero'
		print'-'*40
	
    def solution(self, A, B):
		r = Symbol('r')
		self.A = Function('A')(r)
		self.B = Function('B')(r)
		for i in range(self.dim):
			for j in range(self.dim):
				if simplify(self.matrix()[i,j]) != 0:
					if (diff(A(r),r) or diff(A(r), r, r) ) in simplify(self.matrix()[i,j]):
						pprint(dsolve(simplify(self.matrix()[i,j]), A(r)))
					if (diff(B(r),r) or diff(B(r), r, r) ) in simplify(self.matrix()[i,j]):
						pprint(dsolve(simplify(self.matrix()[i,j]), B(r)))
 
 #pprint(Eq(Symbol('Eq(%i)= 0' %i), self.value(i)))   
# -*- coding: utf-8 -*-
#dimM: dimension of the manifold
#tensortype: 2-dimensional array
from sympy import *
from scipy import *
from numpy import *
class Tensor:
	def __init__(self, symbol, dimM, tensortype, shape ):
		self.symbol = Symbol(symbol)
		self.dimM = dimM
		self.tensortype = tensortype
		self.shape = shape
	
	#def __str__():
	#	return Tensor.pprint

	def dd(self, i, j):
			r= [1, 7]
			return r

T = Tensor('T', 4, (0,2), 1)
def pprint_Tensor_dd(i,j):
	pprint(Eq(Symbol('T_%i%i' % (0, 1)), T.dd(0,1)))

pprint_Tensor_dd(0,1) 
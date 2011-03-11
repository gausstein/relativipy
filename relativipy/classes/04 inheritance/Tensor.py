# -*- coding: utf-8 -*-
#dimM: dimension of the manifold
#tensortype: 2-dimensional array
#shape
from sympy import *
from scipy import *
from numpy import *
class Tensor:
	def __init__(self, symbol, tensortype, dim ):
		self.symbol = Symbol(symbol)
		self.dimM = dim
		self.tensortype = tensortype
		#self.shape = shape
		
	

#T = Tensor('T', 4, (0,2), 1)
#def pprint_Tensor_dd(i,j):
#pprint(Eq(Symbol('T_%i%i' % (0, 1)), T.dd(0,1)))

#pprint_Tensor_dd(0,1) 
# -*- coding: utf-8 -*-
#dim: dimension of the manifold
#tensortype: 2-dimensional array
#shape
from sympy import *
from scipy import *
from numpy import *
class Tensor:
	def __init__(self, symbol, tensortype, dim ):
		self.symbol = Symbol('symbol')
		self.dim = dim
		self.tensortype = tensortype
		
	def matrix(self):
		return Matrix(self.dim, self.dim, lambda i,j: self.dd(i,j))
		
	def ppmatrix(self):
		return pprint(self.matrix())
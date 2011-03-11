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
		self.dimM = dim
		self.tensortype = tensortype
		#self.shape = shape
		
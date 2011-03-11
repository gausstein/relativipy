# -*- coding: utf-8 -*-
from relativipy import *

class Rscalar(object):
	def __init__(self, Ric):
		self.Ric = Ric
		
	def value(self):
		Ric = self.Ric
		r=0
		for i in range(Ric.dim):
			r += simplify(Ric.ud(i,i))
		return simplify(r)

	def printing(self):
		print 'Scalar curvature:'
		return pprint(Eq(Symbol( 'R') , self.value() ))
	
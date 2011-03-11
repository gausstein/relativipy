# -*- coding: utf-8 -*-
from relativipy import *

class Rscalar(object):
	def __init__(self, Ric):
		self.Ric = Ric
		
	def value(self):
		Ric = self.Ric
		return simplify(Ric.ud(0,0)+Ric.ud(1,1)+Ric.ud(2,2)+Ric.ud(3,3))

	def printing(self):
		print 'Scalar curvature:'
		return pprint(Eq(Symbol( 'R') , self.value() ))
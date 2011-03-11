# -*- coding: utf-8 -*-
from sympy import *
class Rscalar(object):
	def __init__(self, Rmn):
		self.Rmn = Rmn
		
	def value(self):
		Rmn = self.Rmn
		return Rmn.ud(0,0)+Rmn.ud(1,1)+Rmn.ud(2,2)+Rmn.ud(3,3)

	def printing(self):
		return pprint(Eq(Symbol( 'R') , self.value() ))
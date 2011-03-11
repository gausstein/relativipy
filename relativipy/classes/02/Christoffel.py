# -*- coding: utf-8 -*-
from sympy import *
class Christoffel(object):
    def __init__(self,g,x):
        self.g = g
        self.x = x

    def udd(self,i,k,l):
        g=self.g
        x=self.x
        r=0
        for m in [0,1,2,3]:
            r+=g.uu(i,m)/2 * (g.dd(m,k).diff(x[l])+g.dd(m,l).diff(x[k]) \
                    - g.dd(k,l).diff(x[m]))
        return r
     
    def printing(self, i,k,l):
		self.i= i
		self.k = k
		self.l = l
		return pprint(Eq(Symbol('Gamma^%i_%i%i' % (i,k,l)) , self.udd(i,k,l)))
     
		
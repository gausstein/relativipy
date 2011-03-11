# -*- coding: utf-8 -*-
from relativipy import *
from sympy import *
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
    
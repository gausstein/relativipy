# -*- coding: utf-8 -*-
from relativipy import *
from sympy import *
class EM(Tensor):
    def __init__(self,m, dim=4, tensortype=(0,2), symbol='T'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.m = Matrix(m)
        self.Tdd=Matrix(m)
        self.Tuu=Matrix(m).inv()
        
    def matrix(self):
		return Matrix(self.m)
#convert to string for printing
    def __str__(self):
        return 'T_dd =\n' + str(self.Tdd)

    def dd(self,i,j):
        return self.Tdd[i,j]

    def uu(self,i,j):
        return self.Tuu[i,j]
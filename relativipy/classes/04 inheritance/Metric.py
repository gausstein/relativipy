#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
from Tensor import *

class Metric(Tensor):
    def __init__(self,m, dim=4, tensortype=(0,2), symbol='g'):
        Tensor.__init__(self, symbol, tensortype, dim)
        self.gdd=m
        self.guu=m.inv()
        

#convert to string for printing
    def __str__(self):
        return 'g_dd =\n' + str(self.gdd)

    def dd(self,i,j):
        return self.gdd[i,j]

    def uu(self,i,j):
        return self.guu[i,j]
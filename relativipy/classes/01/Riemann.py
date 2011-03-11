# -*- coding: utf-8 -*-
from sympy import *
class Riemann(object):
    def __init__(self,G,x):
        self.G = G
        self.x = x

    def uddd(self,rho,sigma,mu,nu):
        G=self.G
        x=self.x
        r=-G.udd(rho,nu,sigma).diff(x[mu])+G.udd(rho,mu,sigma).diff(x[nu])
        for lam in [0,1,2,3]:
            r+=-G.udd(rho,mu,lam)*G.udd(lam,nu,sigma) \
                +G.udd(rho,nu,lam)*G.udd(lam,mu,sigma)
        return r
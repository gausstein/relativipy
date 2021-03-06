# -*- coding: utf-8 -*-
class Ricci(object):
    def __init__(self,R,x):
        self.R = R
        self.x = x
        self.g = R.G.g

    def dd(self,mu,B):
        R=self.R
        x=self.x
        r=0
        for lam in [0,1,2,3]:
            r+=R.uddd(lam,mu,lam,mu)
        return r

    def ud(self,mu,B):
        r=0
        for lam in [0,1,2,3]:
            r+=self.g.uu(mu,lam)*self.dd(lam, mu)
        return r.expand()
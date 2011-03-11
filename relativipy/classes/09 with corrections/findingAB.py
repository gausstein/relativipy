#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import Symbol, sin, Rational, Derivative, dsolve, Function, \
                  Matrix, Eq, pprint, Pow, classify_ode

class MT(object):
#constructor
    def __init__(self,m):
    #initializing the attributes
        self.gdd=m
        self.guu=m.inv()

#convert to string for printing
    def __str__(self):
        return 'g_dd =\n' + str(self.gdd)

    def dd(self,i,j):
        return self.gdd[i,j]

    def uu(self,i,j):
        return self.guu[i,j]

class G(object):
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

class Ricci(object):
    def __init__(self,R,x):
        self.R = R
        self.x = x
        self.g = R.G.g

    def dd(self,mu,nu):
        R=self.R
        x=self.x
        r=0
        for lam in [0,1,2,3]:
            r+=R.uddd(lam,mu,lam,nu)
        return r

    def ud(self,mu,B):
        r=0
        for lam in [0,1,2,3]:
            r+=self.g.uu(mu,lam)*self.dd(lam, mu)
        return r.expand()

def curvature(Rmn):
    return Rmn.ud(0,0)+Rmn.ud(1,1)+Rmn.ud(2,2)+Rmn.ud(3,3)

B= Function('B')
A= Function('A')

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

#general, spherically symmetric metric
gdd=Matrix((
    (-B(r),0,0,0),
    (0, A(r), 0, 0),
    (0, 0, r**2, 0),
    (0, 0, 0, r**2*sin(theta)**2)
    ))

g=MT(gdd)
X=(t,r,theta,phi)
Gamma=G(g,X)
Rmn=Ricci(Riemann(Gamma,X),X)

def pprint_Gamma_udd(i,k,l):
    pprint(Eq(Symbol('Gamma^%i_%i%i' % (i,k,l)), Gamma.udd(i,k,l)))

def pprint_Rmn_dd(i,j):
    pprint(Eq(Symbol('R_%i%i' % (i,j)), Rmn.dd(i,j)))

def main():

    print 'Initial metric:'
    pprint(gdd)
    print '-'*40
    print 'Christoffel symbols:'
    for i in [0,1,2,3]:
    	for k in [0,1,2,3]:
    		for l in [0,1,2,3]:
    			if Gamma.udd(i,k,l) != 0 :
		    		pprint_Gamma_udd(i,k,l)
    print'-'*40
    print'Ricci tensor:'
    for i in [0,1,2,3]:
    	for j in [0,1,2,3]:
    		if Rmn.dd(i,j) !=0:
    			pprint_Rmn_dd(i,j)
    
    print '-'*40
    #Solving EFE for A and B
    s = ( Rmn.dd(1,1)/ A(r) ) + ( Rmn.dd(0,0)/ B(r) )
    pprint (s)
    t = dsolve(s, A(r))
    pprint(t)
    metric = gdd.subs(A(r), t)
    print "metric:"
    pprint(metric)
    r22 = Rmn.dd(3,3).subs( A(r), 1/B(r))
    h = dsolve( r22, B(r) )
    pprint(h)
    
if __name__ == '__main__':
    main()

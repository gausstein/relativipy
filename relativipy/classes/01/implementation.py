#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
from Metric import *
from Christoffel import *
from Riemann import *
from Ricci import *
from Rscalar import *

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

g=Metric(gdd)
X=(t,r,theta,phi)
Gamma=Christoffel(g,X)
Ric=Ricci(Riemann(Gamma,X),X)

def pprint_Gamma_udd(i,k,l):
    pprint(Eq(Symbol('Gamma^%i_%i%i' % (i,k,l)), Gamma.udd(i,k,l)))

def pprint_Ric_dd(i,j):
    pprint(Eq(Symbol('R_%i%i' % (i,j)), Ric.dd(i,j)))

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
   		if Ric.dd(i,j) !=0:
			pprint_Ric_dd(i,j)


print '-'*40
#Solving EFE for A and B
s = ( Ric.dd(1,1)/ A(r) ) + ( Ric.dd(0,0)/ B(r) )
pprint (s)
t = dsolve(s, A(r))
pprint(t)
metric = gdd.subs(A(r), t)
print "metric:"
pprint(metric)
r22 = Ric.dd(3,3).subs( A(r), 1/B(r))
h = dsolve( r22, B(r) )
pprint(h)

Rs =Rscalar(Ric)
print Rs.value() 
    
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
Rie = Riemann(Gamma,X)
Ric=Ricci(Rie,X)
Rs =Rscalar(Ric)

print 'Initial metric:'
pprint(gdd)

Gamma.nonzero()
Ric.nonzero()
#Rie.nonzero()
Rs.printing() 

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

    
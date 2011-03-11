#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
from Metric import *
from Christoffel import *
from Riemann import *
from Ricci import *
from Rscalar import *
from ET import *

B= Function('B')
A= Function('A')

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

#general, spherically symmetric metric


g=Metric(   (  (-B(r),0,0,0), (0, A(r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C,x)
Ric=Ricci( Rie,x)
Rs =Rscalar(Ric)
G = ET(Ric, g, Rs)

print 'Initial metric:'
pprint(g.matrix())
C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
G.nonzero()

print '-'*40
#Solving EFE for A and B
s = ( Ric.dd(1,1)/ A(r) ) + ( Ric.dd(0,0)/ B(r) )
#pprint (s)
t = dsolve(s, A(r))
pprint(t)
metric = g.matrix().subs(A(r), t)
print "metric:"
pprint(metric)
r22 = Ric.dd(3,3).subs( A(r), 1/B(r))
h = dsolve( r22, B(r) )
pprint(h)

    
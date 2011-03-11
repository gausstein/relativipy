#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy import *
from Metric import *
from Christoffel import *
from Riemann import *
from Ricci import *
from Rscalar import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

A= Function('A')
K = Symbol('K')

#general, spherically symmetric metric
gdd=Matrix((
    (-1,0,0,0),
    (0, A(t)/(1 - K*r**2), 0, 0),
    (0, 0, A(t)*r**2, 0),
    (0, 0, 0, A(t)*r**2*sin(theta)**2)
    ))

g=Metric(gdd)
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C,x)
Ric=Ricci( Rie,x)
Rs =Rscalar(Ric)


print 'Initial metric:'
pprint(gdd)
C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 

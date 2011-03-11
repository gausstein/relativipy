# -*- coding: utf-8 -*-
from relativipy import *

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

tau = Symbol('tau')

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
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
geo = Geodesic(tau, C)

print 'Initial metric:'
pprint(gdd)
C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 

geo.printing()
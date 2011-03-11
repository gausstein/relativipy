# -*- coding: utf-8 -*-
from relativipy import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

M= Symbol('M')
rho = Symbol('rho')
P = Symbol('P')
tau = Symbol('tau')

g=Metric(   (  ( ( 2*M/r - 1 ),0,0,0), (0, 1/(1- 2*M/r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho, 0,0,0), (0,P,0,0), (0,0,P,0), (0,0,0,P)   )   )
e = EFE(G, T)
geo = Geodesic(tau,C)

print 'Initial metric:'
pprint(g.matrix())
#g.ppmatrix()
#C.nonzero()
Ric.nonzero()
#Ric.matrix()
#pprint(Ric.matrix())
#Rie.nonzero()
#Rs.printing()
#pprint(G.matrix())
#e.matrix()
#geo.printing()
#geo.printing()

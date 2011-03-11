# -*- coding: utf-8 -*-
from relativipy import *

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Symbol('rho')
P = Symbol('P')
tau = Symbol('tau')

A= Function('A')(t)
B= Function('B')(t)
C= Function('C')(t)

x=(t,r,theta,phi)

g=Metric(   (  (-1,0,0,0), (0, A, 0, 0), (0, 0, B*r**2, 0), (0, 0, 0, C*r**2*sin(theta)**2 )   )  )

C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)

print 'The Kasner solutions'
T = EM( zeros(g.dim)  )
e = EFE(G, T)
geo = Geodesic(tau,C)

print 'Initial metric:'
g.ppmatrix()
C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing()
#G.matrix()
e.nonzero()
geo.printing()
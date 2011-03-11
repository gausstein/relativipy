# -*- coding: utf-8 -*-
from relativipy import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Symbol('rho')
P = Symbol('P')
tau = Symbol('tau')


A= Function('A')
B= Function('B')
C= Function('C')
D= Function('D')


x=(t,r,theta,phi)

g=Metric(   (  (A(t,r,theta,phi),0,0,0), (0, B(t,r,theta,phi), 0, 0), (0, 0, C(t,r,theta,phi)*r**2, 0), (0, 0, 0, D(t,r,theta,phi)*r**2*sin(theta)**2 )   )  )

C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho, 0,0,0), (0,P,0,0), (0,0,P,0), (0,0,0,P)   )   )
e = EFE(G, T)
geo = Geodesic(tau,C)

print 'Initial metric:'
g.ppmatrix()
C.nonzero()
#Ric.nonzero()
Ric.matrix()
Rie.nonzero()
Rs.printing()
G.matrix()
e.matrix()
geo.printing()
# -*- coding: utf-8 -*-
from relativipy import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Symbol('rho')
P = Symbol('P')
tau = Symbol('tau')


A= Function('A')(t,r,theta,phi)
B= Function('B')(t,r,theta,phi)
C= Function('C')(t,r,theta,phi)
D= Function('D')(t,r,theta,phi)


x=(t,r,theta,phi)

g=Metric(   (  (A,0,0,0), (0, B, 0, 0), (0, 0, C*r**2, 0), (0, 0, 0, D*r**2*sin(theta)**2 )   )  )

C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho*B, 0,0,0), (0,P*A,0,0), (0,0,P*r**2,0), (0,0,0,P*r**2*sin(theta))   )   )
e = EFE(G, T)
geo = Geodesic(tau,C)

print 'Initial metric:'
g.ppmatrix()
C.nonzero()
#Ric.nonzero()
#Ric.matrix()
#Rie.nonzero()
#Rs.printing()
#G.matrix()
#e.matrix()
geo.printing()
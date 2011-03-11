# -*- coding: utf-8 -*-
from relativipy import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

M= Symbol('M')


g=Metric(   (  ( ( 2*M/r - 1 ),0,0,0), (0, 1/(1- 2*M/r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C,x)
Ric=Ricci( Rie,x)
Rs =Rscalar(Ric)
G = Einstein(Ric, g, Rs)
#T = EM(  )

print 'Initial metric:'
pprint(g.matrix())
C.nonzero()
Ric.nonzero()
Rie.nonzero()
Rs.printing() 
#G.nonzero()



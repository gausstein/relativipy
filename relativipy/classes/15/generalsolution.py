# -*- coding: utf-8 -*-
from relativipy import *


t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

A= Function('A')
B= Function('B')
C= Function('C')
D= Function('D')

x=(t,r,theta,phi)

g=Metric(   (  (A(t,r,theta,phi),0,0,0), (0, B(t,r,theta,phi), 0, 0), (0, 0, C(t,r,theta,phi)*r**2, 0), (0, 0, 0, D(t,r,theta,phi)*r**2*sin(theta)**2 )   )  )

C=Christoffel(g,x)
Rie = Riemann(C,x)
Ric=Ricci( Rie,x)
Rs =Rscalar(Ric)
G = Einstein(Ric, g, Rs)
#T = EM(  )

print 'Initial metric:'
pprint(g.matrix())
C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
#G.nonzero()


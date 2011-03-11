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



print 'Initial metric:'
g.ppmatrix()
#C.nonzero()
#Rie.nonzero()
#Rs.printingsimplified()
print 'G.ddmatrix()'
#G.ddmatrix()
print '*'*40
pprint(simplify(G.dd(0,0)))
print '*'*40
print G.dd
#G.ppmatrix()

#print g.matrix()

#Ricc.ppmatrix()


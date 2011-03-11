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
Ricc=Ricci( Rie,x)
#Rs =Rscalar(Ricc)
#G = Einstein(Ricc, g, Rs)



print 'Initial metric:'
g.ppmatrix()
#C.nonzero()
#Ricc.nonzerosimplified()
#Rie.nonzero()
#Rs.printingsimplified()
#G.nonzero()

#print Ricc.matrix()
#print g.matrix()

#Ricci = Matrix(((Ricc.dd(0,0),Ricc.dd(0,1),Ricc.dd(0,2),Ricc.dd(0,3)),
				#(Ricc.dd(1,0),Ricc.dd(1,1),Ricc.dd(1,2),Ricc.dd(1,3)),
				#(Ricc.dd(2,0),Ricc.dd(2,1),Ricc.dd(2,2),Ricc.dd(2,3)),
				#(Ricc.dd(3,0),Ricc.dd(3,1),Ricc.dd(3,2),Ricc.dd(3,3))
				#) )

#Ricc.ppmatrix()
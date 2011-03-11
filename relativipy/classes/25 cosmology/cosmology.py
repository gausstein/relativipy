# -*- coding: utf-8 -*-
from relativipy import *
'''
General spherical metric
'''
t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Function('rho')(r)
P = Function('P')(r)
tau = Symbol('tau')


A= Function('A')(r)

g=Metric(   (  (-1.0,0,0,0), (0, A**2, 0, 0), (0, 0, A**2*r**2, 0), (0, 0, 0, A**2*r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (-rho, 0,0,0), (0,A**2*P,0,0), (0,0,A**2*P*r**2,0), (0,0,0,A**2*P*r**2*sin(theta)**2)   )   )
e = EFE(G, T)

print 'Initial metric:'
#pprint(g.matrix())
#C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing()
#pprint(G.matrix())
#pprint(T.matrix())
#pprint(e.matrix())
#e.nonzero()
'''
For Dust P=0
'''
#T = EM( (  (-rho, 0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)   )   )
#e = EFE(G, T)
#e.nonzero()
'''
For Radiation P= rho/3
'''
P = rho/3
T = EM( (  (-rho, 0,0,0), (0,A**2*P,0,0), (0,0,A**2*P*r**2,0), (0,0,0,A**2*P*r**2*sin(theta)**2)   )   )
e = EFE(G, T)
e.nonzero()
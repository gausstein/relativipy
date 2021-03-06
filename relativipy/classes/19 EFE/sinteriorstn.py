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

g=Metric(   (  (-B(r),0,0,0), (0, A(r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho, 0,0,0), (0,P,0,0), (0,0,P,0), (0,0,0,P)   )   )
e = EFE(G, T)

print 'Initial metric:'
pprint(g.matrix())
#C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
print '-'*40
#pprint(G.matrix())

print '-'*40
#G.matrixelement(1,1)
pprint(T.matrix())
pprint(e.equation())
#e.nonzero()
print '-'*40

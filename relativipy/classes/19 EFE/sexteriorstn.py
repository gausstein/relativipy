# -*- coding: utf-8 -*-
from relativipy import *

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

A= Function('A')
B= Function('B')

g=Metric(   (  (-B(r),0,0,0), (0, A(r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)

print 'Initial metric:'
g.ppmatrix()
#C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
#G.matrix()
G.matrixelement(1,1)
print '-'*40
#Solving EFE for A and B
s = ( Ric.dd(1,1)/ A(r) ) + ( Ric.dd(0,0)/ B(r) )
p = dsolve(s, A(r))
pprint(p)
newmetric = g.matrix().subs(A(r), p)
print "New metric:"
pprint(newmetric)
r22 = Ric.dd(3,3).subs( A(r), 1/B(r))
h = dsolve( r22, B(r) )
pprint(h)

M= Symbol('M')

g=Metric(   (  ( ( 2*M/r - 1 ),0,0,0), (0, 1/(1- 2*M/r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
tau = Symbol('tau')

C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
geo = Geodesic(tau, C)

#g.ppmatrix()
#C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing()
#G.matrix()
#geo.printing()

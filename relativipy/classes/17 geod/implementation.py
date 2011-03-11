# -*- coding: utf-8 -*-
from relativipy import *



t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

A= Function('A')
B= Function('B')
tau = Symbol('tau')

g=Metric(   (  (-B(r),0,0,0), (0, A(r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci(Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
#T = EM(  )
geo = Geodesic(tau,C)

print 'Initial metric:'
pprint(g.matrix())
C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
#G.nonzero()
geo.printing()

print '-'*40
#Solving EFE for A and B
s = ( Ric.dd(1,1)/ A(r) ) + ( Ric.dd(0,0)/ B(r) )
#pprint (s)
p = dsolve(s, A(r))
pprint(p)
newmetric = g.matrix().subs(A(r), p)
print "New metric:"
pprint(newmetric)
r22 = Ric.dd(3,3).subs( A(r), 1/B(r))
h = dsolve( r22, B(r) )
pprint(h)


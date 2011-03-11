# -*- coding: utf-8 -*-
from relativipy import *

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Function('rho')(r)
P = Function('P')(r)
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
T = EM( (  (rho*B(r), 0,0,0), (0,P*A(r),0,0), (0,0,P*r**2,0), (0,0,0,P*r**2*sin(theta)**2)   )   )
e = EFE(G, T)

print 'Initial metric:'
pprint(g.matrix())
#C.nonzero()
#Ric.nonzero()
#Rie.nonzero()
#Rs.printing()
#pprint(G.matrix())
#pprint(T.matrix())
#pprint(e.matrix())
e.nonzero()
#e.nonzeroother()
print '-'*40
#a=simplify(e.matrix()[0,0]/(B(r)))
#pprint(a)
#pprint(dsolve(a, A(r)))


# -*- coding: utf-8 -*-
from relativipy import *
from Coord import *


x = Coord('t', 'r', 'theta', 'phi')

r= x.coord()[1]
theta = x.coord()[2]

rho = Function('rho')(r)
P = Function('P')(r)
tau = Symbol('tau')


A= Function('A')
B= Function('B')

g=Metric(   (  (-B(r),0,0,0), (0, A(r), 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho, 0,0,0), (0,P,0,0), (0,0,P,0), (0,0,0,P)   )   )
e = EFE(G, T)




print 'Initial metric:'
pprint(g.matrix())
pprint( diff(rho, r))
x.printing()

C.nonzero()
Ric.nonzero()
#Rie.nonzero()
#Rs.printing() 
print '-'*40
#pprint(G.matrix())

print '-'*40
#G.matrixelement(1,1)
#pprint(T.matrix())
#pprint(e.matrix())
#e.nonzero()



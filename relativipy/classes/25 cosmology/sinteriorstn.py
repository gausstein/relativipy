# -*- coding: utf-8 -*-
from relativipy import *

t=Symbol('t')
r=Symbol('r')
theta=Symbol('theta')
phi=Symbol('phi')

rho = Function('rho')(r)
P = Function('P')(r)
tau = Symbol('tau')


A= Function('A')(r)
B= Function('B')(r)

g=Metric(   (  (-B,0,0,0), (0, A, 0, 0), (0, 0, r**2, 0), (0, 0, 0, r**2*sin(theta)**2)   )  )
x=(t,r,theta,phi)
C=Christoffel(g,x)
Rie = Riemann(C)
Ric=Ricci( Rie)
Rs =Rscalar(Ric)
G = Einstein(Rs)
T = EM( (  (rho*B, 0,0,0), (0,P*A,0,0), (0,0,P*r**2,0), (0,0,0,P*r**2*sin(theta)**2)   )   )
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
#a= simplify(Ric.matrix()[0,0]/(2*B) + Ric.matrix()[1,1]/(2*A) + Ric.matrix()[2,2]/r**2 + 8*pi*rho)
#pprint(a)
#pprint( dsolve(a, A))

'''
rho = Symbol('rho')
m = 4*pi*integrate(rho*r**2, r)
pprint(m)
P = Function('P')(r)
hequil= diff(P, r) + (P+rho)*((m + 4*pi*r**3*P)/(r**2 - 2*m))
P = dsolve(hequil,P)
pprint(simplify(P))
'''
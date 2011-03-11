from scipy import *
from scipy.integrate import *

#definitions
def B(r):
	MG=1.475
	return (1.0 - (2.0*MG)/r)
def Bi(r):
	return 1.0/B(r)
ra= 6.98E7#Km
rp=4.6E7#Km
MG=1.475#Km
K1= (ra*rp)**2
K= K1*(Bi(ra)-Bi(rp))
a= rp**2-ra**2
b= (ra**2)*Bi(ra) - (rp**2)*Bi(rp)
c = a+b
L= 2.0*ra*rp/(ra+rp)
print'--------------------------'
def phi(r):
	return 1.0/ sqrt( (a*r**4 + b*(r**4)*B(r))/K - (r**2)*B(r))
i = fixed_quad(phi, rp, ra)
print i
deltaphi= 2.0*abs(i[0])- 2.0*pi
print deltaphi*206265.0

print'--------------------------'
def phi2(r):
	return sqrt( K/ ( c*r**4 -2.0*b*MG*r**3 -K*r**2 + 2.0*K*MG*r))
i = fixed_quad(phi2, rp, ra)
print i
deltaphi= 2.0*abs(i[0])- 2.0*pi
print deltaphi*206265.0

print'--------------------------'
def phi3(r):
	return 1.0/ sqrt( (c*r**4 -2.0*b*MG*r**3)/K -r**2 + 2.0*MG*r)
i= fixed_quad(phi3, rp, ra)
print i
deltaphi= 2.0*abs(i[0])- 2.0*pi
print deltaphi*206265.0

print '------------------------'
exacti=(1.0 + (3.0*MG/L))*pi
print 'exacti', exacti
exactdelta= 2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi
print exactdelta
print exactdelta*206265




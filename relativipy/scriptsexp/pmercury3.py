from scipy import *
from scipy.integrate import *

#definitions
def B(r):
	MG=1.475
	return (1.0 - (2.0*MG)/r)
def A(r):
	return 1.0/B(r)
ra= 6.98E7#Km
rp=4.6E7#Km
MG=1.475#Km

K1= (ra*rp)**2
K= K1*(A(ra)-A(rp))

E = (ra**2*B(rp) - rp**2*B(ra))/K
print 'Potential Energy', E
J = ( ( B(rp) - B(ra) ) * ra**2*rp**2)/K
print 'Angular momentum', J

a= (1.0-E)
b= (2.0*MG*E)
c= -J**2
d= 2.0*MG*J**2

coeff= [a,b,c,d,0.0]
z = roots(coeff)
print 'Roots of the denominator', z

L= 2.0*ra*rp/(ra+rp)

print'--------------------------'
def phi1(r):
	return abs(J)*sqrt( 1.0 / ( a*r**4 + b*r**3 + c*r**2 + d*r) )
i = quad(phi1, rp, ra)
print i
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi
arcsec = deltaphi*206265.0
print arcsec*415,'revolutions per century'

print'--------------------------'
'''
def phi2(r):
	return sqrt( 1.0/ ( a*r**4 + b*r**3 + c*r**2 + d*r))
i = fixed_quad(phi2, rp, ra, n=10)
print i
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi
arcsec = deltaphi*206265.0
print arcsec*415,'revolutions per century'
'''
print '------------------------'
print 'Value of the integral calculated in the book of Weinberg'
iw=(1.0 + (3.0*MG/L))*pi
print iw
print 'delta phi'
wdelta= 2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi
print wdelta
print (2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi)*206265
arcsec = wdelta*206265.0
print arcsec*415,'revolutions per century'




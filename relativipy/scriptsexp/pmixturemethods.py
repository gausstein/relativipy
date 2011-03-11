from scipy import *
from scipy.integrate import *

#definitions
def B(r):
	MG=1.475
	return (1.0 - 2.0*MG/r)

ra= 6.98E7#Km
rp=4.6E7#Km
MG=1.475#Km
K =  ( ra**2 - rp**2 )* B(ra)*B(rp) 
E = (ra**2*B(rp) - rp**2*B(ra))/K
print E
J = ( ( B(rp) - B(ra) ) * ra**2*rp**2)/K
print J
a= (1.0-E)/J
print a
b= (2.0*MG*E)/J**2
print b


L= 2.0*ra*rp/(ra+rp)
print'--------------------------'

def phi(r):
	return 1.0/ sqrt( r**4/J - E*r**4*B(r)/J - r**2*B(r) )
i = quad(phi, rp, ra)
print i
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi
arcsec = deltaphi*206265.0
print arcsec*415,'revolutions per century'
print '-------------------------------------'

def phi2(r):
	return 1.0/ sqrt( a*r**4 + b*r**3 - r**2 + 2.0*MG*r )
i = quad(phi2, rp, ra)
print i
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi
arcsec = deltaphi*206265.0
print arcsec*415,'revolutions per century'

print '------------------------'
exacti=(1.0 + (3.0*MG/L))*pi
print 'exacti', exacti
exactdelta= 2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi
print exactdelta
print (2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi)*206265
arcsec = exactdelta*206265.0
print arcsec*415,'revolutions per century'




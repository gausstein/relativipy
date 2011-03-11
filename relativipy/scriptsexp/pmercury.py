from scipy import *
from scipy.integrate import *

print 'Precession of Mercury'
print '*'*40
print ''

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
print 'K',K

E = (ra**2*B(rp) - rp**2*B(ra))/K
print 'Potential Energy', E
J = ( ( B(rp) - B(ra) ) * ra**2*rp**2)/K
print 'Angular momentum', J

a= rp**2-ra**2
b= (ra**2)*A(ra) - (rp**2)*A(rp)
c = a+b
L= 2.0*ra*rp/(ra+rp)
print'---------------------------------------------------'
'''
def phi(r):
	return 1.0/ sqrt( (a*r**4 + b*(r**4)*B(r))/K - (r**2)*B(r))
i = quad(phi, rp, ra)
print i
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi*206265.0
'''
#---------------------------------------------------------------------
def phi2(r):
	return sqrt( K/ ( c*r**4 -2.0*b*MG*r**3 -K*r**2 + 2.0*K*MG*r))
i = quad(phi2, rp, ra)
print 'Value of the integral calculated in Python'
print i
print 'delta phi'
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi, 'rad per revolutions'
arcsec = deltaphi*206265.0#from rad/rev to arsec/rev 
print 'Precession of Mercury'
print arcsec*415,'arseconds per century'# from arsec/rev to arsec/cent

print'---------------------------------------------------'
def phi3(r):
	return 1.0/ sqrt( (c*r**4 -2.0*b*MG*r**3)/K -r**2 + 2.0*MG*r)
i= quad(phi3, rp, ra)
print 'Value of the integral calculated in Python'
print i
print 'delta phi'
deltaphi= 2.0*(abs(i[0])- pi)
print deltaphi, 'rad per revolutions'
arcsec = deltaphi*206265.0#from rad/rev to arsec/rev 
print 'Precession of Mercury'
print arcsec*415,'arseconds per century'# from arsec/rev to arsec/cent

print'---------------------------------------------------'
print 'Value of the integral calculated in the book of Weinberg'
iw=(1.0 + (3.0*MG/L))*pi
print iw
print 'delta phi'
wdelta= 2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi
print wdelta
#print (2.0*((1.0 + (3.0*MG/L))*pi)-2.0*pi)*206265
arcsec = wdelta*206265.0
print 'Precession of Mercury'
print arcsec*415,'arseconds per century'
print '---------------------------------------------------'
print 'Observed value of the precession of Mercury (42.66, 43.56) '






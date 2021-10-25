import numpy
from astropy.io import fits

# observatory location: latitude (deg), altitude (km)
lat = -24.6
alt = 2.6
# pressure
pmin = 735
pmax = 750
npres = 5
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = 0
tmax = 20
ntemp = 9
temp = numpy.linspace(tmin,tmax,ntemp)
# humidity
hmin = 5
hmax = 90
nhum = 11
humid = numpy.linspace(hmin,hmax,nhum)
# airmass
amin = 1.0
amax = 2.5
nam = 61
airm = numpy.linspace(amin,amax,nam)
# wavelength range/resolution
wmin = 490
wmax = 1100
R = 20000


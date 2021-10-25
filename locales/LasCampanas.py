import numpy
from astropy.io import fits

# observatory location: latitude (deg), altitude (km)
lat = -29.0
alt = 2.4
# pressure
pmin = 700
pmax = 800
npres = 7
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = -10
tmax = 25
ntemp = 9
temp = numpy.linspace(tmin,tmax,ntemp)
# humidity
hmin = 5
hmax = 90
nhum = 11
humid = numpy.linspace(hmin,hmax,nhum)
# airmass
amin = 1.0
amax = 2.0
nam = 41
airm = numpy.linspace(amin,amax,nam)
# wavelength range/resolution
wmin = 550
wmax = 2550
R = 10000


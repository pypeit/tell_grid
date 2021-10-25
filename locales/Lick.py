import numpy
from astropy.io import fits

# observatory location: latitude (deg), altitude (km)
lat = 37.3
alt = 1.3
# pressure
pmin = 850
pmax = 900
npres = 7
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = -10
tmax = 30
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
wmin = 300
wmax = 1100
R = 10000


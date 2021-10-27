import numpy

# observatory location: latitude (deg), altitude (km)
lat = 19.8
alt = 4.2
# pressure
pmin = 600
pmax = 630
npres = 7
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = -10
tmax = 10
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


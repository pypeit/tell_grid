import numpy

# observatory location: latitude (deg), altitude (km)
lat = 33.4
alt = 1.7
# pressure
pmin = 800
pmax = 850
npres = 7
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = 5
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
wmin = 900
wmax = 2500
R = 10000


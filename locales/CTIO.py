import numpy

# observatory location: latitude (deg), altitude (km)
lat = -30.6
alt = 2.2
# pressure
pmin = 765
pmax = 795
npres = 7
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = 0
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
wmax = 1050
R = 15000


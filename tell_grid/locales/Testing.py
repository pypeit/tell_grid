import numpy

# observatory location: latitude (deg), altitude (km)
lat = 19.8
alt = 4.2
# pressure
pmin = 600
pmax = 630
npres = 2
press = numpy.linspace(pmin,pmax,npres)
# temperature
tmin = 0
tmax = 15
ntemp = 2
temp = numpy.linspace(tmin,tmax,ntemp)
# humidity
hmin = 5
hmax = 90
nhum = 2
humid = numpy.linspace(hmin,hmax,nhum)
# airmass
amin = 1.0
amax = 2.0
nam = 2
airm = numpy.linspace(amin,amax,nam)
# wavelength range/resolution
wmin = 675
wmax = 750
R = 20000


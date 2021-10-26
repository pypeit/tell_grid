import numpy as np
import sys
import os

# Grid parameters loaded in from observatory grid file
obs = sys.argv[1] # observatory name recognized by TelFit
exec("from tell_grid.locales import %s" % obs)
# pressure
exec("pmin = %s.pmin" % obs)
exec("pmax = %s.pmax" % obs)
exec("npres = %s.npres" % obs)
press = np.linspace(pmin,pmax,npres)
# temperature
exec("tmin = %s.tmin" % obs)
exec("tmax = %s.tmax" % obs)
exec("ntemp = %s.ntemp" % obs)
temp = np.linspace(tmin,tmax,ntemp)
# humidity
exec("hmin = %s.hmin" % obs)
exec("hmax = %s.hmax" % obs)
exec("nhum = %s.nhum" % obs)
humid = np.linspace(hmin,hmax,nhum)
# airmass
exec("amin = %s.amin" % obs)
exec("amax = %s.amax" % obs)
exec("nam = %s.nam" % obs)
airm = np.linspace(amin,amax,nam)
# wavelength range/resolution
exec("wmin = %s.wmin" % obs)
exec("wmax = %s.wmax" % obs)
exec("R = %s.R" % obs)

for p in press:
    for t in temp:
        for h in humid:
            for a in airm:
                print("python make_tel_model.py {:.1f} {:.1f} {:.1f} {:.1f} {:.1f} {:.3f} {:.0f} {:s}".format(wmin,wmax,p,t,h,a,R,obs))



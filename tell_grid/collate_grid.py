import numpy as np
import sys
from astropy.io import fits

# Telluric grid parameters
# This could be done *a lot* more elegantly...
obs = sys.argv[1] # observatory/location name recognized by TelFit
exec("from tell_grid.locales import %s as %s" % (obs,obs))
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

# directory with output files
dir = 'output_grids/{:s}/'.format(obs)

# grab the wavelength grid from the first model in the grid
fn0 = dir+'TellModel_{:s}_{:.0f}_{:.0f}_P{:.0f}_T{:.0f}_H{:.0f}_AM{:.3f}_R{:.0f}.fits'.format(
      obs,wmin,wmax,press[0],temp[0],humid[0],airm[0],R)
wave_grid = fits.open(fn0)[1].data
# initialize the full telluric grid
tell_grid = np.zeros((npres,ntemp,nhum,nam,len(wave_grid)))

# Now read in all of the model files
# in a beautiful nested loop
for ip in range(npres):
    for it in range(ntemp):
        for ih in range(nhum):
            for ia in range(nam):
                fn = dir+'TellModel_{:s}_{:.0f}_{:.0f}_P{:.0f}_T{:.0f}_H{:.0f}_AM{:.3f}_R{:.0f}.fits'.format(
                      obs,wmin,wmax,press[ip],temp[it],humid[ih],airm[ia],R)
                tell_grid[ip,it,ih,ia] = fits.open(fn)[0].data

# output filename
outfile = 'TellGrid_{:s}_{:.0f}_{:.0f}_R{:.0f}.fits'.format(obs,10*wmin,10*wmax,R)

# prepare fits hdus
hdu = fits.PrimaryHDU(tell_grid)
hdu2 = fits.ImageHDU(wave_grid)

# add some header information
hdu.header['WAVEMIN']=wmin
hdu.header['WAVEMAX']=wmax
hdu.header['NPRES']=npres
hdu.header['PRES0']=press[0]
hdu.header['DPRES']=press[1]-press[0]
hdu.header['NTEMP']=ntemp
hdu.header['TEMP0']=temp[0]
hdu.header['DTEMP']=temp[1]-temp[0]
hdu.header['NHUM']=nhum
hdu.header['HUM0']=humid[0]
hdu.header['DHUM']=humid[1]-humid[0]
hdu.header['NAM']=nam
hdu.header['AM0']=airm[0]
hdu.header['DAM']=airm[1]-airm[0]
hdu.header['R']=R
hdu.header['OBS']=obs

# write hdus to output fits file
hdul = fits.HDUList([hdu,hdu2])
hdul.writeto(outfile,overwrite=True)


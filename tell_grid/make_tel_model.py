import numpy as np
from telfit import TelluricFitter, DataStructures
from scipy.interpolate import interp1d
from scipy.ndimage import convolve1d
from astropy.io import fits
import astropy.units as u
import sys
import os

# Get telluric model from TelFit
def generate_telluric(lat=-24.6, alt=2.4, # observatory latitude and longitude (default = Paranal)
                      wavestart=1000.0,waveend=2500.0, # limits of wavelength grid in nm
                      pressure=740.0, # pressure in mbar
                      temperature=0.0, # temperature  in Celsius
                      humidity=50.0, # percent humidity
                      airmass=1.5): # airmass

    # prepare TelFit object
    fitter = TelluricFitter()
    
    # Set observatory from latitude and altitude
    fitter.SetObservatory({"latitude": lat, "altitude": alt})
    
    # Prepare TelFit parameters
    fitter.AdjustValue({"angle": np.arccos(1.0/airmass)*180.0/np.pi, # angle from zenith in degrees
                       "pressure": pressure, # pressure in mbar
                       "temperature": temperature+273.15, # temperature in Kelvin
                       "h2o": humidity, # percent humidity
                       "wavestart": wavestart - 20.0, # minimum wavelength in nm
                       "waveend": waveend + 20.0, # maximum wavelength in nm
                       "co2": 400.0, # CO2 content in ppm (default is year 2000 level; should possibly be upped to 410 for 2020+...)
                       }) # In principle, many other molecular abundances can be specified. See TelFit documentation for details.
                       
    fitter.air_wave = False # we want to use vacuum wavelengths
    fitter.xunits = u.nm # standard TelFit units
    tm = fitter.GenerateModel([],nofit=True) # now compute the transmission model

    return tm.x, tm.y # wave grid, transmission grid

def convolve_model(wave_in, # high-resolution telluric wavelengths
                   model_in, # high-resolution telluric model
                   wave_out, # low-resolution wavelengths for output model
                   wavestart=1000.0,waveend=2500.0, # limits of wavelength grid in nm
                   R=25000): # spectral resolution

    # Prepare an evenly sampled (high-resolution) wavelength grid
    num = len(wave_in)
    dloglam = np.log((waveend+15)/(wavestart-15))/num
    new_wave = np.exp(np.arange(np.log(wavestart-15.0),np.log(waveend+15),dloglam))

    # Interpolate the old model onto the new high-res grid
    interp_model = interp1d(wave_in,model_in)
    hires_model = interp_model(new_wave)
    
    # Create boxcar filter for downsampling
    num2 = int(np.median(np.log(wave_out[1:])-np.log(wave_out[:-1]))/dloglam)
    w = (1.0/num2)*np.ones(num2)
    
    # Downsample the model by convolving and resampling
    conv_model = convolve1d(hires_model,w)
    interp_conv_model = interp1d(new_wave,conv_model)
    model_out = interp_conv_model(wave_out)

    return wave_out, model_out

# Write telluric model to fits file
def save_telluric_model(wave_out,
                       model_out,
                       wavestart, waveend,
                       pressure,
                       temperature,
                       humidity,
                       airmass,
                       observatory,
                       filename='tellmodel.fits'):

    # Prepare fits hdus
    hdu = fits.PrimaryHDU(model_out)
    hdu2 = fits.ImageHDU(wave_out)
    
    # Header information for telluric model
    hdu.header['WAVEMIN']=wavestart
    hdu.header['WAVEMAX']=waveend
    hdu.header['PRESSURE']=pressure
    hdu.header['TEMP']=temperature
    hdu.header['HUMID']=humidity
    hdu.header['AIRMASS']=airmass
    hdu.header['RES']=R
    hdu.header['OBS']=observatory

    # Write out hdu list to fits file
    hdul = fits.HDUList([hdu,hdu2])
    hdul.writeto(filename,overwrite=True)

if __name__== "__main__":
    
    # COMMAND LINE ARGUMENTS
    wavestart = float(sys.argv[1])
    waveend = float(sys.argv[2])
    pressure = float(sys.argv[3])
    temperature = float(sys.argv[4])
    humidity = float(sys.argv[5])
    airmass = float(sys.argv[6])
    R = float(sys.argv[7])
    observatory = sys.argv[8]
    
    fn='output_grids/{:s}/TellModel_{:s}_{:.0f}_{:.0f}_P{:.0f}_T{:.0f}_H{:.0f}_AM{:.3f}_R{:.0f}.fits'.format(observatory,observatory,
                                                                                                      wavestart,waveend,
                                                                                                 pressure,temperature,humidity,
                                                                                                 airmass,R)
    
    # Get observatory information
    exec("import tell_grid.locales.%s as %s" % (obs,obs))
    exec("lat = %s.pmin" % obs)
    exec("alt = %s.pmax" % obs)
    
    dloglam = np.log(1+1/(R*2.5)) # 2.5 pixels per FWHM in the output file, sufficient to avoid aliasing as per Nyquist sampling
    wave_out = np.exp(np.arange(np.log(wavestart-10),np.log(waveend+10),dloglam)) # prepare output wavelength grid
    
    wave_hr, model_hr = generate_telluric(lat,alt,wavestart,waveend,pressure,temperature,humidity,airmass) # create telluric model
    model_out = convolve_model(wave_hr,model_hr,wave_out,wavestart,waveend,R) # convolve model and deposit onto output wavelength grid
    
    # print model to file
    os.system("mkdir output_grids/{:s}".format(observatory))
    save_telluric_model(wave_out, model_out, wavestart, waveend, pressure, temperature, humidity, airmass, observatory,
                       filename=fn)



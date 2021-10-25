import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from tell_grid.make_tel_model import generate_telluric, convolve_model
import locales.Lick as obs

# Boundaries of wavelength grid in nm
wv_min = 550.0
wv_max = 1050.0

# Parameters of telluric model
pres = 0.5*(obs.pmin+obs.pmax)
temp = 0.5*(obs.tmin+obs.tmax)
hum = 30.0
airm = 2.0

# Create high-resolution (hr) transmission curve
wave_hr, tell_hr = generate_telluric(obs.lat, obs.alt,
                                     wavestart = wv_min, waveend=wv_max,
                                     pressure=pres,
                                     temperature=temp,
                                     humidity=hum,
                                     airmass=airm)

# Now let's convolve it down to the resolution of a typical spectrum,
# say R = 2000
R = 2000

# To do this, we need to define the low-resolution (lr) output wavelength grid.
# I generally work with constant velocity spacing; you could also use constant dlambda
dloglam = np.log(1+1/(R*2.5))
wave_lr = np.exp(np.arange(np.log(wv_min),np.log(wv_max),dloglam))

# Bin down and resample telluric model
wave_lr, tell_lr = convolve_model(wave_hr,tell_hr,wave_lr,wv_min,wv_max,R)

# Note that convolve_model *does not* include Gaussian smoothing!
# Let's now additionally smooth by a Gaussian corresponding to R = 2000.
sig = 2.5/(2*np.sqrt(2*np.log(2)))
tell_lr_smo = gaussian_filter(tell_lr,sig)

# Now let's plot it up to take a look
fig, ax = plt.subplots(1,1,figsize=(7,4))
plt.plot(wave_hr,tell_hr,c='royalblue',lw=0.1,label='High-res model')
plt.plot(wave_lr,tell_lr_smo,c='firebrick',lw=1.5,drawstyle='steps-mid',label='Low-res model')
plt.xlim(680,1000)
plt.ylim(0,1.05)
plt.xlabel('Wavelength [nm]',fontsize=15)
plt.ylabel('Transmission',fontsize=15)
plt.tick_params(which='both',direction='in',right=True,top=True,labelsize=13)
plt.tight_layout()
plt.show()


                               

import matplotlib.pyplot as plt
from astropy.io import fits

grid = fits.open('TellGrid_Testing_6750_7500_R20000.fits')
wave = grid[1].data
tell = grid[0].data

fig, ax = plt.subplots(1,1,figsize=(7,4))
plt.plot(wave,tell[1,1,1,1],c='firebrick',lw=1.0,drawstyle='steps-mid',alpha=0.7)
plt.plot(wave,tell[0,0,0,0],c='royalblue',lw=1.0,drawstyle='steps-mid',alpha=0.7)
plt.xlim(680,740)
plt.ylim(0,1.05)
plt.xlabel('Wavelength [nm]',fontsize=15)
plt.ylabel('Transmission',fontsize=15)
plt.tick_params(which='both',direction='in',right=True,top=True,labelsize=13)
plt.tight_layout()
plt.show()


from astropy.io import fits

data, hd = fits.getdata('combined_all_b5_c18o_21_noise_weighted.fits', header=True)
hd['BUNIT']=('K', 'Ta*')
fits.writeto('B5_C18O_21.fits', data, hd, clobber=True)

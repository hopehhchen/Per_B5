import numpy as np
import yt
from astropy.io import fits

data0 = fits.open('combined_all_b5_c18o_21_noise_weighted.fits')[0].data
##to make the final obj file small enough to be uploaded to sketchfab
#data0 = data0[160:210, 6:63, 66:136]
data = dict(Density = data0)

ds = yt.load_uniform_grid(data, data0.shape)
dd = ds.all_data()

sf = ds.surface(dd, 'Density', 1.5)
sf.export_obj('test', transparency = .6)

print len(sf.vertices[sf.vertices == sf.vertices])

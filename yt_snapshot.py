##Modified from Tom Robitaille's script to make a 3D movie, using yt
##(https://gist.github.com/astrofrog/9685403)
import numpy as np
import yt
from yt.mods import ColorTransferFunction, write_bitmap


# Read in the data to yt
pf = yt.load('reproj_b5_c18o_21_noise_weighted.fits', auxiliary_files = ['reproj_b5_11_clean_vlsrm.fits'])


# Instantiate the ColorTransferfunction.
min_c18o, max_c18o = .01, 4.
tf_c18o = ColorTransferFunction((min_c18o, max_c18o))
min_11, max_11 = .03, 2.5
tf_11 = ColorTransferFunction((min_11, max_11))


# Set up the camera parameters: center, looking direction, width, resolution
#c = (pf.domain_right_edge + pf.domain_left_edge) / 2.0 #This results in the camera focusing at the edge of the cube
c = np.array([23., 42., 712.])
L = np.array([0.0, 0.0, -1.0])
W = 120
N = 1024


# Create camera objects
cam_c18o= pf.h.camera(c, L, W, N, tf_c18o,
                       fields=['temperature'], log_fields=[False],
                       no_ghost=True, north_vector = [0., 1., 0.])
cam_11 = pf.h.camera(c, L, W, N, tf_11,
                       fields=['temprature_1'], log_fields=[False],
                       no_ghost=True, north_vector = [0., 1., 0.])


# Set up layers
tf_c18o.add_layers(10, 0.003, colormap='RdBu_r')  #was 10, .0001
tf_11.add_layers(18, .003, colormap = 'Reds')


# Produce snapshot
N = 36*4

images_c18o = []
for i, snapshot in enumerate(cam_c18o.rotation(2*np.pi, N, clip_ratio = 8.0, rot_vector = [0., 1., 0.])):
	images_c18o.append(cam_c18o.snapshot())

images_11 = []
for i, snapshot in enumerate(cam_11.rotation(2*np.pi, N, clip_ratio = 8.0, rot_vecotr = [0., 1., 0.])):
	images_11.append(cam_11.snapshot())

for i in range(N):
	image_total = images_c18o[i]*3. + images_11[i]*1.5
	image_total.write_png('c18o_ammonia11_{0:03d}.png'.format(i+1))


#Write bitmap  ##ERROR##
write_bitmap(im_c18o, 'test_c18o_bitmap.png', transpose = True)

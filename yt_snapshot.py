##Modified from Tom Robitaille's script to make a 3D movie, using yt
##(https://gist.github.com/astrofrog/9685403)
import numpy as np
import yt
from yt.mods import ColorTransferFunction, write_bitmap


# Read in the data to yt
pf = yt.load('reproj_b5_c18o_21_noise_weighted.fits')


# Instantiate the ColorTransferfunction.
min_c18o, max_c18o = .01, 4.
tf_c18o = ColorTransferFunction((min_c18o, max_c18o))


# Set up the camera parameters: center, looking direction, width, resolution
#c = (pf.domain_right_edge + pf.domain_left_edge) / 2.0 #This results in the camera focusing at the edge of the cube
c = np.array([23., 42., 712.])
L = np.array([1.0, 1.0, 1.0])
W = 120
N = 1024


# Create camera objects
cam_c18o= pf.h.camera(c, L, W, N, tf_c18o,
                       fields=['temperature'], log_fields=[False],
                       no_ghost=True)


# Set up layers
tf_c18o.add_layers(12, 0.005, colormap='RdBu_r')  #was 10, .0001


# Produce snapshot
#im_c18o = cam_c18o.snapshot('ytcube_c18o.png')
im_c18o = cam_c18o.snapshot()


#Write bitmap  ##ERROR##
write_bitmap(im_c18o, 'test_c18o_bitmap.png', transpose = True)
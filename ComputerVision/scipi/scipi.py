from PIL import Image
from numpy import *
from scipy.ndimage import filters
import os
from pylab import *

im = array(Image.open("../data/empire.jpg"))
#gaussian filter with a standard deviation of 5
#im2 = filters.gaussian_filter(im, 5)

#imshow(im)
#show()

im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i], 5)
im2 = uint8(im2)

imshow(im2)
show()


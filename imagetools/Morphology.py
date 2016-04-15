#Usually done with binary images, converting every pixel to 0 or 1 using thresholding
#https://en.wikipedia.org/wiki/Mathematical_morphology

from scipy.ndimage import measurements, morphology
from numpy import *
from PIL import Image
from scipy import misc
from pylab import *

#load image and threshold to make sure it's binary
im = array(Image.open('../data/houses.png').convert('L'))
im = 1*(im<128)

labels, numberOfObjects = measurements.label(im)
print("Number of Objects:", numberOfObjects)

#morphology - opening to separate objects better
#Second argument is the number of neighbors to use when centering around a pixel
#9,5 will be 4 above and below and 2 left and rights
im_open = morphology.binary_opening(im, ones((9,5)), iterations=3)

labels_open, numberOfObjects_open = measurements.label(im_open)
print("Number of objects:", numberOfObjects_open)

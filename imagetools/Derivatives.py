from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *


im = array(Image.open('../data/Empire.jpg').convert('L'))
imshow(im, cmap=matplotlib.cm.Greys_r)
show()


#Sobel derivative filters
imx = zeros(im.shape)
#Sobel filter, second param selects the x or y derivative
filters.sobel(im, 1, imx)
imshow(imx)
show()

imy = zeros(im.shape)
filters.sobel(im,0,imy)
imshow(imy)
show()

magnitude = sqrt(imx**2+imy**2)
imshow(magnitude)
show()


sigma = 5
imx = zeros(im.shape)
filters.gaussian_filter(im, (sigma, sigma), (0,1), imx)
imshow(imx)
show()

imy = zeros(im.shape)
#Third argument is which order of derivatives to use in each direction using the sd determined by the second arg
filters.gaussian_filter(im, (sigma, sigma), (1, 0), imy)
imshow(imy)
show()



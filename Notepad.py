from PIL import Image
from numpy import *
from imagetools import Histogram
import os
from pylab import *

image = array(Image.open('data/AquaTermi_lowcontrast.jpg').convert('L'))
image2, cdf = Histogram.histogramEqualization(image)

print(cdf)
imshow(image2)
show()

pil_im = Image.open('data/empire.jpg').convert('L')
im = array(pil_im)
#imshow(im)
#show()

print(im.shape, im.dtype)

pil_im2 = Image.open('data/empire.jpg').convert('L')
im2 = array(pil_im2, 'f')
print(im2.shape, im2.dtype)

inverted_im = 255 - im
print(inverted_im.min(), inverted_im.max())

clamped_im = (100.0/255) * im + 100 #image is clamped between 100-200
print(clamped_im.min(), clamped_im.max())


quadratic_im = 255.0 * (im/255)**2 #squared
print(quadratic_im.min(), quadratic_im.max())


pil_im = Image.fromarray(uint8(im))

#imshow(im)
#print 'Please click three points'
#x=ginput(3)
#print 'you clicked', x
#show()


#x = [100, 100, 400, 400]
#y = [200, 500, 200, 500]
#plot(x, y, 'ks:')
#plot(x[:2],y[:2])

#figure()
#gray()
#contour(im, origin='image')
#axis('equal')
#title('Plotting: "empire.jpg"')
#axis('off')


#figure()
#hist(im.flatten(),128)
#show()
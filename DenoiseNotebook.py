from scipy.ndimage import filters
from imagetools.Denoise import *

#create synthetic image with noise
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300, 200:300] = 255
im = im + 30*random.standard_normal((500,500))

U,T = denoise(im, im)
G = filters.gaussian_filter(im, 10)

#save the result
from scipy.misc import imsave
imsave('synth_rof.pdf', U)
imsave('synth_gaussian.pdf', G)


from PIL import Image
from pylab import *

im = array(Image.open('data/Empire.jpg').convert('L'))
U, T = denoise(im, im)

figure()
gray()
imshow(U)
axis('equal')
axis('off')
show()
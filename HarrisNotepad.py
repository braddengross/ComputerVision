from PIL import Image
from numpy import array
from localimagedescriptors import harris
from pylab import gray, figure, show
from imagetools import Resize


"""im = array(Image.open('data/Empire.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim, 6, 0.1)
harris.plot_harris_points(im, filtered_coords)"""

im1 = array(Image.open("data/crans_1_small.jpg").convert("L"))
im2 = array(Image.open("data/crans_2_small.jpg").convert("L"))

# resize to make matching faster
im1 = Resize.imageResize(im1,(int(im1.shape[1]/2),int(im1.shape[0]/2)))
im2 = Resize.imageResize(im2,(int(im2.shape[1]/2),int(im2.shape[0]/2)))


wid = 5
harrisim = harris.compute_harris_response(im1, 5)
filtered_coords1 = harris.get_harris_points(harrisim, wid+1)
d1 = harris.get_descriptors(im1, filtered_coords1, wid)

harrisim = harris.compute_harris_response(im2, 5)
filtered_coords2 = harris.get_harris_points(harrisim, wid+1)
d2 = harris.get_descriptors(im2, filtered_coords2, wid)

print("start matching")
matches = harris.match_twosided(d1, d2)

figure()
gray()
harris.plot_matches(im1, im2, filtered_coords1, filtered_coords2, matches)
show()
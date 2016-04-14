from numpy import *

def histogramEqualization(image, numberOfBins = 256):
    imageHistogram, bins = histogram(image.flatten(), numberOfBins, normed=True)
    cdf = imageHistogram.cumsum()
    cdf = 255 * cdf / cdf[-1]

    im2 = interp(image.flatten(), bins[:-1], cdf)

    return im2.reshape(image.shape), cdf
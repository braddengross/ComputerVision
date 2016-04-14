from numpy import *

def imageResize(image, size):
    pil_im = Image.fromarray(uint8(image))
    return array(pil_im.resize(size))

from numpy import *
from PIL import Image

def imageResize(image, size):
    pil_im = Image.fromarray(uint8(image))
    return array(pil_im.resize(size))

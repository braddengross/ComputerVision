from numpy import *
from PIL import Image

def computeAverage(imageList):
    averageImage = array(Image.open(imageList[0]), 'f')

    for imageName in imageList[1:]:
        try:
            averageImage += array(Image.open(imageName))
        except:
            print imageName + '... skipped'
    averageImage /= len(imageList)

    return array(averageImage, 'uint8')






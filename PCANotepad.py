from PIL import Image
from numpy import *
from pylab import *
from pca import PCA
import glob
import pickle

imlist = glob.glob("data/a_thumbs/*.jpg")
#print imlist
im = array(Image.open(imlist[0]))
#imshow(im)
#show()

m, n = im.shape[0:2]
imageCount = len(imlist)

#create matrix to stor all flattened images
imageMatrix = array([array(Image.open(im)).flatten()
                     for im in imlist], 'f')

#perform pca
V, S, immean = PCA.pca(imageMatrix)

#show some images (mean and 7 first modes
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    #convert images back to one dimension
    imshow(V[i].reshape(m,n))
    #imshow(imageMatrix[i].reshape(m,n))

#show()

f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean, f)
pickle.dump(V, f)
f.close()
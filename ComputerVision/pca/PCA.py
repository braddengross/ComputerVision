from PIL import Image
from pylab import *
from numpy import *
import os

def pca(trainingMatrix):


    #get dimensions
    numberData, dimensions = trainingMatrix.shape

    #center data
    mean_X = trainingMatrix.mean(axis=0)
    trainingMatrix = trainingMatrix - mean_X

    if dimensions>numberData:
        #PCA - compact trick used
        M = dot(trainingMatrix, trainingMatrix.T)
        e, EV = linalg.eigh(M) #eigenvalues and eigenvectors
        tmp = dot(trainingMatrix.T, EV).T #compact trick
        V = tmp[::-1] #reverse to get the last eigenvectors first
        S = sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        #PCA - SVD used
        U, S, V = linalg.svd(trainingMatrix)
        V = V[:numberData] #only makes sense to return the first num data

    #return the projection matrix, variance, and the mean
        return V, S, mean_X







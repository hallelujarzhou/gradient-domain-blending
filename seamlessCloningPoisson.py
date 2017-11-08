'''
  File name: seamlessCloningPoisson.py
  Author:
  Date created:
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mplPath
from PIL import Image
from pylab import plot, ginput, show
import numpy.linalg as lin
import scipy.misc

from drawMask import draw_mask
from maskImage import maskImage
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import resizeImage, getSolutionVect
from reconstructImg import reconstructImg

def clean(Xarray):
    for j in range(Xarray.shape[0]):
        if Xarray[j] < 0:
            Xarray[j] = 0
        if Xarray[j] > 255:
            Xarray[j] = 255


def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
    # Enter Your Code Here

    targetH = targetImg.shape[0]
    targetW = targetImg.shape[1]

    indexes = getIndexes(mask, targetH, targetW, offsetX, offsetY)

    coeffA = getCoefficientMatrix(indexes)

    SolVectorbR = getSolutionVect(indexes, sourceImg[:,:,0], targetImg[:,:,0], offsetX, offsetY)
    SolVectorbG = getSolutionVect(indexes, sourceImg[:,:,1], targetImg[:,:,1], offsetX, offsetY)
    SolVectorbB = getSolutionVect(indexes, sourceImg[:,:,2], targetImg[:,:,2], offsetX, offsetY)

    red = lin.solve(coeffA,SolVectorbR)
    clean(red)

    green = lin.solve(coeffA,SolVectorbG)
    clean(green)

    blue = lin.solve(coeffA,SolVectorbB)
    clean(blue)

    resultImg = reconstructImg(indexes, red, green, blue, targetImg)

    return resultImg

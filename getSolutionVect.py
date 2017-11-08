'''
  File name: getSolutionVect.py
  Author:
  Date created:
'''
import numpy as np
from scipy import signal

def resizeImage(img, source, target, offsetX, offsetY):
    res = np.zeros((target.shape[0],target.shape[1]))
    for j in range(0,source.shape[0]):
        for i in range(0,source.shape[1]):
            res[j+offsetY][i+offsetX] = img[j][i]
    return res

def getSolutionVect(indexes, source, target, offsetX, offsetY):
    # Enter Your Code Here
    n = np.count_nonzero(indexes)
    b = np.zeros(n+1)
    laplacian = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    imSrc = source
    imDest = target

    imSrc = resizeImage(imSrc, source, target, offsetX, offsetY)

    imLaplacian = signal.convolve2d(imSrc, laplacian, mode='same',boundary='fill', fillvalue=0)

    count = 0

    for j in range(1,indexes.shape[0]-1):
        for i in range(1,indexes.shape[1]-1):
            if indexes[j][i]:
                count += 1

                if not indexes[j-1][i]:
                    b[count] += imDest[j-1][i]

                if not indexes[j+1,i]:
                    b[count] += imDest[j+1][i]

                if not indexes[j,i-1]:
                    b[count] += imDest[j][i-1]

                if not indexes[j,i+1]:
                    b[count] += imDest[j][i+1]

                b[count] += imLaplacian[j][i]

    SolVectorb = b[1:]
    return SolVectorb

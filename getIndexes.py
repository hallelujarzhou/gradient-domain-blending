'''
  File name: getIndexes.py
  Author:
  Date created:
'''
import numpy as np


def getIndexes(mask, targetH, targetW, offsetX, offsetY):
    #Enter Your Code Here
    indexes = np.zeros((targetH,targetW))
    index = 0
    for j in range(mask.shape[0]):
        for i in range(mask.shape[1]):
            if mask[j][i] == 1:
                index += 1
                indexes[j+offsetY][i+offsetX] = index
    return indexes

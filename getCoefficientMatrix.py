'''
  File name: getCoefficientMatrix.py
  Author:
  Date created:
'''
import numpy as np


def getCoefficientMatrix(indexes):
    # Enter Your Code Here
    n = np.count_nonzero(indexes)
    coeffA = np.zeros((n+1,n+1))
    count = 0
    for j in range(1,indexes.shape[0]-1):
        for i in range(1,indexes.shape[1]-1):
            if indexes[j][i]:
                count += 1
                if indexes[j-1,i]:
                    coeffA[count][int(indexes[j-1][i])] = -1
                if indexes[j+1,i]:
                    coeffA[count][int(indexes[j+1][i])] = -1
                if indexes[j,i-1]:
                    coeffA[count][int(indexes[j][i-1])] = -1
                if indexes[j,i+1]:
                    coeffA[count][int(indexes[j][i+1])] = -1
                coeffA[count][count] = 4
    x = coeffA[1:,1:]
    return x

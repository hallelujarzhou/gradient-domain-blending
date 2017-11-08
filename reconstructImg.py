'''
  File name: reconstructImg.py
  Author:
  Date created:
'''
import numpy as np

def reconstructImg(indexes, red, green, blue, targetImg):
    # Enter Your Code Here
    resultImg = targetImg
    for j in range(0,targetImg.shape[0]):
        for i in range(0,targetImg.shape[1]):
            if indexes[j][i]:
                idx = indexes[j][i]
                resultImg[j][i][0] = red[int(idx-1)]
                resultImg[j][i][1] = green[int(idx-1)]
                resultImg[j][i][2] = blue[int(idx-1)]
    return resultImg

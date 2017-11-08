import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mplPath
from PIL import Image
from pylab import plot, ginput, show
import numpy.linalg as lin
import scipy.misc

from maskImage import maskImage
from seamlessCloningPoisson import seamlessCloningPoisson


sourceImg = np.array(Image.open('SourceImage.jpg').convert('RGB'))

targetImg = np.array(Image.open('TargetImage.jpg').convert('RGB'))

mask = maskImage(sourceImg)

print(mask)

offsetX = 130
offsetY = 250

result = seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY)

scipy.misc.imsave('blendimg.jpg', result)

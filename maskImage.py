'''
  File name: maskImage.py
  Author:
  Date created:
'''

from drawMask import draw_mask

def maskImage(img):
    # Enter Your Code Here
    mask, bbox = draw_mask(img)
    return mask

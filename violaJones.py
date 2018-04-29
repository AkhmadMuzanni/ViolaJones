# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:27:48 2018

@author: USER
"""

import cv2
import numpy as np
# Read Image and convert it to gray image
image = cv2.imread('resized_image40x20.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Testing', image)

# make array for result of integral image
h, w = image.shape
result = np.zeros((h,w),dtype=int)    

def integralImage():    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i][j] = image[i][j] + intImage(i-1,j) + intImage(i,j-1) - intImage(i-1,j-1)            
               
    print(result[0][0])        
    print(w)
    print(h)

def intImage(a,b):
    if(a < 0) or (b < 0):
        return 0
    else:
        return result[a][b]
        

integralImage()
print(intImage(0,1))
    

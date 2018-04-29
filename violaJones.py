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
#cv2.imshow('Testing', image)

# make array for result of integral image
h, w = image.shape
result = np.zeros((h,w),dtype=int)    
feature1 = []
feature2 = []
feature3 = []
feature4 = []
feature5 = []

# method integralImage to generate the value of integralimage of image to array result
def integralImage():    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i][j] = image[i][j] + intImage(i-1,j) + intImage(i,j-1) - intImage(i-1,j-1)            
               
    print(result[0][0])        
    print(w)
    print(h)

# method intImage for count the value of result at specified index
def intImage(a,b):
    if(a < 0) or (b < 0):
        return 0
    else:
        return result[a][b]

# method haarFeature to find all possible size of haar feature
def haarFeature(feature,a,b):
    i = 1
    #j = 0
    while(a*i <= image.shape[1]):
        j = 0
        while(b*j <= image.shape[0]):            
            feature.append((b*j,a*i))
            j = j+1
        i = i+1
        
   
        
# generate value of integral image
integralImage()
print(intImage(0,1))

# search all possible size of 5 haar feature
haarFeature(feature1,2,1)
haarFeature(feature2,1,2)
haarFeature(feature3,3,1)
haarFeature(feature4,1,3)
haarFeature(feature5,2,2)
    

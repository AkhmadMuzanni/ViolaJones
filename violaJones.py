# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:27:48 2018

@author: USER
"""

import cv2
import numpy as np
import csv
# Read Image and convert it to gray image
image = cv2.imread('resized_image24x24.jpg')
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
nilai1 = []
nilai2 = []
nilai3 = []
nilai4 = []
nilai5 = []
nilai = []

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
        j = 1
        while(b*j <= image.shape[0]):            
            feature.append((b*j,a*i))
            j = j+1
        i = i+1
        
# method applyFeature to apply possible size of feature to image (i,j,w,h) => i = initial x position, j = initial y position, w = width of feature, h = height of feature
def applyFeatureAll(feature, noFeature):
    for x in range(len(feature)):
        a = 0
        while(feature[x][0] + a <= result.shape[0]):
            b = 0
            while(feature[x][1] + b <= result.shape[1]):
                value = 0
                if noFeature == 1:
                    s1 = intImage(a-1,b-1) + intImage(a + feature[x][0] - 1,b + (feature[x][1]/2) - 1) - intImage(a - 1, b + (feature[x][1]/2) - 1) - intImage(a + feature[x][0] - 1, b - 1)
                    s2 = intImage(a-1,b + (feature[x][1]/2) - 1) + intImage(a + feature[x][0] - 1,b + (feature[x][1]) - 1) - intImage(a-1,b + (feature[x][1]) - 1) - intImage(a + feature[x][0] - 1,b + (feature[x][1]/2) - 1)
                    value = s1-s2
                    nilai.append((noFeature,a,b,feature[x][0],feature[x][1]/2,s1,s2,value))
                elif noFeature == 2:
                    s1 = intImage(a-1,b-1) + intImage(a + (feature[x][0]/2) - 1,b + feature[x][1] - 1) - intImage(a-1,b + feature[x][1] - 1) - intImage(a + (feature[x][0]/2) - 1,b-1)
                    s2 = intImage(a + (feature[x][0]/2) - 1,b-1) + intImage(a + (feature[x][0]) - 1,b + feature[x][1] - 1) - intImage(a + (feature[x][0]/2) - 1,b + feature[x][1] - 1) - intImage(a + (feature[x][0]) - 1, b-1)
                    value = s1-s2
                    nilai.append((noFeature,a,b,feature[x][0]/2,feature[x][1],s1,s2,value))
                elif noFeature == 3:
                    nilai.append((noFeature,a,b,feature[x][0],feature[x][1]/3))
                elif noFeature == 4:
                    nilai.append((noFeature,a,b,feature[x][0]/3,feature[x][1]))
                else:
                     nilai.append((noFeature,a,b,feature[x][0]/2,feature[x][1]/2))   
                #nilai.append((noFeature,a,b,feature[x][0],feature[x][1]))
                #nilai.append((a,b,feature[x][0] + a - 1,feature[x][1] + b - 1))
                #print((str)(a)+ ','+(str)(feature[x][1] + a))
                b = b + 1
            a = a + 1


# generate value of integral image
integralImage()
print(intImage(0,1))

# search all possible size of 5 haar feature
haarFeature(feature1,2,1)
haarFeature(feature2,1,2)
haarFeature(feature3,3,1)
haarFeature(feature4,1,3)
haarFeature(feature5,2,2)

#applyFeature(feature1,nilai1)
#applyFeature(feature2,nilai2)
#applyFeature(feature3,nilai3)
#applyFeature(feature4,nilai4)
#applyFeature(feature5,nilai5)

applyFeatureAll(feature1,1)
applyFeatureAll(feature2,2)
applyFeatureAll(feature3,3)
applyFeatureAll(feature4,4)
applyFeatureAll(feature5,5)

myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(nilai)

#with open('example4.csv', 'w') as csvfile:
#    fieldnames = ['first_name', 'last_name', 'Grade']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 
#    writer.writeheader()
#    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
#    writer.writerow({'Grade': 'A', 'first_name': 'Rachael', 'last_name': 'Rodriguez'})
#    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
#    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
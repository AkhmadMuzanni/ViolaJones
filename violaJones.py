# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:27:48 2018

@author: USER
"""

import cv2
import numpy as np
import csv
import os
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
nilai1 = []
nilai2 = []
nilai3 = []
nilai4 = []
nilai5 = []
nilai = [[],[]]
dataTraining = np.array(10)
theta = 10 # threshold
gambar = []
m = 9
l = 3
w = 1.0/(l+m)
# method integralImage to generate the value of integralimage of image to array result
def integralImage(image):
    res = np.zeros((result.shape[0],result.shape[1]),dtype=int)
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i][j] = image[i][j] + intImage(res,i-1,j) + intImage(res,i,j-1) - intImage(res,i-1,j-1)            
               
    #print(result[0][0])        
    #print(w)
    #print(h)
    return res

# method intImage for count the value of result at specified index
def intImage(res,a,b):
    if(a < 0) or (b < 0):
        return 0
    else:
        return res[a][b]

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
        
# method applyFeature to apply possible size of feature to image (i,j,w,h) => i = initial x position, j = initial y position, w = factor scaling of width of feature, h = factor scaling of height of feature
def applyFeatureAll(noImage, res, feature, noFeature):
    values = []    
    
    for x in range(len(feature)):        
        if (noImage == 0):
            fileImage = open('training/dataTraining0.csv', 'a')
        else:
            fileImage = open('training/dataTraining'+str(noImage)+'.csv', 'a')
        with fileImage:
            writer = csv.writer(fileImage)
            a = 0
            while(feature[x][0] + a <= res.shape[0]):
                b = 0
                while(feature[x][1] + b <= res.shape[1]):
                    value = 0
                    if noFeature == 1:
                        s1 = intImage(res,a-1,b-1) + intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/2) - 1) - intImage(res,a - 1, b + (feature[x][1]/2) - 1) - intImage(res,a + feature[x][0] - 1, b - 1)
                        s2 = intImage(res,a-1,b + (feature[x][1]/2) - 1) + intImage(res,a + feature[x][0] - 1,b + (feature[x][1]) - 1) - intImage(res,a-1,b + (feature[x][1]) - 1) - intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/2) - 1)
                        value = s1-s2
                        values.append([noFeature,a,b,feature[x][0],feature[x][1]/2,value])                        
                        writer.writerow([value])
                    elif noFeature == 2:
                        s1 = intImage(res,a-1,b-1) + intImage(res,a + (feature[x][0]/2) - 1,b + feature[x][1] - 1) - intImage(res,a-1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/2) - 1,b-1)
                        s2 = intImage(res,a + (feature[x][0]/2) - 1,b-1) + intImage(res,a + (feature[x][0]) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/2) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]) - 1, b-1)
                        value = s1-s2
                        values.append([noFeature,a,b,feature[x][0]/2,feature[x][1],value])                        
                        writer.writerow([value])
                    elif noFeature == 3:
                        s1 = intImage(res,a-1,b-1) + intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/3) - 1) - intImage(res,a - 1, b + (feature[x][1]/3) - 1) - intImage(res,a + feature[x][0] - 1, b - 1)
                        s2 = intImage(res,a-1,b + (feature[x][1]/3) - 1) + intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/3*2) - 1) - intImage(res,a-1,b + (feature[x][1]/3*2) - 1) - intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/3) - 1)
                        s3 = intImage(res,a-1,b + (feature[x][1]/3*2) - 1) + intImage(res,a + feature[x][0] - 1,b + (feature[x][1]) - 1) - intImage(res,a-1,b + (feature[x][1]) - 1) - intImage(res,a + feature[x][0] - 1,b + (feature[x][1]/3*2) - 1)
                        value = s1-s2+s3
                        values.append([noFeature,a,b,feature[x][0],feature[x][1]/3,value])                        
                        writer.writerow([value])
                    elif noFeature == 4:
                        s1 = intImage(res,a-1,b-1) + intImage(res,a + (feature[x][0]/3) - 1,b + feature[x][1] - 1) - intImage(res,a-1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/3) - 1,b-1)
                        s2 = intImage(res,a + (feature[x][0]/3) - 1,b-1) + intImage(res,a + (feature[x][0]/3*2) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/3) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/3*2) - 1, b-1)
                        s3 = intImage(res,a + (feature[x][0]/3*2) - 1,b-1) + intImage(res,a + (feature[x][0]) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]/3*2) - 1,b + feature[x][1] - 1) - intImage(res,a + (feature[x][0]) - 1, b-1)
                        value = s1-s2+s3
                        values.append([noFeature,a,b,feature[x][0]/3,feature[x][1],value])                        
                        writer.writerow([value])
                    else:
                        s1 = intImage(res,a-1,b-1) + intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]/2) - 1) - intImage(res,a - 1, b + (feature[x][1]/2) - 1) - intImage(res,a + (feature[x][0]/2) - 1, b - 1)
                        s2 = intImage(res,a-1,b + (feature[x][1]/2) - 1) + intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]) - 1) - intImage(res,a-1,b + (feature[x][1]) - 1) - intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]/2) - 1)
                        s3 = intImage(res,a + (feature[x][0]/2) - 1,b-1) + intImage(res,a + (feature[x][0]) - 1,b + (feature[x][1]/2) - 1) - intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]/2) - 1) - intImage(res,a + (feature[x][0]) - 1, b-1)
                        s4 = intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]/2) - 1) + intImage(res,a + (feature[x][0]) - 1,b + (feature[x][1]) - 1) - intImage(res,a + (feature[x][0]/2) - 1,b + (feature[x][1]) - 1) - intImage(res,a + (feature[x][0]) - 1,b + (feature[x][1]/2) - 1)
                        value = s1-s2-s3+s4
                        values.append([noFeature,a,b,feature[x][0]/2,feature[x][1]/2,value])                        
                        writer.writerow([value])
                    #nilai.append((noFeature,a,b,feature[x][0],feature[x][1]))
                    #nilai.append((a,b,feature[x][0] + a - 1,feature[x][1] + b - 1))
                    #print((str)(a)+ ','+(str)(feature[x][1] + a))
                    b = b + 1
                a = a + 1
        fileImage.close()
    return values

def setDataTraining():      
    value = []
    # loop for data training (positive)
    for x in range(3):
        #result = integralImage(cv2.imread('bahan/positif/'+str(x+1)+'.jpg',0))        
        pict = cv2.imread('bahan/positif/r'+str(x+1)+'.jpg',0)
        value.append([[],[1]])
        value[x][0].append(applyFeatureAll((x+1),integralImage(pict),feature1,1))
        value[x][0].append(applyFeatureAll((x+1),integralImage(pict),feature2,2))
        value[x][0].append(applyFeatureAll((x+1),integralImage(pict),feature3,3))
        value[x][0].append(applyFeatureAll((x+1),integralImage(pict),feature4,4))
        value[x][0].append(applyFeatureAll((x+1),integralImage(pict),feature5,5))
        
        #print(result)
        #dataTraining.append(result)
        #dataTraining.append(cv2.imread('bahan/positif/1.jpg',0))
     #= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # loop for data training (negative)
    for x in range(9):
        #result = integralImage(cv2.imread('bahan/positif/'+str(x+1)+'.jpg',0))        
        pict = cv2.imread('bahan/negatif/br'+str(x+1)+'.jpg',0)
        value.append([[],[0]])
        value[l+x][0].append(applyFeatureAll((l+x+1),integralImage(pict),feature1,1))
        value[l+x][0].append(applyFeatureAll((l+x+1),integralImage(pict),feature2,2))
        value[l+x][0].append(applyFeatureAll((l+x+1),integralImage(pict),feature3,3))
        value[l+x][0].append(applyFeatureAll((l+x+1),integralImage(pict),feature4,4))
        value[l+x][0].append(applyFeatureAll((l+x+1),integralImage(pict),feature5,5))
        
    return value   

def adaboost():
    # count initial weight. (between 1/m until 1/n, with m and l are number of negative and positive image)    
    #m = 9
    #l = 3
    #w = 1.0/(m+l)
    '''total = 0
    for i in range(len(nilai[0])):
        for j in range(len(nilai[0][i])):
            total += nilai[0][i][j][5]
    print(1.0/total)'''
    # assign inital weigth to all feature
    for i in range(len(nilai[0])):
        for j in range(len(nilai[0][i])):
            # assign p
            nilai[0][i][j].append(1)
            # assign weight
            nilai[0][i][j].append(w)
            # assign error
            nilai[0][i][j].append(1)
            
    minValue = 99999
    argMin = [0,0,0]
    for i in range(len(nilai[0])):
        for j in range(len(nilai[0][i])): 
            h = 1
            p = nilai[0][i][j][6]
            if (p*nilai[0][i][j][5] < p*theta):
                h = 0
            nilai[0][i][j][8] = 0
            for x in range(len(dataTraining)):                
                nilai[0][i][j][8] += dataTraining[x][0][i][j][5] * np.abs(dataTraining[x][1][0] - h)
            if (nilai[0][i][j][8] < minValue):
                minValue = nilai[0][i][j][8]
                argMin[0] = nilai[0][i][j]
    
    print(minValue)
    print(argMin[0])
                #argMin[0]
            #nilai[0][i][j].append(minValue)
    

# generate value of integral image
result = integralImage(image)
#print(intImage(0,1))

# search all possible size of 5 haar feature
haarFeature(feature1,2,1)
# => [1 0]
haarFeature(feature2,1,2)
# => [1]
#    [0]
haarFeature(feature3,3,1)
# => [1 0 1]
haarFeature(feature4,1,3)
# => [1]
#    [0]
#    [1]
haarFeature(feature5,2,2)
# => [1 0]
#    [0 1]

#applyFeature(feature1,nilai1)
#applyFeature(feature2,nilai2)
#applyFeature(feature3,nilai3)
#applyFeature(feature4,nilai4)
#applyFeature(feature5,nilai5)
for x in range(2):
    try:
        os.remove('training/*.csv')
        os.remove('training/dataTraining'+str(x)+'.csv')
    except OSError, e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename,e.strerror))
    

nilai[0].append(applyFeatureAll(0,result,feature1,1))
nilai[0].append(applyFeatureAll(0,result,feature2,2))
nilai[0].append(applyFeatureAll(0,result,feature3,3))
nilai[0].append(applyFeatureAll(0,result,feature4,4))
nilai[0].append(applyFeatureAll(0,result,feature5,5))


dataTraining = setDataTraining()
adaboost()

#with open('example4.csv', 'w') as csvfile:
#    fieldnames = ['first_name', 'last_name', 'Grade']
#    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# 
#    writer.writeheader()
#    writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
#    writer.writerow({'Grade': 'A', 'first_name': 'Rachael', 'last_name': 'Rodriguez'})
#    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
#    writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
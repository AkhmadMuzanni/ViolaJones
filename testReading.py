# -*- coding: utf-8 -*-
"""
Created on Thu May 03 00:32:25 2018

@author: USER
"""
import csv
def read():
    with open('training/dataTrainingR2.csv') as csvfile:
        i = 0
        reader= csv.DictReader(csvfile)
        for row in reader:
            if (i == 0):
                print(row)
            i = i+1
def write():
    myFile = open('training/test.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        x = 0        
        while (x <= 10):
            v = [1,2,3,x]
            writer.writerow(v)
            x = x+1
    myFile.close()

write()
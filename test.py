# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:09:11 2020

@author: Steven
"""

import csv
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

def generateHistogramCSV(filename, fileFormat):
    #create storage for value stored in
    tempStorage = np.zeros((3,256), dtype = np.uint32)
    
    image = img.imread(filename + "." + fileFormat)
    imgHeight, imgWidth = image.shape[:2]
    #plt.imshow(image)
    
    print(image.shape)
    

    
    
    for height in range(imgHeight):
        for width in range(imgWidth):
            valueR = image[height, width, 0]
            valueG = image[height, width, 1]
            valueB = image[height, width, 2]
            
            tempStorage[0, valueR] += 1
            tempStorage[1, valueG] += 1
            tempStorage[2, valueB] += 1
            
    
    print(tempStorage.shape)
    '''
    write values to .csv file
    '''
    with open('Apartment_float_o15C Histogram.csv', 'w', newline='') as file:
        #create a writer object
        writer = csv.writer(file)
        #write initial value config.
        writer.writerow([filename,"","","","","","","","",""])
        writer.writerow([str(imgWidth) + "*" + str(imgHeight),"","Red","Green","Blue","","","","",""])
        writer.writerow(["resolution", "value", "count", "count", "count", "", "", "", "", ""])
        #write all statistical values
        for value in range(256):
            writer.writerow([imgHeight*imgWidth, value, tempStorage[0, value], tempStorage[1, value], tempStorage[2, value], "", "", "", "", ""])
    

if __name__ == "__main__":
    generateHistogramCSV("Apartment_float_o15C", "bmp")
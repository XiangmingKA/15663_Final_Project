# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 22:28:55 2022

@author: 71552
"""
import skimage.io
import math
%matplotlib qt
import matplotlib.pyplot as plt
from scipy.interpolate import interpn
import numpy as np
from skimage.color import rgb2gray
import cv2
from scipy.interpolate import interp2d

pitch_width = 20

def Generate_Mosaic(offset_x, offset_y):
    
    height = 2000
    width  = 3000
    back_ground = np.zeros((height,width,3), dtype=np.float16)
    
    offset = np.array([offset_x,offset_y])
    
    
    num_of_width = int((width / pitch_width)/2)
    num_of_height = int((height / pitch_width))
    
    for i in range(num_of_width):
        for j in range(num_of_height):
            y_start = int(max(0, offset[0] + j * pitch_width))
            y_start = min(y_start,height)
            y_end   = int(min(height, offset[0] + (j+1) * pitch_width))
            y_end   = max(0, y_end)
            if j % 2 == 0:
                x_start = int(max(0, offset[1] + i*2 * pitch_width))
                x_end   = int(min(width, offset[1] + ((i*2)+1) * pitch_width))
            else:
                x_start = int(max(0, offset[1] + ((i*2)-1) * pitch_width))
                x_end   = int(min(width, offset[1] + ((i*2)) * pitch_width))
                
            x_start = min(x_start,width)
            x_end   = max(0, x_end)
            
            back_ground[y_start:y_end, x_start:x_end,: ] = np.ones((y_end - y_start,x_end - x_start,3), dtype=np.float16)
            
    inv_result = 1.0 - back_ground
    
    skimage.io.imsave('Mosaic'+str(offset[0]) + ',' +str(offset[1])+ '.png',back_ground)
    skimage.io.imsave('Inv_Mosaic'+str(offset[0]) + ',' +str(offset[1])+ '.png',inv_result)
    
    return back_ground
    
def Generate_M_Debug(offset_x, offset_y):
    
    height = 2000
    width  = 3000
    back_ground = np.zeros((height,width,3), dtype=np.float16)
    
    offset = np.array([offset_x,offset_y])
    
    
    num_of_width = int((width / pitch_width)/2)
    num_of_height = int((height / pitch_width))
    
    for i in range(num_of_width):
        for j in range(num_of_height):
            y_start = int(max(0, offset[0] + j * pitch_width))
            y_start = min(y_start,height)
            y_end   = int(min(height, offset[0] + (j+1) * pitch_width))
            y_end   = max(0, y_end)
            if j % 2 == 0:
                x_start = int(max(0, offset[1] + i*2 * pitch_width))
                x_end   = int(min(width, offset[1] + ((i*2)+1) * pitch_width))
            else:
                x_start = int(max(0, offset[1] + ((i*2)-1) * pitch_width))
                x_end   = int(min(width, offset[1] + ((i*2)) * pitch_width))
                
            x_start = min(x_start,width)
            x_end   = max(0, x_end)
            
            back_ground[y_start:y_end, x_start:x_end,: ] = np.ones((y_end - y_start,x_end - x_start,3), dtype=np.float16)
    return back_ground
# Generate_Mosaic(5,0)
# Generate_Mosaic(5,5)
# Generate_Mosaic(5,10)
# Generate_Mosaic(5,15)

# Generate_Mosaic(10,0)
# Generate_Mosaic(10,5)
# Generate_Mosaic(10,10)
# Generate_Mosaic(10,15)

# Generate_Mosaic(15,0)
# Generate_Mosaic(15,5)
# Generate_Mosaic(15,10)
# Generate_Mosaic(15,15)

# Generate_Mosaic(20,0)
# Generate_Mosaic(20,5)
# Generate_Mosaic(20,10)
# Generate_Mosaic(20,15)
# Generate_Mosaic(20,20)

# Generate_Mosaic(5,20)
# Generate_Mosaic(10,20)
# Generate_Mosaic(15,20)

def Validate():
    height = 2000
    width  = 3000
    result = np.zeros((height,width,3), dtype=np.float64)
    
    # result += Generate_M_Debug(-15, 0)
    # result += Generate_M_Debug(-15, 5)
    # result += Generate_M_Debug(-15, 10)
    # result += Generate_M_Debug(-15, 15)
    # result += Generate_M_Debug(-15, 20)
    # result += Generate_M_Debug(-15, 25)
    # # result += Generate_M_Debug(-15, 30)
    
    # result += Generate_M_Debug(-10, 0)
    # result += Generate_M_Debug(-10, 5)
    # result += Generate_M_Debug(-10, 10)
    # result += Generate_M_Debug(-10, 15)
    # result += Generate_M_Debug(-10, 20)
    # result += Generate_M_Debug(-10, 25)
    # result += Generate_M_Debug(-10, 30)
    # result += Generate_M_Debug(-10, 30)
    
    # result += Generate_M_Debug(-5, 0)
    # result += Generate_M_Debug(-5, 5)
    # result += Generate_M_Debug(-5, 10)
    # result += Generate_M_Debug(-5, 15)
    # result += Generate_M_Debug(-5, 20)
    # result += Generate_M_Debug(-5, 25)
    # result += Generate_M_Debug(-5, 30)
    
    
    result += Generate_M_Debug(0, 0)
    result += Generate_M_Debug(0, 3)
    result += Generate_M_Debug(0, 6)
    result += Generate_M_Debug(0, 9)
    result += Generate_M_Debug(0, 12)
    # result += Generate_M_Debug(0, 15)
    
    result += Generate_M_Debug(3, 0)
    result += Generate_M_Debug(3, 3)
    result += Generate_M_Debug(3, 6)
    result += Generate_M_Debug(3, 9)
    result += Generate_M_Debug(3, 12)
    # result += Generate_M_Debug(3, 15)
    
    result += Generate_M_Debug(6, 0)
    result += Generate_M_Debug(6, 3)
    result += Generate_M_Debug(6, 6)
    result += Generate_M_Debug(6, 9)
    result += Generate_M_Debug(6, 12)
    # result += Generate_M_Debug(6, 15)
    
    result += Generate_M_Debug(9, 0)
    result += Generate_M_Debug(9, 3)
    result += Generate_M_Debug(9, 6)
    result += Generate_M_Debug(9, 9)
    result += Generate_M_Debug(9, 12)
    # result += Generate_M_Debug(9, 15)
    
    result += Generate_M_Debug(12, 0)
    result += Generate_M_Debug(12, 3)
    result += Generate_M_Debug(12, 6)
    result += Generate_M_Debug(12, 9)
    result += Generate_M_Debug(12, 12)
    # result += Generate_M_Debug(12, 15)
    
    # result += Generate_M_Debug(0, 15)
    # result += Generate_M_Debug(0, 20)
    # result += Generate_M_Debug(0, 25)
    # result += Generate_M_Debug(0, 30)

    # result += Generate_M_Debug(5, 0)
    # result += Generate_M_Debug(5, 5)
    # result += Generate_M_Debug(5, 10)
    # result += Generate_M_Debug(5, 15)
    # result += Generate_M_Debug(5, 20)
    
    # result += Generate_M_Debug(10, 0)
    # result += Generate_M_Debug(10, 5)
    # result += Generate_M_Debug(10, 10)
    # result += Generate_M_Debug(10, 15)
    # result += Generate_M_Debug(10, 20)
    
    
    # result += Generate_M_Debug(5, 25)
    # result += Generate_M_Debug(5, 30)
    
    # result += Generate_M_Debug(15, 0)
    # result += Generate_M_Debug(15, 5)
    # result += Generate_M_Debug(15, 10)
    # result += Generate_M_Debug(15, 15)
    # result += Generate_M_Debug(15, 20)
    # # result += Generate_M_Debug(15, 25)
    # # result += Generate_M_Debug(15, 30)
    
    # result += Generate_M_Debug(20, 0)
    # result += Generate_M_Debug(20, 5)
    # result += Generate_M_Debug(20, 10)
    # result += Generate_M_Debug(20, 15)
    # result += Generate_M_Debug(20, 20)
    # result += Generate_M_Debug(20, 25)
    
    result = np.amin(result, axis=2)
    print(str(np.amin(np.amin(result, axis=1))))
    
    skimage.io.imsave('validate.png',result)
    
# Validate()
Generate_Mosaic(0, 0)
Generate_Mosaic(0, 6)
Generate_Mosaic(0, 12)
Generate_Mosaic(0, 18)
Generate_Mosaic(0, 24)
Generate_Mosaic(0, 30)

Generate_Mosaic(6, 0)
Generate_Mosaic(6, 6)
Generate_Mosaic(6, 12)
Generate_Mosaic(6, 18)
Generate_Mosaic(6, 24)
Generate_Mosaic(6, 30)

Generate_Mosaic(12, 0)
Generate_Mosaic(12, 6)
Generate_Mosaic(12, 12)
Generate_Mosaic(12, 18)
Generate_Mosaic(12, 24)
Generate_Mosaic(12, 30)

Generate_Mosaic(18, 0)
Generate_Mosaic(18, 6)
Generate_Mosaic(18, 12)
Generate_Mosaic(18, 18)
Generate_Mosaic(18, 24)
Generate_Mosaic(18, 30)

Generate_Mosaic(24, 0)
Generate_Mosaic(24, 6)
Generate_Mosaic(24, 12)
Generate_Mosaic(24, 18)
Generate_Mosaic(24, 24)
Generate_Mosaic(24, 30)

Generate_Mosaic(30, 0)
Generate_Mosaic(30, 6)
Generate_Mosaic(30, 12)
Generate_Mosaic(30, 18)
Generate_Mosaic(30, 24)
Generate_Mosaic(30, 30)

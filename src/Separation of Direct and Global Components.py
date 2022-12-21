# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:09:42 2022

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

N = (2**8) -1
N = 1

title = "_strip"

def Generate_Image_stack():
    
    starting_index = 3934
    num_of_img = 4
    
    test_image = skimage.io.imread('../data/strip/IMG_' + str(starting_index) + '.jpg')
    
    width = test_image.shape[1]
    height = test_image.shape[0]
    
    stack = np.zeros((height,width,3,num_of_img), dtype=np.float64)
    
    for i in range(num_of_img):
        stack[:,:,:,i] = skimage.io.imread('../data/strip/IMG_' + str(starting_index+i) + '.jpg')/N

    return stack
    

def Direct_and_Global_Components_Separation():
    
    img_stack = Generate_Image_stack()
    
    # back_imge = skimage.io.imread('../data/IMG_2865.jpg')/N
    
    width = img_stack.shape[1]
    height = img_stack.shape[0]
    
    img_max = np.amax(img_stack, axis=3)
    img_min = np.amin(img_stack, axis=3)
    
    skimage.io.imsave('img_max'+title+'.png',img_max)
    skimage.io.imsave('img_min'+title+'.png',img_min)
    
    b = 0.1
    
    L_d = (img_max - img_min)/(1-b)
    L_g = (img_max - L_d) / (1 + b) * 2
    
    skimage.io.imsave('L_d'+title+'.png',L_d)
    skimage.io.imsave('L_g'+title+'.png',L_g)
    
def Generate_Novel_Image():
    
    Ld = skimage.io.imread('L_d_occluder2.png')
    Lg = skimage.io.imread('L_g_occluder2.png')
    
    Ld_weight = 2.0
    Lg_weight = 3.0
    
    result = (Ld_weight* Ld + Lg_weight*Lg)/2.0
    
    skimage.io.imsave('novel_occluder.png',result)
        
            
# Direct_and_Global_Components_Separation()
Generate_Novel_Image()
            
    
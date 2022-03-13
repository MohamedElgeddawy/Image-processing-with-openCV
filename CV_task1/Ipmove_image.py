#Name : Mohamed Eslam 
#sec  : 3

import numpy as np
import cv2 as cv

img = cv.imread('Imege.jpeg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('improved.png',res)


import numpy as np
import cv2 as cv

img = cv.imread('WhatsApp Image 2022-03-12 at 6.43.38 PM.jpeg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('NEW.png',res)


import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

# reading image
img=cv.imread('images/elephants.jpg')

# green (0,255,0)


# paint image a certain color
blank[100:150, 200:250]=0,255,0
cv.imshow('Green filled rectangle', blank)

# draw a rectangle
# normal border thickness
cv.rectangle(blank, (blank[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Green oulined rectangle', blank)

# draw a circle
cv.circle(blank,(blank[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=1)
cv.imshow('Green oulined Circle',blank)

# showing image
cv.imshow('Elephants', img)

# waiting
cv.waitKey(0)
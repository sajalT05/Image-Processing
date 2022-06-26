import cv2 as cv

# reading image
img=cv.imread('images/elephants.jpg')

# showing image
cv.imshow('Pigeon', img)

# waiting
cv.waitKey(0)
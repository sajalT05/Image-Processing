import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    '''
    rescale frame
    '''
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# reading image
img=cv.imread('images/elephants.jpg')

# rescaling image
imageRescaled=rescaleFrame(img,scale=0.25)

# showing image
cv.imshow('Elephant', img)
# show rescaled image
cv.imshow('Resized Elephant',img)


# waiting
cv.waitKey(0)
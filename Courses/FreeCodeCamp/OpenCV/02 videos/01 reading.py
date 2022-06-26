import cv2 as cv

# read video
capture = cv.VideoCapture('videos/prople.mp4')

while True:
    '''
    present video by single frames
    '''
    # create frame
    isTrue, frame=capture.read()
    # present frame
    cv.imshow('Video',frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()

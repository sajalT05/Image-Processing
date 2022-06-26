import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    '''
    rescale frame
    '''
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# read video
capture = cv.VideoCapture('videos/people.mp4')

while True:
    '''
    present video by single frames
    '''
    # create frame
    isTrue, frame=capture.read()

    # resize frame
    videoRescaled=rescaleFrame(frame,scale=0.25)

    # present frame
    cv.imshow('Video',frame)
    # present resized frame
    cv.imshow('Video Resized',videoRescaled)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()

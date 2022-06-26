import cv2 as cv
import mediapipe as mp
import time

# capture video from directory
capture_saved_video=cv.VideoCapture('video.mp4')

pTime=0

# drawing on frame
# draw on faces
mpDraw=mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# create face mesh
mpFaceMesh=mp.solutions.face_mesh
# create objects
    # set maximum number of faces to detect
faceMesh=mpFaceMesh.FaceMesh(max_num_faces=2)


while True:
    # capture video frame by frame
    success, frame = capture_saved_video.read()
    frameRGB=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frameRGB, face,mp.FaceMesh.FACE_CONNECTIONS)
            mpDraw.draw_face_id(frameRGB, face.face_id)

    # frame rate of video
    # current time
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    # publish frame rate
    cv.putText(frame, f"FPS: {int(fps)}",(10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1)

    # show each captured frame
    cv.imshow('saved video', frame)
    # wait to end
    cv.waitKey(1)

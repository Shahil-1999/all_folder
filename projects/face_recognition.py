# import libararies 

import numpy as np # for mathematical use 
import cv2 # cv2 means open-cv for capturing the motions 

cap = cv2.VideoCapture(0) # to turn on the camera 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # for face detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # for eye detection 

while True:
    ret, frame = cap.read() # for reading the video data or visual data capturing 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # to detect the default color of our background or face 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # to capture accurate images or objects 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w] # do adjust left and right as per frame size 
        roi_color = frame[y:y+h, x:x+w] # do adjust the height and widht 
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5) 
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord(' '): # space is beign use for terminate the video can screen 
        break

cap.release()
cv2.destroyAllWindows()     # default syntax to close down the application 


# Importing the OpenCV library
import cv2
import time

# Initializing video
video = cv2.VideoCapture(0)

# Creating a CascadeClassifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize the flag variable
flag = 1

while True:
    flag+=1
    check, frame = video.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Search co-ordinates of face
    faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow('Capturing', frame)
    # Waiting for 1ms
    key = cv2.waitKey(1)
    # Break if user presses quit
    if(key==ord('q')):
        break

print(flag)

video.release()

cv2.destroyAllWindows()
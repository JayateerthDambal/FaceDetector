import cv2
import numpy as np 
import sys


def face_detector():
    cascadePath = 'N:/Tech Fandome/2-DayBootCamp/FaceDetector/haarcascade_frontalface_default.xml'
    faceCascade = cv2.CascadeClassifier(cascadePath)

    vid_Cap = cv2.VideoCapture(0)


    while True:
        ret, frame = vid_Cap.read()
        grayScaleImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            grayScaleImg, scaleFactor=1.5, minNeighbors=5,
            minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE  
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y),
                (x+w, y+h), (255,200,125),
                2
            )

        cv2.imshow("Face Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid_Cap.release()
    cv2.destroyAllWindows()        



if __name__ == '__main__':
    face_detector()
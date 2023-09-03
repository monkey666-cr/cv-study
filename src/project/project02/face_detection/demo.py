"""
视频流检测人脸
"""
import os
import cv2
import numpy as np

cap = cv2.VideoCapture(0)


class FaceDetection:
    def __init__(self):
        model_file = os.path.join(os.path.dirname(__file__), "cascades", "haarcascade_frontalface_default.xml")
        self.haar_face_detector = cv2.CascadeClassifier(model_file)

    def detect(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detections = self.haar_face_detector.detectMultiScale(frame_gray, minNeighbors=7)

        for (x, y, w, h) in detections:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)

        return frame


face_detection = FaceDetection()

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    frame = face_detection.detect(frame)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

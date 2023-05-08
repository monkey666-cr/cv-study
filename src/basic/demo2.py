"""
openCV 读取视频文件
"""
import os
import time

import cv2
import numpy as np

video_file_path = os.path.join(os.path.dirname(__file__), "video", "demo1.mp4")


cap = cv2.VideoCapture(video_file_path)
if not cap.isOpened():
    raise Exception("视频文件不存在或者编码错误")

while cap.isOpened():
    # 读取每一帧
    ret, frame = cap.read()
    
    if not ret:
        break

    cv2.imshow("Demo", frame)
    time.sleep(0.01)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

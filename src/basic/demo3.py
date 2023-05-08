"""
OpenCV在摄像头视频流上添加文字和图形
"""
import time

import cv2

from utils import draw

# 读取摄像头
cap = cv2.VideoCapture(0)

start_timestamp = time.time()

while True:
    # 读取每一帧
    ret, frame = cap.read()

    # 对frame进行操作
    frame = cv2.flip(frame, 1)

    # 画一个矩形
    cv2.rectangle(frame, (20, 200), (120, 300), (255, 0, 255), 10)

    # 计算帧率
    fps = int(1 / (time.time() - start_timestamp))

    frame_text = f"帧率: {str(fps)}"

    frame = draw.cv2AddChineseText(frame, frame_text, (20, 50), (0, 255, 0), 30)

    start_timestamp = time.time()

    cv2.imshow("Demo3", frame)

    # 退出条件
    if cv2.waitKey(10) & 0xFF == 27:
        break


cap.release()
"""
opencv读取摄像头视频流, 并且显示
保存为mp4
"""

import os
import cv2
import numpy as np

# 调用摄像头
cap = cv2.VideoCapture(0)

# DIVX, X264
fourcc = cv2.VideoWriter_fourcc(*'X264')
fps = 20

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_path = os.path.join(os.path.dirname(__file__), "video", "demo1.mp4")
writer = cv2.VideoWriter(video_path, fourcc, fps, (width, height))

while True:
    # 返回frame
    rec, frame = cap.read()

    # 镜像
    frame = cv2.flip(frame, 1)

    # 灰度显示
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 画面写入视频
    writer.write(frame)

    # 显示画面
    cv2.imshow("Demo1", frame)
    
    # ESC 退出
    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()

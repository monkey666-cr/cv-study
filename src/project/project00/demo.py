"""
步骤:
1, OpenCV获取视频流
2, 在画面上画一个方块
3, 通过mediapipe获取手指关键点坐标
4, 判断手指是否在方块上
5, 如果在方块上, 方块跟着手指移动
"""
import os
import math

import cv2

import mediapipe as mp

from utils.video import save_video

RED = (0, 255, 0)
BLUE = (255, 0, 255)



def virtual_drag():
    # 初始化方块坐标位置
    square_x, square_y, square_length = 100, 100, 100

    # 方块颜色
    square_color = BLUE

    # mediapipe相关参数
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    # 获取摄像头
    cap = cv2.VideoCapture(0)

    # 获取画面的长度和宽度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 是否在方块上, 是否更新方块坐标
    on_square = False
    # 手指坐标在方块的的坐标差
    L1, L2 = 0, 0

    # 保存视频路径
    video_path = os.path.join(os.path.dirname(__file__), "VirtualDrag.mp4")

    with save_video(video_path, video_width=width, video_height=height) as writer:
        with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as hands:

            while True:
                ret, frame = cap.read()

                frame = cv2.flip(frame, 1)

                # mediapipe 处理
                frame.flags.writeable = False
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(frame)

                # 还原颜色
                frame.flags.writeable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # 标记关键点
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )

                    # 保存21个关键点
                    x_list  = []
                    y_list = []

                    for item in hand_landmarks.landmark:
                        x_list.append(int(item.x * width))
                        y_list.append(int(item.y * height))

                    # 食指的坐标
                    index_finger_x = x_list[8]
                    index_finger_y = y_list[8]

                    # 中指的坐标
                    middle_finger_x = x_list[12]
                    middle_finger_y = y_list[12]

                    finger_distance = math.hypot((middle_finger_x - index_finger_x), (middle_finger_y - index_finger_y))

                    if finger_distance >= 60:
                        on_square = False

                        square_color = BLUE
                    else:
                        # 判断坐标是否在方块上 并且 当手指距离小于30的时候更新拖拽状态
                        if (
                            (
                                index_finger_x > square_x
                                and
                                index_finger_x < (square_x + square_length)
                            )
                            and
                            (
                                index_finger_y > square_y
                                and 
                                index_finger_y < (square_y + square_length)
                            )
                            and
                            finger_distance < 60 
                        ):
                            if not on_square:
                                on_square = True
                                
                                L1 = index_finger_x - square_x
                                L2 = index_finger_y - square_y

                                square_color = RED

                    if on_square:
                        # 跟新方块坐标
                        square_x = index_finger_x - L1
                        square_y = index_finger_y - L2

                    # 标记坐标
                    # cv2.circle(frame, (index_finger_x, index_finger_y), 20, (255, 0, 255), -1)

                # 画一个实心方块
                # cv2.rectangle(frame, (square_x, square_y), (square_x + square_length, square_y + square_length), (255, 0, 0), -1)

                # 半透明处理
                overlay = frame.copy()
                cv2.rectangle(frame,(square_x, square_y),(square_x + square_length, square_y + square_length), square_color, -1)
                frame = cv2.addWeighted(overlay, 0.5, frame, 1 - 0.5, 0)

                # 写入视频, 发微信装逼用
                writer.write(frame)

                cv2.imshow("Virtual Drag", frame)

                if cv2.waitKey(10) & 0xFF == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    virtual_drag()

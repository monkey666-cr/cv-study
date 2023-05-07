"""
opencv 展示图片
"""

import cv2

# 读取图片
img = cv2.imread("./img/cat/jpg")


while True:
    # 展示图片
    cv2.imshow("Demo", img)

    # 等待至少10ms, 并且用户按了ESC键
    if cv2.waitKey(10) & 0xFF == 27:
        break

# 关闭所有窗口
cv2.destroyAllWindows()

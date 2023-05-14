import cv2
import numpy as np


def read_image(file_path: str):
    """
    解决cv2读取中文路径失败的问题
    """
    raw_data = np.fromfile(file_path, dtype=np.uint8)
    img = cv2.imdecode(raw_data, -1)

    return img
import os
import cv2
import numpy as np

from PIL import Image, ImageDraw, ImageFont


def cv2AddChineseText(img, text, position, color=(0, 255, 0), thickness=10):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    draw = ImageDraw.Draw(img)

    font_path = os.path.join(os.path.dirname(__file__), "font", "simsun.ttc")
    font_style = ImageFont.truetype(font_path, thickness, encoding="utf-8")

    draw.text(position, text, color, font=font_style)

    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

import contextlib

import cv2

@contextlib.contextmanager
def save_video(video_path: str, video_width, video_height, fps=20):
    # DIVX, X264
    fourcc = cv2.VideoWriter_fourcc(*'X264')

    writer = cv2.VideoWriter(video_path, fourcc, fps, (video_width, video_height))

    yield writer

    writer.release()
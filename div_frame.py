import cv2
import os

path = "pic/"


# 将视频按帧抽取出图像
def div(path_video):
    cap = cv2.VideoCapture(path_video)

    def save_image(image, addr, num):
        address = addr + str(num) + '.jpg'
        cv2.imwrite(address, image)

    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

    success, frame = cap.read()
    i = 0

    while success:
        i = i + 1
        save_image(frame, path, i)
        print("已抽取:" + str(i))
        success, frame = cap.read()

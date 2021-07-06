from div_frame import div, path
from threshold_ import grey
from re_video import remake
import cv2
import os


def save_image(image, addr):
    address = addr
    cv2.imwrite(address, image)


def change(img_path):
    ig = grey(img_path)

    def num(m, n):
        count_pix = 0
        for ii in range(0, 4):
            for jj in range(0, 4):
                if ig[4 * m + ii, 4 * n + jj] <= 10:
                    count_pix = count_pix + 1
        return count_pix

    def draw_black(m, n):
        for ii in range(0, 4):
            for jj in range(0, 4):
                ig[4 * m + ii, 4 * n + jj] = 255
        for ii in range(1, 3):
            for jj in range(1, 3):
                ig[4 * m + ii, 4 * n + jj] = 0

    def draw_white(m, n):
        for ii in range(0, 4):
            for jj in range(0, 4):
                ig[4 * m + ii, 4 * n + jj] = 255

    for j in range(0, 360):
        for i in range(0, 270):
            if num(i, j) >= 8:
                draw_black(i, j)
            else:
                draw_white(i, j)
    return ig


if __name__ == "__main__":
    path_video = "bad apple.mp4"
    print("————开始抽取视频帧————")
    div(path_video)
    print("————视频帧抽取完毕————")
    file_list = os.listdir(path)
    file_list.sort(key=lambda x: int(x[:-4]))
    print("————开始转换帧图像————")
    for file in file_list:
        file_path = path + file
        print("已转换：" + file_path)
        save_image(change(file_path), file_path)
    print("————帧图像转换完毕————")
    print("————开始制作视频————")
    remake(path, "BadApple", 30, 1440, 1080)

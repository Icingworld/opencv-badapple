import cv2


# 图像灰度化、二值化
def grey(path):
    img = cv2.imread(path)
    e1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(e1, 100, 255, cv2.THRESH_BINARY)
    return thr

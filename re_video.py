import os
import cv2


# 将图像按帧重新制作成视频
def remake(path_pic, name, fps, a, b):
    file_list = os.listdir(path_pic)
    # 列表排序
    file_list.sort(key=lambda x: int(x[:-4]))

    count = 0
    size = (a, b)
    # 可以使用cv2.resize()进行修改

    video = cv2.VideoWriter(name + ".avi", cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), fps, size)

    for item in file_list:
        count = count + 1
        item = path_pic + item
        img = cv2.imread(item)
        video.write(img)
        print("已加载: " + str(count))

    video.release()
    cv2.destroyAllWindows()

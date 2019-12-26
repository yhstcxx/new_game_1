import numpy as np
import cv2

#转灰度图

def otsu_threshold(im):
    width, height = [640,480]
    pixel_counts = np.zeros(256)
    for x in range(width):
        for y in range(height):
            pixel = im[y][x]
            pixel_counts[pixel] = pixel_counts[pixel] + 1
    # 得到图片的以0-255索引的像素值个数列表
    s_max = (0, -10)
    for threshold in range(256):
        # 遍历所有阈值，根据公式挑选出最好的
        # 更新
        w_0 = sum(pixel_counts[:threshold])  # 得到阈值以下像素个数
        w_1 = sum(pixel_counts[threshold:])  # 得到阈值以上像素个数

        # 得到阈值下所有像素的平均灰度
        u_0 = sum([i * pixel_counts[i] for i in range(0, threshold)]) / w_0 if w_0 > 0 else 0

        # 得到阈值上所有像素的平均灰度
        u_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0

        # 总平均灰度
        u = w_0 * u_0 + w_1 * u_1

        # 类间方差
        g = w_0 * (u_0 - u) * (u_0 - u) + w_1 * (u_1 - u) * (u_1 - u)

        # 类间方差等价公式
        # g = w_0 * w_1 * (u_0 * u_1) * (u_0 * u_1)

        # 取最大的
        if g > s_max[1]:
            s_max = (threshold, g)
        print(s_max)
    return s_max[0]
fname = r"C:\Users\yhstc\Desktop\untitled4 (2)\zanshi\0002.bmp"
img = cv2.imread(fname)
img = cv2.resize(img, (640,480), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
a = otsu_threshold(gray)
print(a)
ret, binary = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)  # 前面哪个是阈值，后面的是设定值

cv2.imshow("binary",binary)
cv2.imshow("gray",gray)
cv2.waitKey(0)
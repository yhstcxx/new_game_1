import cv2
import numpy as np

#阈值设置后，高斯降噪，中值滤波等，然后再改

#阈值设置成10就行了，其他不用管

def img_binary(gray,lenth,wedth):
    # frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
    # # 二值化
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(gray.shape)



    s_max = (10, -10)

    # # ostu算法,可以用来分层计算
    # pixel_counts = np.zeros(256)
    # for x in range(lenth):
    #     for y in range(wedth):
    #         pixel = gray[y][x]
    #         pixel_counts[pixel] = pixel_counts[pixel] + 1
    # # 得到图片的以0-255索引的像素值个数列表
    #
    # for threshold in range(256):
    #     # 遍历所有阈值，根据公式挑选出最好的
    #     # 更新
    #     w_0 = sum(pixel_counts[:threshold])  # 得到阈值以下像素个数
    #     w_1 = sum(pixel_counts[threshold:])  # 得到阈值以上像素个数
    #
    #     # 得到阈值下所有像素的平均灰度
    #     u_0 = sum([i * pixel_counts[i] for i in range(0, threshold)]) / w_0 if w_0 > 0 else 0
    #
    #     # 得到阈值上所有像素的平均灰度
    #     u_1 = sum([i * pixel_counts[i] for i in range(threshold, 256)]) / w_1 if w_1 > 0 else 0
    #
    #     # 总平均灰度
    #     u = w_0 * u_0 + w_1 * u_1
    #
    #     # 类间方差
    #     g = w_0 * (u_0 - u) * (u_0 - u) + w_1 * (u_1 - u) * (u_1 - u)
    #
    #     # 类间方差等价公式
    #     # g = w_0 * w_1 * (u_0 * u_1) * (u_0 * u_1)
    #
    #     # 取最大的
    #     if g > s_max[1]:
    #         s_max = (threshold, g)
    #     # print(s_max)
    ret, binary = cv2.threshold(gray, s_max[0], 255, cv2.THRESH_BINARY)  # 前面哪个是阈值，后面的是设定值

    #
    # cv2.imshow("binary",binary)
    # cv2.imshow("gray",gray)
    def erode(binary):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))
        dst = cv2.erode(binary,kernel)
        # cv2.imshow("erode",dst)
        return dst
    def dilate(binary):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(13,13))
        dst = cv2.dilate(binary,kernel)
        # cv2.imshow("dilate",dst)
        return dst

    dst_dilate = dilate(binary)
    erode = erode(dst_dilate)

    for i in range(lenth):
        list = []
        for j in range(wedth):
            # print(binary[j][i])
            if  binary[j][i]:
                list.append(j)
        #         print("yes")
        # print(list)
        for j in range(wedth):
            try:
                if (list[0]<j<list[-1]) and (not binary[j][i]):
                    binary[j][i] = erode[j][i]
            except:
                pass
    #
    # cv2.imshow("finall",binary)
    # #
    cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return binary
# frame = cv2.imread(r"C:\Users\yhstc\Desktop\shiyan\shiyan-1-\3\0002.bmp")
# frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
# # 二值化
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# img_binary(gray,640,480)
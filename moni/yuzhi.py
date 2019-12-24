import cv2
import numpy as np

#阈值设置后，高斯降噪，中值滤波等，然后再改

#阈值设置成10就行了，其他不用管

def img_binary(gray,lenth,wedth):
    # frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
    # # 二值化
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # print(gray.shape)
    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)# 前面哪个是阈值，后面的是设定值

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
                if list[0]<j<list[-1]:
                    binary[j][i] = erode[j][i]
            except:
                pass

    # cv2.imshow("finall",binary)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return binary
# frame = cv2.imread(r"E:\shiyan\shiyan-1-2kw\3\0305.bmp")
# frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
# # 二值化
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# img_binary(gray,640,480)
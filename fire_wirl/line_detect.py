import cv2 as cv
import numpy as np
from moni import yuzhi
import glob,os
import csv
wedth = 480
lenth =640

# f_1 = open("遮挡.csv","a")#,"a", newline='')
# f_1 = csv.writer(f_1)
# # f = open(r'E:\shiyan\volume_.csv', "r").readlines()

def line_detection(image,name):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, gray = cv.threshold(gray,30, 255, cv.THRESH_BINARY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)
    try :
        lines.shape
        print(name,"存在")
        return
    except:
        print(name,"不存在")
        return
    for line in lines:
        print(type(lines))
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image-lines", image)
def line_detect_possible_demo(image,name):

    # print(gray)
    #
    # gray = yuzhi.img_binary(gray, lenth, wedth)
    # # print(gray.shape)
    # # exit()
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    # gray = cv.resize(gray, (lenth, wedth), interpolation=cv.INTER_AREA)
    # cv.imshow("image-ines", gray)
    # cv.waitKey(0)
    ret, gray = cv.threshold(gray,1, 255, cv.THRESH_BINARY)

    kernel = cv.getStructuringElement(cv.MORPH_RECT,(13,13))
    gray = cv.erode(gray,kernel)
    gray = cv.dilate(gray,kernel)

    # # print(gray.shape)
    # # exit()
    # gray = yuzhi.img_binary(gray, gray.shape[1], gray.shape[0])
    edges = cv.Canny(gray, 50, 150, apertureSize=3)

    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=1, maxLineGap=500)
    # edges = cv.resize(edges, (lenth, wedth), interpolation=cv.INTER_AREA)
    # gray = cv.resize(gray, (lenth, wedth), interpolation=cv.INTER_AREA)
    # cv.imshow("image-lines", edges)
    # cv.imshow("image-ines", gray)
    # cv.waitKey(0)

    # print("lines",lines[0])
    # exit()

    try :
        lines.shape
        print(name,"存在")
        return
    except:
        print(name,"不存在")
        return
    try:
        lin = lines.reshape(lines.shape[0], 4)
        a = (np.max(lin,axis=0)-np.min(lin,axis=0))<50
        if a[0] and a[1]and a[2] and a[3]:
            #删除数组多行
            lines = np.delete(lines,[1,lines.shape[0]-1], axis=0)
            print(name, "存在")
            return
        else:
            print(name, "不存在")
            return
    except:
        print(name, "不存在")
        return

    # lin = np.array(line[0])
    print("lines", len(lines))

    # for line in lines:
    #     print(type(line))
    #     x1, y1, x2, y2 = line[0]
    #     cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #     print(line[0])
        # cv.imshow("line_detect_possible_demo", image)
        # cv.waitKey(0)
        # exit()
    # image = cv.resize(image, (lenth,wedth), interpolation=cv.INTER_AREA)
    # cv.imshow("line_detect_possible_demo", image)


print("--------- Python OpenCV Tutorial ---------")
all_files = glob.glob(os.path.join(r"C:\Users\yhstc\Documents\Tencent Files\648810974\FileRecv\8kw 1.4\8kw 1.4","*.jpg"))
for src in all_files:
    img = cv.imread(src)
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
#     line_detection(img,os.path.basename(src))
# cv.waitKey(0)
    line_detect_possible_demo(img,os.path.basename(src))
# cv.waitKey(0)
#
# cv.destroyAllWindows()
# import cv2 as cv
# import numpy as np

#
# def line_detection(image):
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     edges = cv.Canny(gray, 50, 150, apertureSize=3)
#     lines = cv.HoughLines(edges, 1, np.pi/180, 200)
#     for line in lines:
#         print(type(lines))
#         rho, theta = line[0]
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0+1000*(-b))
#         y1 = int(y0+1000*(a))
#         x2 = int(x0-1000*(-b))
#         y2 = int(y0-1000*(a))
#         cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     cv.imshow("image-lines", image)
#
#
# def line_detect_possible_demo(image):
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     edges = cv.Canny(gray, 50, 150, apertureSize=3)
#     lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=40, maxLineGap=100)
#     for line in lines:
#         print(type(line))
#         x1, y1, x2, y2 = line[0]
#         cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#     image = cv.resize(image, (lenth, wedth), interpolation=cv.INTER_AREA)
#     cv.imshow("line_detect_possible_demo", image)
#
#
# print("--------- Python OpenCV Tutorial ---------")
# src = cv.imread(r"C:\Users\yhstc\Desktop\untitled4\mianji\2511387.jpg")
# # cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# #
# # cv.imshow("input image", src)
# line_detect_possible_demo(src)
# cv.waitKey(0)
#
# cv.destroyAllWindows()

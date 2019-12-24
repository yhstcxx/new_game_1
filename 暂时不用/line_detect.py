import cv2 as cv
import numpy as np
from moni import yuzhi
import glob,os
import csv
wedth = 480
lenth =640

f_1 = open("obstract.csv","a",newline='')
f_1 = csv.writer(f_1)

f_1.writerow(['name','是否存在'])
#检测是否存在直线
# 进度
progress_bar = 0
num_oneh =0
def line_detct_possible_demo(image, name):
    #二值化+腐蚀+膨胀
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    # ret, gray = cv.threshold(gray,30, 255, cv.THRESH_BINARY)
    # kernel = cv.getStructuringElement(cv.MORPH_RECT,(13,13))
    # gray = cv.erode(gray,kernel)
    # gray = cv.dilate(gray,kernel)

    # # print(gray.shape)
    # # exit()
    # gray = yuzhi.img_binary(gray, gray.shape[1], gray.shape[0])
    #canny边缘检测
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    #霍夫直线检测
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=70, maxLineGap=1)
    edges = cv.resize(edges, (lenth, wedth), interpolation=cv.INTER_AREA)
    gray = cv.resize(gray, (lenth, wedth), interpolation=cv.INTER_AREA)
    # cv.imshow("image-lines", edges)
    # cv.imshow("image-ines", gray)
    # cv.waitKey(0)

    # print("lines",lines[0])
    # exit()



    # for line in lines:
    #     print(type(line))
    #     x1, y1, x2, y2 = line[0]
    #     cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #     print(line[0])
    #     image = cv.resize(image, (lenth, wedth), interpolation=cv.INTER_AREA)
    #     cv.imshow("line_detect_possible_demo", image)
    #     cv.waitKey(0)
    #     exit()

    try :
        lines.shape
        print(name,"存在")
        f_1.writerow([name,"存在"])
        return
    except:
        print(name,"不存在")
        f_1.writerow([name, "不存在"])
        return

    # try:
    #     lin = lines.reshape(lines.shape[0], 4)
    #     a = (np.max(lin,axis=0)-np.min(lin,axis=0))<50
    #     if a[0] and a[1]and a[2] and a[3]:
    #         #删除数组多行
    #         lines = np.delete(lines,[1,lines.shape[0]-1], axis=0)
    #         print(name, "存在")
    #         return
    #     else:
    #         print(name, "不存在")
    #         return
    # except:
    #     print(name, "不存在")
    #     return

    # lin = np.array(line[0])
    # print("lines", len(lines))




print("--------- Python OpenCV line_detect ---------")
all_files = glob.glob(os.path.join(r"F:\shiyan\fire_wirl\7.0kw_00_38.85rpm_7\1","*.bmp"))
for src in all_files:
    progress_bar +=1
    img = cv.imread(src)
    if progress_bar%100==0:
        num_oneh+=1
        print(num_oneh,"/",len(all_files)/100)

# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
#     line_detection(img,os.path.basename(src))
# cv.waitKey(0)
    line_detct_possible_demo(img,src)
# cv.waitKey(0)

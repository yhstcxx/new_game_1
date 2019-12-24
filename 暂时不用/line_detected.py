import csv

import cv2
import numpy as np
import pandas as pd

from moni import png_dir
from moni import zu_dir

#
# progress_bar = 0
# num_oneh = 0


drc=4
path = r"F:\shiyan\fire_wirl"



#1.实验组数 2.方向数，3.照片编号
#标定图片，返回相机序（方向）号及对应内外惨----2
zu_path=r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"
#实验组的路径和名字
print(zu_path)
zu_all,zu_name = zu_dir.fenzu(zu_path,"rpm")

print(zu_path)

#循环组
for num_zu in range(len(zu_all)):


    # 保存数组，保存的坐标值及对应亮度，二值化----1，3
    path_01 = r"{}\point".format(zu_all[num_zu])

    # 保存体积、面积，每组实验随时间变化----1，3
    path_02 = zu_all[num_zu]

    # 实验图片。返回相机序号+图片（字典类型)（方向）---2，3
    path_03 = zu_all[num_zu]
    image_1 = png_dir.DFS_file_range(path_03,drc-1)

    f_1 = open(path_02 + "\\" + 'lindetect' + ".csv", "a", newline='')
    f_1_close = f_1
    f_1 = csv.writer(f_1)

    f_1.writerow(['name', '是否存在'])
    # 检测是否存在直线
    # 进度


    #深度循环，不是广度
    for drc_num in range(1,drc):#方向数循环
        num_pic = 1
        for pic in image_1[drc_num]:#循环图片
            frame = cv2.imread(pic)
            # 二值化+腐蚀+膨胀
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 阈值
            ret, gray = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
            # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 13))
            # gray = cv2.erode(gray, kernel)
            # gray = cv2.dilate(gray, kernel)

            edges = cv2.Canny(gray, 50, 150, apertureSize=3)
            # 霍夫直线检测
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=1, maxLineGap=500)
            # wedth = 480
            # lenth = 640
            # edges = cv2.resize(edges, (lenth, wedth), interpolation=cv2.INTER_AREA)
            # gray = cv2.resize(gray, (lenth, wedth), interpolation=cv2.INTER_AREA)
            # cv2.imshow("image-lines", edges)
            # cv2.imshow("image-ines", gray)
            # cv2.waitKey(0)
            try:
                lines.shape
                # f_1.writerow([pic, "存在"])
                f_1.writerow([pic,num_pic ,"存在"])
                num_pic+=1
                # for line in lines:
                #     print(type(line))
                #     x1, y1, x2, y2 = line[0]
                #     cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                #     print(line[0])
                #     cv2.imshow("line_detect_possible_demo", image)
                #     cv2.waitKey(0)
                #     exit()
                # image = cv2.resize(image, (lenth, wedth), interpolation=cv2.INTER_AREA)
                # cv2.imshow("line_detect_possible_demo", image)
            except:
                # f_1.writerow([pic,"不存在"])
                f_1.writerow([pic,num_pic,"不存在"])
                num_pic += 1
    try:
        # 对数据进行筛选，让它更有规律（已知存在规律的情况下）
        a = pd.read_csv(path_02 + "\\" + 'lindetect' + ".csv", encoding='gbk')
        a = np.array(a)
        # print(a.shape)
        # exit()
        # f.close
        num = 0
        while 1:
            for i in range(len(a) - 2):
                if a[i][2] == a[i + 2][2] and a[i][2] != a[i + 1][2]:
                    a[i + 1][2] = a[i][2]
            for i in range(len(a) - 5):
                if a[i][2] == a[i + 5][2] and a[i + 1][2] == a[i + 4][2] and a[i + 2][2] == a[i + 3][2] and a[i + 1][2] != \
                        a[i + 2][2]:
                    a[i + 2][2] = a[i + 3][2] = a[i + 1][2]
            for i in range(len(a) - 8):
                if a[i][2] == a[i + 8][2] and a[i + 1][2] == a[i + 7][2] and a[i + 2][2] == a[i + 6][2] and a[i + 3][2] == \
                        a[i + 4][
                            2] == a[i + 5][2] and a[i + 3][2] != a[i][2]:
                    a[i + 3][2] = a[i + 4][2] = a[i + 5][2] = a[i][2]
            for i in range(len(a) - 9):
                if a[i][2] == a[i + 9][2] and a[i + 1][2] == a[i + 8][2] and a[i + 2][2] == a[i + 7][2] and a[i + 3][2] == \
                        a[i + 4][
                            2] == a[i + 5][2] == a[i + 6][2] and a[i + 3][2] != a[i][2]:
                    a[i + 3][2] = a[i + 4][2] = a[i + 5][2] = a[i + 6][2] = a[i][2]
            num += 1
            if num == 2:
                break
        # print(a[0][1]=='不存在')
        num_len = 0
        count_begin = False
        obstract_may = []
        # 计算存在的个数，对应的开始点
        for i in range(len(a)):
            if count_begin:
                if a[i][2] == '存在':
                    num_len += 1
                else:
                    count_begin = False
                    obstract_may.append(num_len)
                    num_len = 0
            else:
                if a[i][2] == '存在':
                    count_begin = True
                    num_len += 1
                    # 初始化字典
                    obstract_may.append(a[i][0])
                    obstract_may.append(a[i][1])
                else:
                    pass
        obstract_may = np.array(obstract_may).reshape(-1, 3)
        print(obstract_may)

        # 验证准确性
        deta = []
        for i in range(len(obstract_may)):
            if 0 < i < len(obstract_may) - 1:
                deta.append(int(obstract_may[i + 1][1]) - int(obstract_may[i][1]))
        deta = np.array(deta).reshape(-1, 1)

        obstract_may = np.column_stack((obstract_may, deta))

        obstract_may = pd.DataFrame(obstract_may)
        obstract_may.to_csv(path_02 + "\\" +'obstract_may.csv', encoding='gbk')

        data1 = pd.DataFrame(a)
        data1.to_csv(path_02 + "\\" +'obstract_modify.csv', encoding='gbk')
    except:
        pass


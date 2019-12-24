import cv2
import numpy as np
import pandas as pd
import glob,os
import csv
from moni import zu_dir
from moni import png_dir

wedth = 120
lenth = 160

drc=4
path = r"F:\shiyan\fire_wirl"


#1.实验组数 2.方向数，3.照片编号

#组所在文件夹
zu_path=r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"

#实验组的路径和名字
zu_all,zu_name = zu_dir.fenzu(zu_path,"14.6rpm")

class cal_area:
    def begin(self):
        #循环组
        for num_zu in range(len(zu_all)):

            # 组路径，保存体积、面积，每组实验随时间变化----1，3
            path_02 = zu_all[num_zu]

            #组路径内图片
            image_1 = png_dir.DFS_file_range(path_02,drc-1)

            #方向数循环
            for drc_num in range(1,drc):
                #保存面积
                f_1 = open(path_02 + "\\" + 'area_detect' + ".csv", "a", newline='')
                f_1_close = f_1
                f_1 = csv.writer(f_1)
                f_1.writerow(['dizhi', "xuhao"])
                area = []
                for src in image_1[drc_num]:#循环图片

                    img = cv2.imread(src)
                    try:
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    except:
                        continue
                    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
                    binary = cv2.resize(binary, (lenth, wedth), interpolation=cv2.INTER_AREA)
                    binary_size = binary.shape[::-1]
                    numi = 0
                    for i in range(binary_size[0]):  # 0-320
                        for j in range(binary_size[1]):  # 0-240
                            if binary[j][i]:  # 白色（火焰），1，注意bug，颜色
                                numi += 1
                    area.append(numi)
                #面积转数组
                area=np.array(area)
                area = np.mean(area) / 2
                    # 遍历图片,筛选面积小于1/2平均值的
                for src in image_1[drc_num]:

                    img = cv2.imread(src)
                    try:
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    except:
                        continue
                    ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
                    binary = cv2.resize(binary, (lenth, wedth), interpolation=cv2.INTER_AREA)
                    binary_size = binary.shape[::-1]
                    numi = 0
                    # cv2.imshow("line_detect_possible_demo", binary)
                    # cv2.waitKey(0)
                    for i in range(binary_size[0]):  # 0-640
                        for j in range(binary_size[1]):  # 0-480
                            if binary[j][i]:  # 白色（火焰），1，注意bug，颜色
                                numi += 1
                    #筛选面积不符合的图片
                    if numi < area:
                        # 文件地址、文件序号
                        f_1.writerow([src, src.split("\\")[-1].split(".")[0]])
                f_1_close.close()

                # 文件地址、文件序号
                a = pd.read_csv(path_02 + "\\" + "area_detect.csv", encoding='gbk')
                a = np.array(a)

                # 文件地址
                obstract_begin = []

                # 计算存在的个数，对应的开始点
                for i in range(1, len(a)):
                    if i == 1:
                        obstract_begin.append(a[i][0])
                        obstract_begin.append(a[i][1])
                    else:
                        if int(a[i][1]) - int(a[i - 1][1]) != 1:
                            obstract_begin.append(a[i][0])
                            obstract_begin.append(a[i][1])
                #文件地址，文件序号
                obstract_begin = np.array(obstract_begin).reshape(-1, 2)
                obstract_begin = pd.DataFrame(obstract_begin)
                obstract_begin.to_csv(path_02 + "\\" +'obstract_begin_%d.csv'%drc_num, encoding='gbk')
                os.remove(path_02 + "\\" +"area_detect.csv")
cal_area().begin()


import cv2
import numpy as np
import pandas as pd
import glob,os
import csv
from moni import zu_dir
import matplotlib.pyplot as plt
from moni import png_dir
#空格：确认，esc返回，1：前进10张，2：后退10张，+：后退一张 -：前进一张；
#正确步骤：找到图片————空格————，点错即返回

wedth = 240
lenth = 320
#方向数
drc=4
#组所在文件夹
path = r"F:\shiyan\fire_wirl"

#1.实验组数 2.方向数，3.照片编号
#组所在文件夹
zu_path=r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"

#实验组的路径和名字
zu_all,zu_name = zu_dir.fenzu(zu_path,"rpm")




class save_pic_num:
    def begin(self):
        # 循环组
        for num_zu in range(len(zu_all)):
            pic_all = []
            # 组路径，保存体积、面积，每组实验随时间变化----1，3
            path_02 = zu_all[num_zu]

            #组路径内图片
            image_1 = png_dir.DFS_file_range(path_02,drc-1)

            #方向数循环
            hav_pic = True
            for drc_num in range(1,drc):
                try:
                    a = pd.read_csv(path_02 + "\\" +"obstract_begin_%d.csv"%drc_num, encoding='gbk')
                    a = np.array(a)
                except:
                    hav_pic=False
                    break
                delect_1=[]
                #索引，地址，图片索引+1
                image_1 = png_dir.DFS_file_range(path_02, drc - 1)
                pic_range_all = []
                # 取出地址和图片索引
                for i,j,k in a:
                    delect_1.append([j,k])

                #地址和索引
                for img,index in delect_1:

                    try:
                        # 尝试索引是不是再上次添加的索引内
                        if pic_range_all[-1][0]<index<pic_range_all[-1][1]:
                            continue
                    except:
                        pass
                    # 显示索引内图片
                    # print(img)
                    image = cv2.imread(img)
                    image = cv2.resize(image, (lenth, wedth), interpolation=cv2.INTER_AREA)
                    # print(image)
                    cv2.imshow(str(index), image)
                    cv2.moveWindow(str(index), 500, 200)
                    keyboard = cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    # 储存起始位置
                    pic_range=[]
                    # 等待输入遮挡的起始位置
                    while keyboard !=27:#esc:
                        print(keyboard)
                        def pic_imshow(index):
                            image = cv2.imread(image_1[drc_num][index - 1])
                            image = cv2.resize(image, (lenth, wedth), interpolation=cv2.INTER_AREA)
                            cv2.imshow(str(index), image)
                            cv2.moveWindow(str(index), 500, 200)
                            keyboard = cv2.waitKey(0)
                            cv2.destroyAllWindows()
                            return keyboard
                        if keyboard == 43:#+
                            index = index+1
                            #读取索引图片
                            try:
                                keyboard=pic_imshow(index)
                            except:
                                index = index - 1
                                keyboard=pic_imshow(index)
                        if keyboard == 45:#-
                            index = index-1
                            try:
                                keyboard=pic_imshow(index)
                            except:
                                index = index + 1
                                keyboard=pic_imshow(index)
                        if keyboard == 49:#1
                            index = index-10
                            try:
                                keyboard=pic_imshow(index)
                            except:
                                index = index + 10
                                keyboard=pic_imshow(index)
                        if keyboard == 50:#2
                            index = index+10
                            try:
                                keyboard=pic_imshow(index)
                            except:
                                index = index - 10
                                keyboard=pic_imshow(index)
                        if keyboard == 32:#空格
                            pic_range.append(index)
                            index = index
                            keyboard=pic_imshow(index)

                        if keyboard not in [32,50,49,45,43,27]:
                            keyboard=45


                    print(pic_range)
                    if pic_range:
                        pic_range_all.append(pic_range)
                    print(pic_range_all)
                #循环每个方向列表内图片
                for i in pic_range_all:
                    if len(i)!=2:
                        continue
                    for pic in range(i[0]-1,i[1]):
                        #把图片序号.bmp存入pic_all
                        pic_all.append(image_1[drc_num][pic].split("\\")[-1])
                print(pic_all)
            #删除储存的文件
            if hav_pic == True:
                for drc_num in range(1,drc):
                    os.remove(path_02 + "\\" +"obstract_begin_%d.csv"%drc_num)
                #去重
                pic_all = set(pic_all)
                #保存
                pic_all = pd.DataFrame(pic_all)
                pic_all.to_csv(path_02 + "\\" +'pic_all.csv', encoding='gbk')

class delect:
    def begin(self):
        # 循环组
        for num_zu in range(len(zu_all)):

            # 组路径，保存体积、面积，每组实验随时间变化----1，3
            path_02 = zu_all[num_zu]
            try:
                #读取路径
                pic_all = pd.read_csv(path_02 + "\\" +'pic_all.csv', encoding='gbk')
                pic_all = np.array(pic_all)[:,1]
            except:
                continue

            #方向路径，方向名
            drc_all, drc_name = zu_dir.fenzu(path_02, "")

            for drc_num in range(0, drc-1):  # 方向数循环
                for pic in pic_all:
                    #路径拼接方向，删除每个方向图片
                    print(drc_all[drc_num] + "\\" + str(pic))
                    # os.remove(drc_all[drc_num] + "\\" + str(pic))
class ignore:
    def __init__(self):
        self.area = []
    def begin(self):
        # 循环组
        for num_zu in range(len(zu_all)):

            # 组路径，保存体积、面积，每组实验随时间变化----1，3
            path_02 = zu_all[num_zu]
            try:
                #读取路径
                pic_all = pd.read_csv(path_02 + "\\" +'pic_all.csv', encoding='gbk')
                # pic_all = np.array(pic_all)[:,1]
                # 取图片索引
                x = np.array([int(i.split('.')[0]) for i in pic_all['0']])
            except:
                area = pd.read_csv(path_02 + "\\" + 'area_' + zu_name[num_zu] + '_1.csv', encoding='gbk')
                self.area.append(area['area_%s_1' % zu_name[num_zu]].mean(axis=0))
                continue

            #方向路径，方向名
            drc_all, drc_name = zu_dir.fenzu(path_02, "")
            try:
                area = pd.read_csv(path_02 + "\\" + 'area_' + zu_name[num_zu] + '_1.csv', encoding='gbk')
            except:
                continue

            # print(pic_all['0'],'pic_all')

            # print(x)
            # print(area)
            # print(area['index']-1)
            # print(~ area['index'].isin(x))

            #除去遮挡的平均值
            self.area.append(area['area_%s_1' % zu_name[num_zu]].loc[ ~(area['index'].isin(x))].mean(axis=0))
            # print(area['area_%s_1'%zu_name[num_zu]],"area")
            # for drc_num in range(0, drc-1):  # 方向数循环
            #     for pic in pic_all:
            #         #路径拼接方向，删除每个方向图片
            #         print(drc_all[drc_num] + "\\" + str(pic))
                    # os.remove(drc_all[drc_num] + "\\" + str(pic))
        # print(self.area)
        x = [int(i.split('_')[-1]) for i in zu_name]
        show ={}
        for i in range(len(x)):
            show[x[i]]=self.area[i]

        # print(show)
        #对y轴数据进行排序，我们根据文件夹遍历并不是按照转速进行的
        y_sort = []
        for i in range(len(x)):
            for j,k in show.items():
                if i==j:
                    y_sort.append(k)
        # 自定义 x轴 的取值：
        # colums_x = x
        colums_y = y_sort
        plt.xticks(range(len(x)))
        # 不要再写进 colums_x 了
        plt.plot(colums_y)

        plt.xlabel("x axis ")
        plt.ylabel("y axis ")
        plt.show()
ignore().begin()
# save_pic_num().begin()
# delect().begin()
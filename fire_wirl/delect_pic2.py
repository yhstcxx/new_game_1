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
import time




wedth = 480
lenth = 640
#方向数
drc=4
#组所在文件夹
path = r"G:\shiyan\fire_wirl_2"

#1.实验组数 2.方向数，3.照片编号
#组所在文件夹
zu_path=r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"

#实验组的路径和名字
power = 3.5
# zu_all,zu_name = zu_dir.fenzu(zu_path,"*%skw"%power)
zu_all,zu_name = zu_dir.fenzu(zu_path,"%skw"%power)



if power==3.5:
    hz=[0,0.9,1.8,2.1,2.5,4.0,5.0,8.9,11.9,13.2]
elif power==7.0:
    hz = [0,1.0,1.8,2.6,2.9,4.9,8.8,9.8,13.1,15.0]


class cal_area:
    def begin(self):
        #循环组
        for num_zu in range(len(zu_all)):

            # 组路径，保存体积、面积，每组实验随时间变化----1，3
            path_02 = zu_all[num_zu]

            #组路径内图片
            image_1 = png_dir.DFS_file_range(path_02,drc-1)
# jika
            try:#如果先计算了面积
                #读取面积文件
                path = path_02 + "\\" + "area_" + zu_name[num_zu] + ".xlsx"
                area = pd.read_excel(io=path)

                # 文件内不同sheet
                sheet_name = [x for x in range(3)]
                file = pd.read_excel(io=path, sheet_name=sheet_name)
                drc_num = 0  #方向方向
                #不同表格数据
                for i in file.values():
                    drc_num += 1
                    # 面积平均值
                    # 平均值注意亮光部分会识别成火焰,可能有bug
                    mean = i["area_" + zu_name[num_zu] + "_" + str(drc_num)].mean(axis=0)
                    min = i["area_" + zu_name[num_zu] + "_" + str(drc_num)].min(axis=0)
                    # i[i["area_" + zu_name[num_zu] + "_" + str(drc_num)] > mean].index
                    # 满足要求的列
                    pic_num = np.array(i[i["area_" + zu_name[num_zu] + "_" + str(drc_num)]-min <((mean-min)/2)].index)
                    # print(pic_num)

                    f_1 = open(path_02 + "\\" + "obstract_begin_%d.csv" % drc_num, "a", newline='')
                    f_1_close = f_1
                    f_1 = csv.writer(f_1)
                    for temp_num in pic_num:
                        src = image_1[drc_num][temp_num]
                        # print(src)
                        f_1.writerow([src,src.split("\\")[-1].split(".")[0]])
                    f_1_close.close()
                    time.sleep(1)
                    a = pd.read_csv(path_02 + "\\" + "obstract_begin_%d.csv" % drc_num, encoding='gbk')
                    a = np.array(a)
                    # print(a)
                    # exit()
                    # 文件地址
                    obstract_begin = []

                    # 计算存在的个数，对应的开始点
                    for i in range(0, len(a)):
                        if i == 0:
                            obstract_begin.append(a[i][0])
                            obstract_begin.append(a[i][1])
                        else:
                            if int(a[i][1]) - int(a[i - 1][1]) != 1:
                                obstract_begin.append(a[i][0])
                                obstract_begin.append(a[i][1])
                    # 文件地址，文件序号
                    obstract_begin = np.array(obstract_begin).reshape(-1, 2)
                    obstract_begin = pd.DataFrame(obstract_begin)
                    obstract_begin.to_csv(path_02 + "\\" + 'obstract_begin_%d.csv' % drc_num, encoding='gbk')
# jika
            except:#否则重新算面积
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
                    # if zu_name[num_zu] == "7.0kw_00_10.3rpm_4":
                    #     index = index-300
                    try:
                        # 尝试索引是不是再上次添加的索引内
                        if (pic_range_all[-1][0]<index<pic_range_all[-1][1])or(index<pic_range_all[-1][0]):
                            continue
                    except:
                        pass
                    # 显示索引内图片
                    # print(img)
                    image = cv2.imread(img)
                    image = cv2.resize(image, (lenth, wedth), interpolation=cv2.INTER_AREA)
                    # print(image)
                    cv2.imshow(str(index)+"--"+zu_name[num_zu]+"--"+str(drc_num), image)
                    cv2.moveWindow(str(index)+"--"+zu_name[num_zu]+"--"+str(drc_num), 200, 200)
                    keyboard = cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    # 储存起始位置
                    pic_range=[]
                    # 等待输入遮挡的起始位置
                    while keyboard !=27:#esc:
                        print(keyboard)

                        def pic_imshow(index):
                            # print(image_1[drc_num][index - 1])
                            image = cv2.imread(image_1[drc_num][index - 1])
                            image = cv2.resize(image, (lenth, wedth), interpolation=cv2.INTER_AREA)
                            cv2.imshow(str(index)+"--"+zu_name[num_zu]+"--"+str(drc_num), image)
                            cv2.moveWindow(str(index)+"--"+zu_name[num_zu]+"--"+str(drc_num), 200, 200)
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
class ignore:#忽略障碍物作图
    def __init__(self):
        #平均面积/体积
        # self.area = []
        self.volum = []

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
            #如果没有障碍物面积/体积直接取平均值
            except:
                # area = pd.read_csv(path_02 + "\\" + 'area_' + zu_name[num_zu] + '_1.csv', encoding='gbk')
                volum = pd.read_csv(path_02 + "\\" + 'volum_' + zu_name[num_zu] + '.csv', encoding='gbk')
                # self.area.append(area['area_%s_1' % zu_name[num_zu]].mean(axis=0))
                self.volum.append(volum['volum_%s' % zu_name[num_zu]].mean(axis=0))
                continue#大体积

            #方向路径，方向名
            drc_all, drc_name = zu_dir.fenzu(path_02, "")

            # 如果有障碍物
            try:
                # area = pd.read_csv(path_02 + "\\" + 'area_' + zu_name[num_zu] + '_1.csv', encoding='gbk')
                volum = pd.read_csv(path_02 + "\\" + 'volum_' + zu_name[num_zu] + '.csv', encoding='gbk')
            except:
                continue

            # print(pic_all['0'],'pic_all')

            # print(x)
            # print(area)
            # print(area['index']-1)
            # print(~ area['index'].isin(x))

            #除去遮挡的平均值
            # self.area.append(area['area_%s_1' % zu_name[num_zu]].loc[ ~(area['index'].isin(x))].mean(axis=0))
            self.volum.append(volum['volum_%s' % zu_name[num_zu]].loc[~(volum['index'].isin(x))].mean(axis=0))
            try:
                volum['volum_%s' % zu_name[num_zu]].loc[~(volum['index'].isin(x)).to_csv('%s.csv' %  zu_name[num_zu], encoding='gbk')]
            except:
                print(zu_name[num_zu])


            # print(area['area_%s_1'%zu_name[num_zu]],"area")
            # for drc_num in range(0, drc-1):  # 方向数循环
            #     for pic in pic_all:
            #         #路径拼接方向，删除每个方向图片
            #         print(drc_all[drc_num] + "\\" + str(pic))
                    # os.remove(drc_all[drc_num] + "\\" + str(pic))
        # print(self.area)


        #组序号
        x = [int(i.split('_')[-1]) for i in zu_name]
        #组序号对应面积/体积
        show ={}
        for i in range(len(x)):
            #面积
            # show[x[i]] = self.area[i]
            # show[x[i]self.area[i]/43660*729/100000
            # 变成火焰表面积,s/图像面积*真是面积*Π,注意图片是经过分辨率变换后得到的
            # show[x[i]] = power/((self.area[i] / 34302) * (7.29 / 1000)*np.pi)

            #power是功率,x[i]是序号
            show[x[i]] = [power / (self.volum[i]*(13.5**3)*(0.001**3)),zu_name[i]]
        # print(show)
        #对y轴数据进行排序，我们根据文件夹遍历并不是按照转速进行的
        y_sort = []
        y_zu_sort=[]
        for i in range(len(x)):
            for j,k in show.items():
                if i==j:
                    y_sort.append(k[0])
                    y_zu_sort.append(k[1].split("_")[2].split("r")[0])
        # 自定义 x轴 的取值：
        # colums_x = x

        colums_y = y_sort
        x_zuobiao =[float(i) for i in y_zu_sort]
        print(colums_y)
        fig, ax1 = plt.subplots(figsize=(10, 5))

        # ax2 = ax1.twinx()
        ax2 = ax1.twiny()
        ax2.plot(hz,colums_y, 'g--', marker='o')

        ax2.set_xlabel("hz-green")

        # 不要再写进 colums_x 了,这是绘制点
        ax1.plot(x_zuobiao,colums_y, 'r--',marker='o')

        # plt.xticks(range(len(x)))


        ax1.set_xticks(x_zuobiao,x_zuobiao)



        # ax1.set_xlim(ax1.get_xlim()[0],70)

        # ax1.set_xticklabels(y_zu_sort)

        # plt.xlabel("x axis ")
        # plt.ylabel("y axis ")


        # plt.axhline(y=0, ls=":")  # 添加水平直线
        for j in [1,2,4,6,7]:
            ax1.axvline(x=x_zuobiao[j], ls=":")  # 添加垂直直线


        ax1.set_xlabel("rpm")
        ax1.set_ylabel("q''kw/m3")

        #功率

        ax1.text(-5, ax1.get_ylim()[1]+2000,str(power)+"kw", family='fantasy', fontsize=12, \
                 style='italic', color='green',verticalalignment="top",horizontalalignment="right")

        pi_pei = {0:"wu_feng",1:"qing_xie",2:"xing_cheng",3:"ruo",4:"ruo",5:"zhui",6:"zhui",7:"zhuan_bian",8:"zhu",9:"zhu"}


        for i in [1,2,4,6,7,9]:
            y_situation = (ax1.get_ylim()[1] - ax1.get_ylim()[0]) / 2
            if i==2:
                y_situation = ax1.get_ylim()[1]/2+3000
            if i!=4:
                ax1.annotate(pi_pei[i], xy=(x_zuobiao[i-1], y_situation), xytext=(x_zuobiao[i-1],y_situation),fontsize=10)
            else:
                ax1.annotate(pi_pei[i], xy=(x_zuobiao[i-2], y_situation), xytext=(x_zuobiao[i-2], y_situation), fontsize=10)
        # plt.annotate('ruo', xy=(7, colums_y[1]), xytext=(7.05,colums_y[1]+3000), \
        #              arrowprops=dict(facecolor='black', shrink=100,width=1,headwidth=5))

        plt.show()

ignore().begin()
# cal_area().begin()
# save_pic_num().begin()
# delect().begin()
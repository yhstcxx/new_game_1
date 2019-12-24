import glob
import math
import sys
import threading
import time
import os
import cv2
import numpy as np
# from matplotlib import pyplot as plt
from mianji import area_v, mianji, v, biaomian
# from scipy import io
from moni import png_dir
from moni import yuzhi,baocun_csv,zhenghe_csv,zu_dir,show
#
# def begin_cal_2(a):
#     print("ok")
def begin_cal(signal_begin,path):
# 0.如果需要调用手机相机，则调用phone_pic
    time_all = time.time()
    # print(path)
    # exit()
    # 方向数+1
    # drc = 4
    print(signal_begin)
    signal_begin_int = list(map(eval, signal_begin))
    print(signal_begin_int)
    # exit()


    a = np.load("x_y_z.npy")
    print(a.shape)
    print(a[1:,:].min(axis=0))
    print(a[1:,:].max(axis=0))
    x0,y0,z0 = a[1:,:].min(axis=0)
    x1,y1,z1 = a[1:,:].max(axis=0)

    # a = np.load("x_y_z.npy")
    # print(a.shape)
    # print(a[1:,:].min(axis=0))
    # print(a[1:,:].max(axis=0))
    # x0,y0,z0 = a[1:,:].min(axis=0)
    # x1,y1,z1 = a[1:,:].max(axis=0)

    # #
    # signal_begin = ["4","6","9","360","240","1","1","1","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]


    drc,w,h,lenth,wedth,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1 = signal_begin_int
    # #棋盘格模板规格
    # w = 6
    # h = 9
    # # 世界坐标系中的棋盘格点,例如(0,0,0), (1,0,0), (2,0,0) ....,(5,8,0)，去掉Z坐标，（w*h）*3的二维矩阵,这个时有顺序的，先x，再y，再z
    # # 图片尺寸
    # lenth = 640
    # wedth = 480
    #
    # #网格划分
    # x_deta = 0.5
    # y_deta = 0.5
    # z_deta = 0.5
    # x0 = -5
    # x1 = 6
    # y0 = 0
    # y1 = 30
    # z0 = -5
    # z1 = 6

    #三维点个数
    # points_numb = int(((x1 - x0) * (z1 - z0) * (y1 - y0)) / z_deta / x_deta / y_deta)

    # 三维坐标，第四个储存辐射强度


    # points_numb=np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].T.reshape(-1, 3).shape[0]
    points_numb=np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].T.reshape(-1, 3).shape[0]
    # exit()
    poinst_3d_all = np.zeros((points_numb, 5), np.float32)
    # print(len(poinst_3d_all),"point3d")
    # print(points_numb,"points_numb")
    # sys.exit(0)
    #注意x,y,z别搞错了，有bug
    poinst_3d_all[:, :3] = np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].T.reshape(-1, 3)

    # 为后面绘图重构坐标
    shape_1 = np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].shape[1:]
    # print(shape_1,"shapeshape")
    # print(poinst_3d.shape,"3Dshape")
    # sys.exit(0)

    #1.实验组数 2.方向数，3.照片编号
    #标定图片，返回相机序（方向）号及对应内外惨----2

    zu_path=r"{}".format(path)
    # zu_path = r"C:\Users\yhstc\Desktop\shiyan"
    #实验组的路径和名字
    print(zu_path)
    zu_all,zu_name = zu_dir.fenzu(zu_path,"shiyan")

    print(zu_path)
    #标定
    path_0 = r"{}\biaoding".format(zu_path)
    image_all = png_dir.DFS_file_range(path_0,drc-1)



    print('Starting CalibrateCamera...')
    # 1.标定算法开始
    criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
    #写入体积

    for num_zu in range(len(zu_all)):


        # 保存数组，保存的坐标值及对应亮度，二值化----1，3
        path_01 = r"{}\point".format(zu_all[num_zu])

        # 保存体积、面积，每组实验随时间变化----1，3
        path_02 = zu_all[num_zu]

        # 实验图片。返回相机序号+图片（字典类型)（方向）---2，3
        path_03 = zu_all[num_zu]
        image_1 = png_dir.DFS_file_range(path_03,drc-1)


        #创建point文件夹，必须在path_1之后
        try:
            os.mkdir(path_01)
        except:
            pass

        f_volum, f_volum_close = baocun_csv.dakai(path_02, "volum_%s" % zu_name[num_zu])

        #深度循环，不是广度
        for drc_num in range(1,drc):#方向数循环

            objp = np.zeros((w*h,3), np.float32)
            #每行前两个进行赋值，标定
            objp[:,:2] = np.mgrid[-(w - 1):(w):2, 0:2 * h:2].T.reshape(-1, 2)

            obj_points = [] # 存储世界坐标系中的3D点(实际上Zw在标定板上的值为0)
            img_points = [] # 存储图像坐标系中的2D点
            images = image_all[drc_num]

            #面积
            # f_area = open(path_1 + "\\" +str(drc_num)+  "\\" + 'area_%d'%drc_num + ".csv", "a", newline='')
            # f_area = csv.writer(f_area)
            #
            # f_area.writerows([[now_time], ["index", "area"]])


            for fname in images:# 标定
                img = cv2.imread(fname)
                img = cv2.resize(img, (lenth,wedth), interpolation=cv2.INTER_AREA)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                size = gray.shape[::-1]
                ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
                #print(corners)  # 输出角点位置

                if ret:

                    obj_points.append(objp)

                    corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
                    #print(corners2)
                    if [corners2]:
                        img_points.append(corners2)
                    else:
                        img_points.append(corners)

                    # cv2.drawChessboardCorners(img, (w, h), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
                    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
                    # cv2.resizeWindow('img', 1000, 1000)
                    # cv2.imshow('img', img)
                    # cv2.waitKey(1550)

            # print(len(img_points))  # 数据集数
            cv2.destroyAllWindows()



            #print(size)
            # 标定
            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,size, None, None)
            # print(rvecs,"rvecs")

            # print("ret:", ret)  # 重投影误差
            # print("mtx:", mtx)  # 内参数矩阵
            # print("dist:", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
            # print("rvecs:", rvecs)  # 旋转向量  # 外参数
            # print("tvecs:", tvecs)  # 平移向量  # 外参数a

            #判断是投影是否在火焰内,如果只要轮廓的话，可以用比值法，比较几种算法的可靠性？

            #读取图片，到时候改为视频
            pic_num = 0
            f_area,f_area_close = baocun_csv.dakai(path_02, "area_%s_%d" % (zu_name[num_zu], drc_num))#方向
            for pic in image_1[drc_num]:#循环图片

                pic_num += 1

                frame = cv2.imread(pic)
                frame = cv2.resize(frame, (lenth , wedth), interpolation=cv2.INTER_AREA)

                # 二值化

                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                # print(gray.shape)
                # ret,binary = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)#前面哪个是阈值，后面的是设定值
                binary = yuzhi.img_binary(gray,lenth,wedth)
                # cv2.imshow("binary",binary)
                # cv2.imshow("gray",gray)
                #
                # cv2.waitKey(3000)


                binary_size = binary.shape[::-1]
                # 图像到pi个数映射，找到火焰像素个数,得到投影矩阵
                # print("______",binary_size)
                #投影对应序号，像素值
                binary_to_pi = {}
                numi = 0

                for i in range(binary_size[0]):#0-640
                    for j in range(binary_size[1]):#0-480
                        if  binary[j][i]:#白色（火焰），1，注意bug，颜色
                            numi += 1
                            binary_to_pi["binary[%d][%d]"%(j,i)]=[numi,gray[j][i]]
                baocun_csv.baocun_1(f_area,pic_num, numi)
                # f_area.writerow([pic_num, len(binary_to_pi)])
                # print(binary_to_pi,"______")
                # print(len(binary_to_pi),"binary_to_pi")

                # 投影矩阵
                # W = np.zeros((len(binary_to_pi), points_numb))#ART
                # 创建每个序列图片对应的网格,这里中断了怎么处理，，要注意
                try:
                    poinst_3d = np.load(path_01 + "\\" + "point_3d_%d.npy" % pic_num)
                except:
                    poinst_3d = poinst_3d_all
                if drc_num ==1:
                    pass
                elif drc_num==2:
                    # 坐标变换，不同视角标定，2号2
                    poinst_3d[:, 2], poinst_3d[:, 0] = poinst_3d[:, 0], -poinst_3d[:, 2]
                # 坐标变换，不同视角标定3号
                else:
                    poinst_3d[:, 0], poinst_3d[:, 2] = poinst_3d[:, 2], -poinst_3d[:, 0]

                #判断是否在指定范围内
                #转为像素点X坐标， 转为像素点Y坐标,i 为第i个点
                # #坐标变换，不同视角标定
                # poinst_3d[:,0],poinst_3d[:,2] = poinst_3d[:,2],-poinst_3d[:,0]
                for i in range(len(poinst_3d[:, :3])):
                    imgpoints2, _ = cv2.projectPoints(poinst_3d[i][:3], rvecs[0], tvecs[0], mtx, dist)#注意参数要与摄像头对应
                    imgpoints2=list(imgpoints2[0][0])
                    # if binary[math.ceil(imgpoints2[0])][math.ceil(imgpoints2[1])]:#这里注意不要超出范围,如果是,这里是binary[y][x]:X,Y已经换过了

                    try:
                        #这里ART算法的时候有bug

                        if  binary[math.ceil(imgpoints2[1])][math.ceil(imgpoints2[0])] and (poinst_3d[i][3] == 1 or drc_num == 1):
                            poinst_3d[i][3]=1#白的，1(火焰）#得到火焰内点
                            # 得到投影矩阵,[0]获取投影对应序号,-1是因为binary回去的是,建网格比较稀的时候会有bug，不要忘记-1
                            # wi = binary_to_pi["binary[%d][%d]"%(math.ceil(imgpoints2[1]),math.ceil(imgpoints2[0]))][0]-1#AR
                            # wj = i
                            # W[wi,wj] = 1
                        else:
                            poinst_3d[i][3]=0  # 黑的，0
                    except:
                        pass


                # print(np.sum(W),"np.sum(W)")
                # sys.exit(0)

                #
                # # ART算法
                # #迭代像素点个数
                # I = len(binary_to_pi)
                # # #i与像素值对应
                # binary_to_pi_i={}
                # for key,val in binary_to_pi.values():
                #     binary_to_pi_i[key] = val
                # # poinst_3d[:,3] = np.ones(points_numb)
                # #
                # # sys.exit(0)
                # # import time
                # a = time.time()
                # print("ART开始——————————")
                # #这里range可以变
                # print(points_numb,"点个数")
                # # ART算法比较慢得根据最小最大x,y计算可能能够快很多，ART算法还有改进
                # for k in range(points_numb*50):
                #     i = k%I + 1
                #     # 就是求解X
                #     # print(binary_to_pi_i[i])
                #     # print(((binary_to_pi_i[i]-W[i-1].T*poinst_3d[:,3])/(W[i-1].T*W[i-1]))*W[i-1])
                #     # print(np.sum(W[i-1]))
                #     if np.sum(W[i-1]) !=0:
                #         # print(np.sum(W[i-1]),"+++++++")
                #         # poinst_3d[:,4] = poinst_3d[:,4] + 0.9*(binary_to_pi_i[i]-W[i-1,:].dot(poinst_3d[:,4]))/W[i-1].dot(W[i-1]).T*W[i-1].T
                #         poinst_3d[:, 4] = poinst_3d[:, 4] + 0.9 * (binary_to_pi_i[i] - W[i-1,:].dot(poinst_3d[:, 4])) / W[i-1,:].dot(W[i - 1,:]).T * W[i - 1,:].T
                #
                #     for j in range(points_numb):
                #          if poinst_3d[j,4]<0:
                #              poinst_3d[j,4]=0
                # # print(np.sum(poinst_3d[:,3]),"sum")
                # print(poinst_3d,"----3d")
                # print(np.sum(poinst_3d[:,4]),"----sum")
                # a=(time.time()-a)
                # print("时间间隔为%d"%a)



                #这里调换顺序会有bug，2号
                if drc_num ==1:
                    pass
                elif drc_num ==2:
                    # 这里调换顺序会有bug，2号，        #投影不一定在xy上，这里有bug
                    poinst_3d[:, 0],poinst_3d [:, 2]  = poinst_3d[:, 2], -poinst_3d[:, 0]
                else:
                    #这里调换顺序会有bug，3号
                    poinst_3d[:, 2], poinst_3d[:, 0] = poinst_3d[:, 0], -poinst_3d[:, 2]

                np.save(path_01 + "\\" + "point_3d_%d.npy" % pic_num, poinst_3d)
                print(poinst_3d,"point_3d")

                volum = v.vol(poinst_3d,y_deta,z_deta, points_numb)#h后面加判断

                if drc_num ==drc - 1:
                    baocun_csv.baocun_1(f_volum, pic_num, volum)
                    if pic_num == len(image_1[drc_num]):
                        f_area_close.close()
                        zhenghe_csv.zhenghe("area_%s"%zu_name[num_zu], path_02)

                # p像素个数
    # 三维可视化
    # poinst_3d = np.load(r"C:\Users\yhstc\Desktop\untitled3\point_3d_1.npy")
    # shape_1 = np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].shape[1:]
    # I = poinst_3d[:, 3]
    # print(I.shape, "ishape")
    # left_points = show.show(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d)

    time_all = time.time()-time_all
    print(time_all)
    print("success")

    # sys.exit(0)


    # # #最小凸包
    # # area_v.aera(left_points)

    # 面积.aera(X, Y, Z)
# begin_cal(['4', '6', '9', '640', '480', '100', '100', '100', '-5', '5', '0', '30', '-5', '5'],r"C:\Users\yhstc\Desktop\shiyan")
# print(eval(str(10)+"i"))
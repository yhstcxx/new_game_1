import cv2
import numpy as np
from mianji import v
from moni import png_dir
from moni import yuzhi, baocun_csv, zhenghe_csv, zu_dir, show
from progressbar import *
import time
from PyQt5.QtWidgets import QApplication#ui设计
from PyQt5 import QtCore
def begin_cal(signal_begin, path, ui_obj,ui_2_obj=None):
    # 0.如果需要调用手机相机，则调用phone_pic

    model=signal_begin[-2]
    # 用于计算时间
    time_all = time.time()
    te_zheng = signal_begin[-1]
    signal_begin = signal_begin[:-2]
    # 将传入参数处理
    signal_begin_int = list(map(eval, signal_begin))
    # 参数赋值
    print(1111)
    drc, w, h, lenth, wedth, x_deta, y_deta, z_deta, x0, x1, y0, y1, z0, z1,yu_zhi_num,scale_num = signal_begin_int
    print(1111)
    # 1.实验组数 2.方向数，3.照片编号
    # 标定图片，返回相机序（方向）号及对应内外惨----2

    # 实验存放的文件夹
    zu_path = r"{}".format(path)
    print(zu_path)
    # zu_all, zu_name = zu_dir.fenzu(zu_path, "*kw")
    # 实验组的路径和名字
    zu_all, zu_name = zu_dir.fenzu(zu_path, "%s"%te_zheng)

    print(zu_path)
    # 标定路径
    path_0 = r"{}\biaoding".format(zu_path)
    # 标定图片：方向-图片名
    image_biaoding = png_dir.DFS_file_range(path_0, drc - 1)

    # 点个数
    points_numb = \
    np.mgrid[x0:x1:eval(str(x_deta) + "j"), y0:y1:eval(str(y_deta) + "j"), z0:z1:eval(str(z_deta) + "j")].T.reshape(-1,
                                                                                                                    3).shape[
        0]

    # 三维坐标，第四个储存辐射强度
    poinst_3d_all = np.zeros((points_numb, 5), np.float32)
    # print(len(poinst_3d_all),"point3d")
    # print(points_numb,"points_numb")
    # sys.exit(0)
    # 注意x,y,z别搞错了，有bug
    poinst_3d_all[:, :3] = np.mgrid[x0:x1:eval(str(x_deta) + "j"), y0:y1:eval(str(y_deta) + "j"),
                           z0:z1:eval(str(z_deta) + "j")].T.reshape(-1, 3)

    # 为后面绘图重构坐标
    shape_1 = np.mgrid[x0:x1:eval(str(x_deta) + "j"), y0:y1:eval(str(y_deta) + "j"),
              z0:z1:eval(str(z_deta) + "j")].shape[1:]
    # print(shape_1,"shapeshape")
    # print(poinst_3d.shape,"3Dshape")
    # sys.exit(0)




    print('Starting CalibrateCamera...')
    # 1.标定算法开始
    criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)

    # 组循环
    # print(zu_all)
    # exit()
    # for num_zu in range(len(zu_all)):

    # 自己设置从哪个组开始
    a_zu = 0
    b_zu = 1
    for num_zu in range(a_zu, b_zu):

        print("组为", a_zu, b_zu - 1, num_zu)

        # 保存数组，保存的坐标值及对应亮度，二值化----1，3
        path_01 = r"{}\point".format(zu_all[num_zu])

        # 保存体积、面积，每组实验随时间变化----1，3
        path_02 = zu_all[num_zu]

        # 实验图片。返回相机序号+图片（字典类型)（方向）---2，3
        path_03 = zu_all[num_zu]
        image_fangxiang = png_dir.DFS_file_range(path_03, drc - 1)

        # 创建point文件夹，必须在path_1之后
        try:
            os.mkdir(path_01)
        except:
            pass

        # 体积和三维面积的写入
        f_volum, f_volum_close = baocun_csv.dakai(path_02, "volum_%s" % zu_name[num_zu])
        f_area_3d, f_area_3d_close = baocun_csv.dakai(path_02, "area3d_%s" % zu_name[num_zu])
        f_height,f_height_close = baocun_csv.dakai(path_02, "height_%s" % zu_name[num_zu])

        # 深度循环，不是广度
        for drc_num in range(1, drc):  # 方向数循环
        #
        # for drc_num in range(3,4):
            print("方向", drc_num)
            # for drc_num in range(3,4):  # 方向数循环,从2开始会有bug，下面去调投影条件
            objp = np.zeros((w * h, 3), np.float32)
            # 每行前两个进行赋值，标定
            objp[:, :2] = np.mgrid[-(w - 1):(w):2, 0:2 * h:2].T.reshape(-1, 2)

            obj_points = []  # 存储世界坐标系中的3D点(实际上Zw在标定板上的值为0)
            img_points = []  # 存储图像坐标系中的2D点
            images = image_biaoding[drc_num]
            # print(image_all[drc_num])
            # 面积
            # f_area = open(path_1 + "\\" +str(drc_num)+  "\\" + 'area_%d'%drc_num + ".csv", "a", newline='')
            # f_area = csv.writer(f_area)
            #
            # f_area.writerows([[now_time], ["index", "area"]])

            print('标定完成-P')
            for fname in images:  # 标定
                # ui设计
                QApplication.processEvents()
                img = cv2.imread(fname)
                # img = cv2.resize(img, (lenth,wedth), interpolation=cv2.INTER_AREA)<
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                size = gray.shape[::-1]
                ret, corners = cv2.findChessboardCorners(gray, (w, h), None)
                # print(corners)  # 输出角点位置

                if ret:

                    obj_points.append(objp)

                    corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
                    # print(corners2)
                    if [corners2]:
                        img_points.append(corners2)
                    else:
                        img_points.append(corners)
                        #
                        # cv2.drawChessboardCorners(img, (w, h), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
                        # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
                        # cv2.resizeWindow('img', 1000, 1000)
                        # cv2.imshow('img', img)
                        # cv2.waitKey(0)
            #
            # print(len(img_points))  # 数据集数
            # cv2.destroyAllWindows()
            # exit()


            # print(size)
            # 标定
            ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
            if drc_num == 1:
                print("标定时间", time.time() - time_all)
                time_all = time.time()
            # print(rvecs,"rvecs")
            #
            # print("ret:", ret)  # 重投影误差
            # print("mtx:", mtx)  # 内参数矩阵
            # print("dist:", dist)  # 畸变系数   distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
            # print("rvecs:", rvecs)  # 旋转向量  # 外参数
            # print("tvecs:", tvecs)  # 平移向量  # 外参数a

            # 判断是投影是否在火焰内,如果只要轮廓的话，可以用比值法，比较几种算法的可靠性？

            # 读取图片，到时候改为视频
            pic_num = 0
            # pic_num = 714
            print('标定完成P')
            # 图片总数
            total_num = len(image_fangxiang[drc_num]) * (drc - 1)
            # 进度条
            widgets = ['[组-{}{}   方向-{}]'.format(num_zu, zu_name[num_zu], drc_num), Percentage(), ' ', Bar('>'), ' ', Timer(),
                       ' ', ETA()]
            pbar = ProgressBar(widgets=widgets, maxval=total_num).start()
            print("进度条设置")
            print(ui_obj)
            #ui 进度条
            if model == 'many':
                _translate = QtCore.QCoreApplication.translate
                #改组显示的名称
                ui_2_obj.zu_name.setText(_translate("ManyWindow", "{}/{}/{}".format(num_zu, zu_name[num_zu], drc_num)))

                ui_2_obj.progressBar.setRange(0, total_num)  # 设置进度条的范围

            print("进度条设置完成")
            # 面积加强
            f_area, f_area_close = baocun_csv.dakai(path_02, "area_%s_%d" % (zu_name[num_zu], drc_num))  # 方向
            for pic in image_fangxiang[drc_num]:  # 循环图片
                # for pic in image_1[drc_num][714:]:
                pic_num += 1
                #还可以加入组的图片个数
                progress_update_data = (drc_num - 1) * len(image_fangxiang[drc_num]) + pic_num
                pbar.update(progress_update_data)
                # print((num_zu + 1) *(pic_num)*drc_num/ len(zu_all)/len(image_1)/drc_num)
                print("进度条更新")
                print(progress_update_data,total_num)
                if model == 'many':
                    ui_2_obj.progressBar.setValue(progress_update_data)
                print("进度条更新完成")
                frame = cv2.imread(pic)
                frame = cv2.resize(frame, (lenth, wedth), interpolation=cv2.INTER_AREA)

                # 二值化

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # print(gray.shape)
                # ret,binary = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)#前面哪个是阈值，后面的是设定值
                binary = yuzhi.img_binary(gray, lenth, wedth)
                # cv2.imshow("binary",binary)
                # cv2.imshow("gray",gray)

                # cv2.waitKey(0)
                if drc_num == 1:
                    print("阈值化", time.time() - time_all)
                    time_all = time.time()

                binary_size = binary.shape[::-1]
                # 图像到pi个数映射，找到火焰像素个数,得到投影矩阵
                # print("______",binary_size)
                # 投影对应序号，像素值
                binary_to_pi = {}
                numi = 0

                for i in range(binary_size[0]):  # 0-640
                    for j in range(binary_size[1]):  # 0-480
                        if binary[j][i]:  # 白色（火焰），1，注意bug，颜色
                            numi += 1
                            binary_to_pi["binary[%d][%d]" % (j, i)] = [numi, gray[j][i]]
                baocun_csv.baocun_1(f_area, pic_num, numi)

                if drc_num == 1:
                    print("保存单面面积", time.time() - time_all)
                    time_all = time.time()

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
                    # print("alllllllllll")
                    # exit()

                # if drc_num ==1:
                #     pass
                # # elif drc_num==2:
                # elif drc_num == 2 :
                #     # 坐标变换，不同视角标定，2号2
                #     poinst_3d[:, 2], poinst_3d[:, 0] = poinst_3d[:, 0], -poinst_3d[:, 2]
                # # 坐标变换，不同视角标定3号
                # else:
                #     poinst_3d[:, 0], poinst_3d[:, 2] = poinst_3d[:, 2], -poinst_3d[:, 0]


                # if drc_num ==2 or drc_num == 3:
                #     pass
                #
                # else:
                #     poinst_3d[:, 0], poinst_3d[:, 2] = poinst_3d[:, 2], -poinst_3d[:, 0]


                # 判断是否在指定范围内
                # 转为像素点X坐标， 转为像素点Y坐标,i 为第i个点
                # #坐标变换，不同视角标定
                # poinst_3d[:,0],poinst_3d[:,2] = poinst_3d[:,2],-poinst_3d[:,0]

                # 最耗时的，可以优化
                for i in range(len(poinst_3d[:, :3])):
                    #ui设计
                    QApplication.processEvents()
                    imgpoints2, _ = cv2.projectPoints(poinst_3d[i][:3], rvecs[0], tvecs[0], mtx, dist)  # 注意参数要与摄像头对应
                    imgpoints2 = list(imgpoints2[0][0])
                    # print(imgpoints2)
                    # if binary[math.ceil(imgpoints2[0])][math.ceil(imgpoints2[1])]:#这里注意不要超出范围,如果是,这里是binary[y][x]:X,Y已经换过了
                    # if i == 1:
                    #     print("判断是否在指定范围内1", time.time() - time_all)
                    #     time_all = time.time()
                    try:
                        #     #这里ART算法的时候有bug
                        #     if binary[math.ceil(imgpoints2[1])][math.ceil(imgpoints2[0])]:
                        if binary[math.ceil(imgpoints2[1])][math.ceil(imgpoints2[0])] and (
                                poinst_3d[i][3] == 1 or drc_num == 1):
                            # poinst_3d[i][3]=poinst_3d[i][3]+1#白的，1(火焰）#得到火焰内点
                            poinst_3d[i][3] = 1
                            # print("A")
                        # 得到投影矩阵,[0]获取投影对应序号,-1是因为binary回去的是,建网格比较稀的时候会有bug，不要忘记-1
                        # wi = binary_to_pi["binary[%d][%d]"%(math.ceil(imgpoints2[1]),math.ceil(imgpoints2[0]))][0]-1#AR
                        # wj = i
                        # W[wi,wj] = 1
                        else:
                            # pass
                            poinst_3d[i][3] = 0  # 黑的，0
                            # print("B")
                    except:
                        pass
                        # if i == 1:
                        #     print("判断是否在指定范围内2", time.time() - time_all)
                        #     time_all = time.time()
                if drc_num == 1:
                    print("判断是否在指定范围内", time.time() - time_all)
                    time_all = time.time()

                # print(np.sum(W),"np.sum(W)")
                # sys.exit(0)


                # 这里调换顺序会有bug，2号
                # if drc_num ==1:
                #     pass
                # elif drc_num == 2:
                #     # 这里调换顺序会有bug，2号，        #投影不一定在xy上，这里有bug
                #     poinst_3d[:, 0],poinst_3d [:, 2]  = poinst_3d[:, 2], -poinst_3d[:, 0]
                # else:
                #     #这里调换顺序会有bug，3号
                #     poinst_3d[:, 2], poinst_3d[:, 0] = poinst_3d[:, 0], -poinst_3d[:, 2]

                # if drc_num ==2 or drc_num ==3:
                #     pass
                # else:
                #     #这里调换顺序会有bug，3号
                #     poinst_3d[:, 2], poinst_3d[:, 0] = poinst_3d[:, 0], -poinst_3d[:, 2]



                np.save(path_01 + "\\" + "point_3d_%d.npy" % pic_num, poinst_3d)

                # print(poinst_3d,"point_3d")

                #最后方向
                if drc_num == drc - 1:
                    # final_z为计算火焰高度
                    volum,final_z = v.vol(poinst_3d, y_deta, z_deta, points_numb)

                    baocun_csv.baocun_1(f_volum, pic_num, volum)
                    baocun_csv.baocun_1(f_height,pic_num,final_z)
                    # p像素个数
                    # 三维可视化,导出3d面积
                    I = poinst_3d[:, 3]
                    # print(I.shape, "ishape")


                    S = show.save(I, shape_1, x0, x1, y0, y1, z0, z1, x_deta, y_deta, z_deta, poinst_3d, zu_all[num_zu],
                                  pic_num, len(image_fangxiang[drc_num]), model, ui_obj)
                    # print('a')

                    baocun_csv.baocun_1(f_area_3d, pic_num, 0)
                    # print('b')
                    if pic_num == len(image_fangxiang[drc_num]):
                        f_area_close.close()
                        f_area_3d_close.close()
                        f_height_close.close()
                        f_volum_close.close()
                        zhenghe_csv.zhenghe("area_%s" % zu_name[num_zu], path_02)
                        #像ui界面发射信号
                        if model=='single':
                            #体积,面积
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            img_trans = cv2.transpose(frame)#旋转

                            img_flip0 = cv2.flip(img_trans, 0)#对称

                            ui_obj.finish1([volum, S], img_flip0)
                    # print('c')
            # 进度条结束
                    print('传递参数')
                    if model=='many':
                        ui_obj.loading([volum, S,pic_num])
        pbar.finish()
    time_all = time.time() - time_all
    print(time_all)
    print("success")
    if model=='many':
        ui_obj.finish()
    #为了给窗口刷新
    return False
    # sys.exit(0)


    # # #最小凸包
    # # area_v.aera(left_points)

    # 面积.aera(X, Y, Z)

# 分辨率太小会影响标定
if __name__ == '__main__':
    # begin_cal(['4', '6', '9', '1920', '1200', '50', '50', '150', '-5', '5', '0', '30', '-5', '5'],r"E:\shiyan")
    begin_cal(['4', '6', '9', '1920', '1200', '30', '80', '30', '-5', '5', '-4', '80', '-5', '5','10','1','model','kw'],
              r"C:\Users\yhstc\Desktop\90",'ui')
    # print(eval(str(10)+"i"))

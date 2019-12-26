
#按照组划分精度
from moni import zu_dir
import numpy as np
#实验放的文件夹
# path = r"E:\shiyan"
path = r"C:\Users\yhstc\Desktop\shiyan"
#实验放的文件夹
zu_path = r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"
# print(zu_path)

# 实验   组  的路径和名字
zu_all, zu_name = zu_dir.fenzu(zu_path, "shiyan")
# print(zu_all,zu_name)
for num_zu in range(len(zu_all)):
    # point文件夹的轮径
    path_01 = r"{}\point".format(zu_all[num_zu])
    # print(path_01)

    # point   名字和路径
    point_add, point_name = zu_dir.fenzu(path_01, "*")

    array_x_y_z = np.array([[0, 0, 0]])

    #每个文件
    for add in point_add:
        # print(add)
        #
        #加载点
        point = np.load(add)



        #每个点
        for i in range(len(point)):
            #1.如果第四个是1，则加一行数组
            if point[i][3]==1:
                # print(point[i,:3])
                array_x_y_z=np.row_stack((array_x_y_z,point[i,:3]))

    # np.save(path_01+"\\"+"modify.npy",array_x_y_z)
    x0, y0, z0 = array_x_y_z[1:, :].min(axis=0)
    x1, y1, z1 = array_x_y_z[1:, :].max(axis=0)
    # 得改一下
    x0 = x0 - 0.5
    x1 = x1 + 0.5
    y1 = y1 + 0.5
    z0 = z0 - 0.5
    z1 = z1 + 0.5
    # 重要
    signal_begin = ["4", "6", "9", "640", "480", "256", "256", "256", "%s" % (x0), "%s" % (x1), "%s" % y0, "%s" % (y1),
                    "%s" % (z0), "%s" % (z1)]
    # ART.begin_cal(signal_begin,r"C:\Users\yhstc\Desktop\shiyan")
    # final_all.begin_cal(signal_begin,r"C:\Users\yhstc\Desktop\shiyan")
    # zu_all[num_zu]组地址



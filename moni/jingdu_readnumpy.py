#主要是为了ART
import numpy as np

import final_all
from moni import zu_dir

#读取范围

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

    # point修正   名字和路径
    point_mo, point_name = zu_dir.fenzu(path_01, "modify")



    #只有一个
    for add in point_mo:
        a = np.load(add)
        # print(a.shape)
        # print(a[1:,:].min(axis=0))
        # print(a[1:,:].max(axis=0))
        x0,y0,z0 = a[1:,:].min(axis=0)
        x1,y1,z1 = a[1:,:].max(axis=0)
        #得改一下
        x0 = x0-0.5
        x1 = x1+0.5
        y1 = y1+0.5
        z0 = z0-0.5
        z1 = z1+0.5
        #重要
        signal_begin = ["4","6","9","640","480","256","256","256","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
        # ART.begin_cal(signal_begin,r"C:\Users\yhstc\Desktop\shiyan")
        final_all.begin_cal(signal_begin, r"C:\Users\yhstc\Desktop\shiyan")
        # '4', '6', '9', '640', '480', '0.2', '0.2', '0.2', '-5', '6', '0', '30', '-5', '6'
import cv2
import sys, os
# 1.方向循环
#2.组循环+第一张图片
#3.获取每个循环内4个点，得到每个组，每个方向低阈值的范围


def OnMouse(event, x, y, flags, param):
    # EVENT_LBUTTONDOWN 左键点击
    if event == cv2.EVENT_LBUTTONDOWN:
        pts_2d.append([x, y])
        cv2.circle(img, (x, y), 1, (0, 255, 0), -1)
        global n
        n+=1

# # # # # # # # # # #
if __name__ == '__main__':
    import numpy as np
    from moni import zu_dir
    for j in range(1,6):#方向数目，5个方向写6,每个方向确定一个范围，范围内是低阈值，范围外是高阈值
        zu_path = r"F:\2020_6_21-23_shiyan\fangxinghuo18_33"
        te_zheng = "_"
        zu_all, zu_name = zu_dir.fenzu(zu_path, "%s" % te_zheng)
        #danzu 是kw或者_里面一层
        for dandu_zu in zu_all:
            img_path =  dandu_zu+'//'+'%s'%j+'//'+'0001.bmp'
            pts_2d = []
            global n
            n = 0  # 用于取点的个数
            # img_path = r"C:\Users\yhstc\Desktop\bbb\1_\1\0001.bmp"#光取点从这开始，批注前面即可
            img = cv2.imread(img_path)
            cv2.namedWindow('image')
            # setMouseCallback 用来处理鼠标动作的函数
            # 当鼠标事件触发时，OnMouse()回调函数会被执行
            cv2.setMouseCallback('image', OnMouse)
            print(dandu_zu)
            while 1:
                cv2.imshow("image", img)
                k = cv2.waitKey(1)
                if k == 27 or n==4:
                    break
            pts_2d = np.array(pts_2d)#将四个点转为数组
            #获取点的最值
            xmin, ymin, xmax, ymax = pts_2d.min(axis=0)[0], pts_2d.min(axis=0)[1], pts_2d.max(axis=0)[0], pts_2d.max(axis=0)[1]

            np.save(dandu_zu+'//'+'yuzhi_minrange_%s.npy'%j, [xmin, ymin, xmax, ymax])

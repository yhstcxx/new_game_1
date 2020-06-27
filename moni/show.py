import numpy as np
from mayavi import mlab
import re,os,time
import pandas as pd



def save(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d,path,pic_num,image_len,model,ui_obj,num_scal=1,text=False):
    # print(text)
    time_begin = time.time()
    X, Y, Z = np.mgrid[x0:x1:eval(str(x_deta) + "j"), y0:y1:eval(str(y_deta) + "j"), z0:z1:eval(str(z_deta) + "j")]
    s = I.reshape(shape_1[2], shape_1[1], shape_1[0]).T
    if pic_num == image_len and model == 'single':
        mlab.figure(bgcolor=(1, 1, 1))
    #判断是否存在面
    try:
        obj = mlab.contour3d(X, Y, Z, s, opacity=0.7, contours=[1])  # , transparent=True)
    except:
        return 0
    # print(1)

    mlab.savefig(filename=path + "\\" +'point'+ "\\" + 'surface%s.obj' % pic_num)
    objFilePath = path + "\\" +'point' + "\\" + 'surface%s.obj'% pic_num
    mtlFilePath = path + "\\" +'point' + "\\" + 'surface%s.mtl'% pic_num
    csvFilePath = path + "\\" +'point' + "\\" + 'surface%s.csv'% pic_num
    # print(2)
    # mlab.savefig(filename="Z:\\" + 'surface%s.obj' % pic_num)
    # objFilePath = "Z:\\"  + 'surface%s.obj'% pic_num
    # mtlFilePath = "Z:\\" + 'surface%s.mtl'% pic_num
    # csvFilePath = "Z:\\" +  'surface%s.csv'% pic_num




    # mlab.savefig(filename=path + "\\" + 'point' + "\\" + 'surface%s.png' % pic_num)
    #ui端
    if pic_num == image_len and model == 'single':
        #绘图
        mlab.view(azimuth=0, elevation=0, distance=None, focalpoint=None, roll=None, reset_roll=True, figure=None)




        import cv2
        path_temp = path + "\\" + 'point' + "\\" + 'surface%s.png'%pic_num
        mlab.savefig(filename=path_temp)
        pic_3d = cv2.imread(path_temp)
        pic_3d=cv2.cvtColor(pic_3d, cv2.COLOR_BGR2RGB)
        ui_obj.finish2(pic_3d)
        # ui_obj.FinishSignal[obj].emit(pic_3d)
        os.remove(path_temp)


    mlab.clf(figure=None)
    mlab.draw(figure=None)
    # 不能用close，否则会出错
    # print('das')

    #   ui端
    if pic_num == image_len:
        mlab.close(scene=None, all=True)



    # while True:
    #     time.sleep(3)
    #     print('a')
    with open(objFilePath) as file:
        with open(csvFilePath,'w') as f:
            f.write(file.read().replace(" ",",").replace(r"//",","))

        surface_pd = pd.read_csv(csvFilePath, encoding='gbk')
        # 删除/选取某行含有特定数值的列
        cols = [x for i, x in enumerate(surface_pd.columns)]
        # print(cols)
        # print(surface_pd[1,2,3].get_loc[surface_pd['#'].isin(['v'])])
        #取指定列
        col_v = [cols[1], cols[2], cols[3]]
        col_f = [cols[1], cols[3], cols[5]]
        #面对应的点索引和对应的点坐标
        faces = np.array(surface_pd[col_f][surface_pd['#'].isin(['f'])]).astype(int)
        points = np.row_stack(([0, 0, 0], np.array(surface_pd[col_v][surface_pd['#'].isin(['v'])]).astype(float)))

    #     points = np.zeros(3)
    #     faces = np.zeros(3)
    #     lines = file.readlines()
    #     for line in lines:
    #         strs = line.split(" ")
    #         if strs[0] == "v":
    #             points = np.row_stack((points, [float(strs[1]), float(strs[2]), float(strs[3])]))
    #             # print(points)
    #
    #         if strs[0] == "f":
    #             strs = re.split(' |//', line)
    #             faces = np.row_stack((faces, [int(strs[1]), int(strs[3]), int(strs[5])]))
    #             # face = np.row_stack((face, [int(strs[1]), int(strs[3]), float(int[5])]))
    #
    #             # print(faces)
    # # 删除第一行元素,但是point第一行不用删，面对点索引从1开始,
    # #points=np.delete(points, 0, axis=0)
    # faces = np.delete(faces, 0, axis=0)
    # print(points)
    # print(faces)
    # print(time.time()-time_begin)
    # exit()
    S = 0

    len_target = 3#点个数
    Fi_S = np.array([0.0 for x in range(len_target)]) #角系数和,  2为点个数,下同,如果设置为0会有bug
    Fs2t = np.array([0.0 for x in range(len_target)])
    #T_all = np.array([[0,0,0.1] for x in range(len_target)])/num_scal#目标物坐标,这里记得将实际坐标转为相机坐标，下同/（15*0.001）
    # T_all = np.array([[0,num_scal*text,1] for x in range(len_target)])/num_scal#同一个点，6个方向，，改变y坐标，1为实际坐标，高度为坐标系的高度
    T_all = np.array([[30,0,-15],[30,0,12.5],[30,0,-3.5]]) /100/num_scal#工况1
    # T_all = np.array([[30, 21, -15], [30, 21, 12.5], [30, 21, -3.5]]) / 100 / num_scal#工况2
    # print(T_all)
    # n2_all = np.array([[0,0,1],[0,0,-1],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0]])#目标物法向量，面向y和面向-z
    n2_all = np.array([[-1, 0, 0],[-1, 0, 0],[-1, 0, 0]])#工况1，2
    for face in faces:
        # print(int(face[0]))
        # exit()
        point_1 = points[int(face[0])]
        point_2 = points[int(face[1])]
        point_3 = points[int(face[2])]
        # print(point_1,point_2,point_3)
        vector_1 = point_2 - point_1
        vector_2 = point_3 - point_1
        # 三i角形法线
        n = np.cross(vector_1, vector_2) / np.linalg.norm(np.cross(vector_1, vector_2))
        Si =  np.linalg.norm(np.cross(vector_1, vector_2)) / 2
        S += np.linalg.norm(np.cross(vector_1, vector_2)) / 2



        # print(n)
        # 质心
        c = (point_1+point_2+point_3)/3

        #遍历目标
        for i in range(len_target):
            T_i = T_all[i] #目标物坐标
            n2_i = n2_all[i] #目标物法向量
            r = (c-T_i)/np.linalg.norm(c-T_i)#目标到质心的单位向量S-T
            cos_c2T = (-r).dot(n)
            cos_T2c = r.dot(n2_i)
            # print(r,cos_c2T,cos_T2c)
            if cos_c2T>0 and cos_T2c>0:#dA2没有考虑
                Fi_S[i] = Fi_S[i] + Si*cos_c2T*cos_T2c/(np.pi*np.linalg.norm(c-T_i)**2)
                # if text:
                #     print(Fi_S[i])
                #     print('都可见',Fi_S,'Si',Si,'cos_c2T',cos_c2T,'cos_c2T',cos_T2c,"pir2",np.pi*np.linalg.norm(c-T_i)**2)
    if text:
        # print(Fi_S)
        pass
    for i in range(len_target):
        Fs2t[i] = Fi_S[i]/S#最后单位  kw/m2 ~1/k2   k =  1/num_scal
    print(Fs2t[1])



    try:
        # os.remove(objFilePath)
        os.remove(mtlFilePath)
        os.remove(csvFilePath)
    except:
        pass
    # print("保存表面积",time.time() - time_begin)
    return S,Fs2t


def show(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d):
    X, Y, Z = np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")]
    # print(X,"x")
    # print(Y,"y")
    # print(Z,"z")
    #mayavi绘制
    s = I.reshape(shape_1[2],shape_1[1],shape_1[0]).T
    # print(np.sum(s),"s.sum")
    # s = I.T
    # print(s.shape,"s",Z.shape,"Z")
    # src = mlab.pipeline.scalar_field(X, Y, Z, s)
    # src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # mlab.contour3d(X, Y, Z, X,contours=[s.max() - 1 * s.ptp(), ], opacity=0,color=(0,0,0))#contours=[s.min() + 1 * s.ptp(), ], opacity=0.1)
    # mlab.contour3d(X,Y,Z,X,opacity=0.7,contours=[3])# contours=[s.max() - 1 * s.ptp(), ])
    #这个绘制的是在火焰投影内的点，同一平面会存在重复0000，有bug
    # mlab.points3d(X,Y,Z,s,colormap="copper", scale_factor=.25)

    #
    # pts = mlab.points3d(X, Y, Z, s, scale_mode='none', scale_factor=0.2)  # 绘制点,并把s作为标量值
    # mesh = mlab.pipeline.delaunay2d(pts)
    # surf = mlab.pipeline.surface(mesh)


    # mlab.contour3d(X, Y, Z, X,contours=[s.max() - 1 * s.ptp(), ], opacity=0,color=(0,0,0))#contours=[s.min() + 1 * s.ptp(), ], opacity=0.1)
    mlab.contour3d(X, Y, Z, s, opacity=0.7,contours=[1])#, transparent=True)
    # saa = mlab.pipeline.iso_surface(src, contours=[1],opacity=0.1)
    # obj = tools.pipline.probe_data(obj)
    # mlab.pipeline.
    # src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # field = mlab.pipeline.delaunay3d(src)
    # print(src.data)

    # 保存图片
    # figsize = (32*5, 24*5)
    # mlab.savefig(filename='surface.png', size=figsize)
    # mlab.savefig(filename='surface%s.obj')
    mlab.show()

def leftpoint(point,shape_1):
    point_left = []
    for point_num in point:
        if point_num[3] == 1:
            point_left.append([point_num[0],point_num[1],point_num[2],point_num[3]])
    X,Y,Z,s = np.array(point_left).T
    print(point_left)
    print(len(point_left))
    # obj = mlab.contour3d(X, Y, Z, s, contours=[1], transparent=True)
    src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # pts = mlab.pipeline.glyph(src, scale_mode='none', scale_factor=.1)
    # pts = mlab.points3d(X, Y, Z, s, scale_mode='none', scale_factor=0.2)  # 绘制点,并把s作为标量值
    # field = mlab.pipeline.delaunay3d(src)
    # surface = mlab.contour_surf(field)
    # obj = mlab.contour3d(X, Y, Z, s, contours=[1], transparent=True)

    # print(mlab.pipeline.get_vtk_src(obj))
    mlab.show()

    # print(point_left.shape,"point.shape")


#
# poinst_3d = np.load(r"C:\Users\yhstc\Desktop\shiyan\shiyan-1-2kw\point\point_3d_1.npy")#--1
#  poinst_3d = np.load(r"C:\Users\yhstc\Desktop\untitled3\point_3d_1.npy")#--0.2

# # I = poinst_3d[:,3]#ART
# a = np.load("x_y_z.npy")
# print(a.shape)
# print(a[1:,:].min(axis=0))
# print(a[1:,:].max(axis=0))
# x0,y0,z0 = a[1:,:].min(axis=0)
# x1,y1,z1 = a[1:,:].max(axis=0)
# # # #
# # signal_begin = ["4","6","9","360","240"1",","1","1","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
#
# signal_begin = ["4","6","9","360","240","0.5","0.5","0.5","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
# signal_begin = ["4","6","9","640","480","0.2","0.2","0.2","%s"%(-5),"%s"%(6),"%s"%0,"%s"%(30),"%s"%(-5),"%s"%(6)]
# signal_begin = ["4","6","9","640","480","256","256","256","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
if __name__ == '__main__':

    # 火旋风
    path =r"G:\shiyan\fire_wirl_2\3.5kw_00_0"
    path =r"C:\Users\yhstc\Desktop\bbb\1_"
    poinst_3d = np.load(path+"\\" +'point'+"\\" +"point_3d_1.npy")
    I = poinst_3d[:, 3]  # 轮廓
    print(I.shape)
    #火旋风的，C:\Users\yhstc\Desktop\shiyan - 1\kw\point\point_3d_1.npy
    # signal_begin = ['4', '6', '9', '1920', '1200', '60', '60', '300', '-5', '5', '0', '60', '-5', '5']
    # signal_begin = ['4', '6', '9', '1920', '1200', '30', '150', '30', '-5', '5', '-4', '80', '-5', '5']
    # signal_begin = ['4', '6', '9', '1920', '1200', '50', '50', '150', '-5', '5', '0', '30', '-5', '5']
    signal_begin = ['7', '8', '11','1920', '1200', '50', '210', '50', '-10', '10', '-4', '80', '-10', '10']
    #圆柱体1
    # signal_begin = ['7', '8', '11', '1600', '800', '50', '210', '50', '-10', '10', '-4', '30', '-5', '15']
    #圆柱体2
    # signal_begin = ['6', '8', '11', '1600', '800', '50', '210', '50', '-20', '20', '-2', '30', '-20', '20']
    signal_begin_int = list(map(eval, signal_begin))
    drc,w,h,lenth,wedth,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1 = signal_begin_int
    #
    #
    shape_1=np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].shape[1:]
    # # print(I.shape,"ishape")
    # #
    show(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d)
    # for i in range(20):#这里的i是不同的高度，里面的i为不同的方向，热流计面积还没加进去
    #     S_, Fs2t_ = save(I, shape_1, x0, x1, y0, y1, z0, z1, x_deta, y_deta, z_deta, poinst_3d, path, 1, 1, '',
    #              '', num_scal=0.0135,text = i)
    # print(Fs2t_,S_)
    # save(I-点, shape_1-矩阵形状, x0, x1, y0, y1, z0, z1, x_deta, y_deta, z_deta, poinst_3d-点数据
    # , zu_all[num_zu]-组的地址,
    #               pic_num-图片序号, len(image_fangxiang[drc_num])-图片长度, model-模式, ui_obj-ui对象,num_scal=1)
    # leftpoint(poinst_3d,shape_1)



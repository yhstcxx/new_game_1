import numpy as np
from mayavi import mlab
def show(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d):
    X, Y, Z = np.mgrid[x0:x1:x_deta, y0:y1:y_deta, z0:z1:z_deta]
    # print(X,"x")
    # print(Y,"y")
    # print(Z,"z")
    #mayavi绘制
    s = I.reshape(shape_1[2],shape_1[1],shape_1[0]).T
    print(np.sum(s),"s.sum")
    # s = I.T
    print(s.shape,"s",Z.shape,"Z")
    src = mlab.pipeline.scalar_field(X, Y, Z, s)
    # src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # mlab.contour3d(X, Y, Z, X,contours=[s.max() - 1 * s.ptp(), ], opacity=0,color=(0,0,0))#contours=[s.min() + 1 * s.ptp(), ], opacity=0.1)
    # mlab.contour3d(X,Y,Z,X,opacity=0.7,contours=20)# contours=[s.max() - 1 * s.ptp(), ])
    #这个绘制的是在火焰投影内的点，同一平面会存在重复0000，有bug
    # mlab.points3d(X,Y,Z,s,colormap="copper", scale_factor=.25)

    #
    # pts = mlab.points3d(X, Y, Z, s, scale_mode='none', scale_factor=0.2)  # 绘制点,并把s作为标量值
    # mesh = mlab.pipeline.delaunay2d(pts)
    # surf = mlab.pipeline.surface(mesh)


    # mlab.contour3d(X, Y, Z, X,contours=[s.max() - 1 * s.ptp(), ], opacity=0,color=(0,0,0))#contours=[s.min() + 1 * s.ptp(), ], opacity=0.1)
    obj = mlab.contour3d(X, Y, Z, s, contours=[1], transparent=True)
    # saa = mlab.pipeline.iso_surface(src, contours=[1],opacity=0.1)
    # obj = tools.pipline.probe_data(obj)
    # mlab.pipeline.
    # src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # field = mlab.pipeline.delaunay3d(src)
    # print(src.data)

    # 保存图片
    # figsize = (32*5, 24*5)
    # mlab.savefig(filename='surface.png', size=figsize)
    # mlab.savefig(filename='surface.obj')

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



# x_deta = 0.05
# y_deta = 0.05
# z_deta = 0.05
# x0 = -5
# x1 = 4
# y0 = 0
# y1 = 22
# z0 = -5
# z1 = 3.5

# #
poinst_3d = np.load(r"C:\Users\yhstc\Desktop\shiyan\shiyan-1-\point\point_3d_1.npy")#--1
# poinst_3d = np.load(r"C:\Users\yhstc\Desktop\untitled3\point_3d_1.npy")#--0.2
# I = poinst_3d[:,3]#轮廓
I = poinst_3d[:,3]#ART
a = np.load("x_y_z.npy")
print(a.shape)
print(a[1:,:].min(axis=0))
print(a[1:,:].max(axis=0))
x0,y0,z0 = a[1:,:].min(axis=0)
x1,y1,z1 = a[1:,:].max(axis=0)
# #
# signal_begin = ["4","6","9","360","240","1","1","1","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]

signal_begin = ["4","6","9","360","240","0.5","0.5","0.5","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
# signal_begin = ["4","6","9","640","480","0.2","0.2","0.2","%s"%(-5),"%s"%(6),"%s"%0,"%s"%(30),"%s"%(-5),"%s"%(6)]
signal_begin_int = list(map(eval, signal_begin))
drc,w,h,lenth,wedth,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1 = signal_begin_int


shape_1=np.mgrid[x0:x1:x_deta, y0:y1:y_deta, z0:z1:z_deta].shape[1:]
# print(I.shape,"ishape")
#
# show(I, shape_1, x0, x1, y0, y1,z0,z1, x_deta, y_deta,z_deta, poinst_3d)
#
leftpoint(poinst_3d,shape_1)
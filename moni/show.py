import numpy as np
from mayavi import mlab
def show(I, shape_1, w0, w1, h0, h1, w_deta, h_deta, poinst_3d):
    X, Y, Z = np.mgrid[w0:w1:w_deta, h0:h1:h_deta,w0:w1:w_deta]
    # print(X,"x")
    # print(Y,"y")
    # print(Z,"z")
    #mayavi绘制
    s = I.reshape(shape_1[2],shape_1[1],shape_1[0]).T
    print(np.sum(s),"s.sum")
    # s = I.T
    print(s.shape,"s",Z.shape,"Z")
    # src = mlab.pipeline.scalar_field(X, Y, Z, s)
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
    # obj = mayavi.mlab.contour3d(X, Y, Z, s, contours=[1], transparent=True)
    obj = mlab.contour3d(X, Y, Z, s, contours=[1], transparent=True)
    # obj = tools.pipline.probe_data(obj)
    # mlab.pipeline.
    print(obj)
    mlab.show()


# poinst_3d = np.load(r"C:\Users\yhstc\Desktop\untitled3\point_3d_1.npy")
# I = poinst_3d[:,3]
# w_deta = 0.2
# h_deta = 0.2
# w0 = -5
# w1 = 6
# h0 = 0
# h1 = 30
# shape_1=np.mgrid[w0:w1:w_deta, h0:h1:h_deta,w0:w1:w_deta].shape[1:]
# print(I.shape,"ishape")
#
# left_points = show(I, shape_1, w0, w1, h0, h1, w_deta, h_deta, poinst_3d)
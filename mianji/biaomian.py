import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
import numpy as np
import scipy as sp
from scipy import spatial as sp_spatial
from mayavi import mlab
import sys

# points--点,I--亮度值，y_deta--用来计算边缘，shape_1--用来重构数组-绘图

def left_points(points,shape_1,y_deta):
    # 边界点集合中
    left_points = []
    bg = 0
    # for i in points:
    for num in range(len(points)):
        # 遍历xy，若存在边界条件则把点加入到边界点集合中
        # for x,y in points[:,:,numz]:
        #     try:
        #         if (int(x)!=0 and (int(x-1)==0 or int(x+1)==0) or (int(y!=0)and(int(y-1)==0or(int(y+1)==0)))):
        #             left_points.append(points[x,y,numz])


        if num < len(points) - y_deta:#不能越界
            #用y的时候会出问题：int+-1内都为0，这里有bug
            if (int(points[num][3])!=0 and (int(points[num-1][3])==0 or int(points[num+1][3])==0)) or (int(points[num][3])!=0 and (int(points[num-y_deta][3])==0 or int(points[num+y_deta][3])==0)):#and int(points[num-y_deta][1])!=0):
            # if int(points[num][3])!=0:
                left_points.append(points[num])
                # I[num] = 1
                # print(left_points,"leftpoints")
                # left_points[num][num][4] = 1
                # sys.exit(0)

    # print(left_points, "leftpoints")
    print(left_points,"leftpoints")
    print(points,"points")
    # left_points[num][num][4] = 1

    # left_points = np.array(left_points)
    # fig = plt.figure(3)
    # ax = fig.add_subplot(111, projection='3d')
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')
    # X = left_points[:,0]
    # print(sum(X))
    # Y = left_points[:, 1]
    # Z = left_points[:, 2]
    # ax.scatter(X, Y, Z, alpha=0.3, c=np.random.random(len(left_points)), s=np.random.randint(10, 20, size=(20, 40)))
    # plt.show()
    #
    # # sys.exit(0)
    #
    # # surf = ax.plot_surface(X, Y, Z, cmap=mpl.cm.gist_rainbow)
    # # fig.colorbar(surf, shrink=0.5, aspect=5)



    #points
    X = points[:, 0].reshape(shape_1[0],shape_1[1],shape_1[2])
    print(X.shape,"X.SHAPE")
    Y = points[:, 1].reshape(shape_1[0],shape_1[1],shape_1[2])
    Z = points[:, 2].reshape(shape_1[0],shape_1[1],shape_1[2])
    # mayavi绘制
    s = points[:,4].reshape(shape_1[0],shape_1[1],shape_1[2])
    # s = I.T
    print(s.shape,"s",Z.shape,"Z")
    # src = mlab.pipeline.scalar_field(X, Y, Z, s)
    # src = mlab.pipeline.scalar_scatter(X, Y, Z, s)
    # mlab.contour3d(X, Y, Z, X,contours=[s.max() - 1 * s.ptp(), ], opacity=0,color=(0,0,0))#contours=[s.min() + 1 * s.ptp(), ], opacity=0.1)
    # mlab.contour3d(X,Y,Z,X,opacity=0.7,contours=20)# contours=[s.max() - 1 * s.ptp(), ])
    #这个绘制的是在火焰投影内的点，同一平面会存在重复0000，有bug
    # mlab.points3d(X,Y,Z,s,colormap="copper", scale_factor=.25)
    pts = mlab.points3d(X, Y, Z, s, scale_mode='none', scale_factor=0.2)  # 绘制点,并把s作为标量值
    # mesh = mlab.pipeline.delaunay2d(pts)
    # surf = mlab.pipeline.surface(mesh)

    mlab.show()

    # sys.exit(0)
    return left_points

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d as a3
# import numpy as np
# import scipy as sp
# from scipy import spatial as sp_spatial
#
#
# # # 测试用
# # # def icosahedron():
# # #     h = 0.5*(1+np.sqrt(5))
# # #     p1 = np.array([[0, 1, h], [0, 1, -h], [0, -1, h], [0, -1, -h]])
# # #     p2 = p1[:, [1, 2, 0]]
# # #     p3 = p1[:, [2, 0, 1]]
# # #     return np.vstack((p1, p2, p3))
# # #
# # #
# # # def cube():
# # #     points = np.array([
# # #         [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
# # #         [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1],
# # #     ])
# # #     return points
# # #points = icosahedron()
# # # points = cube()
# #
# #
# #
# # def aera(points):
# def aera(points):
#     point_left = []
#     for point_num in points:
#         if point_num[3] == 1:
#             point_left.append([point_num[0],point_num[1],point_num[2]])
#     points = np.array(point_left)
#     print(points.shape)
#     hull = sp_spatial.ConvexHull(points)#,qhull_options='Qi'
#     indices = hull.simplices#序号
#     faces = points[indices]
#
#     print('area: ', hull.area)
#     print('volume: ', hull.volume)
#     #视图放大或者缩小
#     def call_back(event):
#         axtemp = event.inaxes
#         x_min, x_max = axtemp.get_xlim()
#         y_min,y_max = axtemp.get_ylim()
#         z_min, z_max = axtemp.get_zlim()
#         fanwei1 = (x_max - x_min) / 10
#         fanwei2 = (y_max - y_min) / 10
#         fanwei3 = (z_max - z_min) / 10
#         if event.button == 'up':
#             axtemp.set(xlim=(x_min + fanwei1, x_max - fanwei1))
#             axtemp.set(ylim=(y_min + fanwei2, y_max - fanwei2))
#             axtemp.set(zlim=(z_min + fanwei3, z_max - fanwei3))
#         elif event.button == 'down':
#             axtemp.set(xlim=(x_min - fanwei1, x_max + fanwei1))
#             axtemp.set(ylim=(y_min - fanwei2, y_max + fanwei2))
#             axtemp.set(zlim=(z_min - fanwei3, z_max + fanwei3))
#         fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
#
#
#     fig = plt.figure(2)
#     fig.canvas.mpl_connect('scroll_event', call_back)
#     ax = fig.add_subplot(111, projection='3d')
#     ax.dist = 30
#     ax.azim = -140
#     ax.set_xlim([0, 9])
#     ax.set_ylim([0, 9])
#     ax.set_zlim([0, 9])
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_zlabel('z')
#
#     for f in faces:
#         face = a3.art3d.Poly3DCollection([f])
#         face.set_color(mpl.colors.rgb2hex(sp.rand(3)))
#         face.set_edgecolor('k')
#         face.set_alpha(0.5)
#         ax.add_collection3d(face)
#
#     plt.show()
#     return None
# # poinst_3d = np.load(r"C:\Users\yhstc\Desktop\shiyan\shiyan-1-\point\point_3d_1.npy")#--1
# poinst_3d = np.load(r"C:\Users\yhstc\Desktop\untitled3\point_3d_1.npy")#--0.2
# I = poinst_3d[:,3]
# a = np.load("x_y_z.npy")
# print(a.shape)
# print(a[1:,:].min(axis=0))
# print(a[1:,:].max(axis=0))
# x0,y0,z0 = a[1:,:].min(axis=0)
# x1,y1,z1 = a[1:,:].max(axis=0)
# # #
# # signal_begin = ["4","6","9","360","240","1","1","1","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
# signal_begin = ["4","6","9","640","480","0.2","0.2","0.2","%s"%(-5),"%s"%(6),"%s"%0,"%s"%(30),"%s"%(-5),"%s"%(6)]
# signal_begin_int = list(map(eval, signal_begin))
# drc,w,h,lenth,wedth,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1 = signal_begin_int
#
#
# shape_1=np.mgrid[x0:x1:eval(str(x_deta)+"j"), y0:y1:eval(str(y_deta)+"j"), z0:z1:eval(str(z_deta)+"j")].shape[1:]
# print(I.shape,"ishape")
# aera(poinst_3d)

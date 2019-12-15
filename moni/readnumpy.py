from moni import  final_all,ART
import numpy as np

a = np.load("x_y_z.npy")
print(a.shape)
print(a[1:,:].min(axis=0))
print(a[1:,:].max(axis=0))
x0,y0,z0 = a[1:,:].min(axis=0)
x1,y1,z1 = a[1:,:].max(axis=0)
# #
signal_begin = ["4","6","9","360","240","0.5","0.5","0.5","%s"%(x0),"%s"%(x1),"%s"%y0,"%s"%(y1),"%s"%(z0),"%s"%(z1)]
ART.begin_cal(signal_begin,r"C:\Users\yhstc\Desktop\shiyan")
# final_all.begin_cal(signal_begin,r"C:\Users\yhstc\Desktop\shiyan")
# '4', '6', '9', '640', '480', '0.2', '0.2', '0.2', '-5', '6', '0', '30', '-5', '6'
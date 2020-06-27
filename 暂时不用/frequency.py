import numpy as np
# from matplotlib.pyplot import plot, show
import pandas as pd

import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
# path = r"C:\Users\yhstc\Desktop\untitled3\新建文件夹\area_shiyan-4-2.3kw.xlsx"
# path = r"G:\shiyan\fire_wirl_2\3.5kw_00_0\area_3.5kw_00_0.xlsx"
# # 面积
# x = pd.read_excel(io=path)
# print(x)
# sheet_name = [x for x in range(3)]
# file = pd.read_excel(io=path,sheet_name=sheet_name)
# num = 0
# for i in file.values():
#     num+=1
#     i = np.array(i['area_3.5kw_00_0_%d'%num][1:])
#     # i = np.array(i['1'][1:])
#     i = i - np.mean(i)
#
#     transformed = abs(fft(i) / len(i))
#     x_deta =[ x_in * 60 / len(transformed) for x_in in range(1, len(transformed) + 1)]
#     # print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9)
#     x_deta = np.array(x_deta)
#     fig = plt.figure('area%s'%num)
#     plt.plot(x_deta, transformed, c='green')
#     plt.xlim(0, 20)
#     # plt.plot(transformed[:600])
#
#     #输出最大值所在X坐标
#     transformed = list(transformed)
#     print('area_%d:'%num,transformed.index(max(transformed))* 60 / len(transformed))
#     if num== 3:
#         plt.show()
#     plt.show(block = False)
# exit()

# path = r'C:\Users\yhstc\Desktop\untitled3\新建文件夹\volum_shiyan-4-2.3kw.csv'
path = r"G:\shiyan\fire_wirl_2\3.5kw_00_0\volum_3.5kw_00_0 - 副本.csv"
x = pd.read_csv(path)

x = np.array(x['volum_3.5kw_00_0'][1:])
# x.columns = ['A']
# # print(x['A'][1:])
# # exit()
# x = np.array(x['A'][1:])

# x=x.astype(float)
x= x- np.mean(x)
# # print(x.shape)
# # print(len(x))
# # exit()

transformed =abs(fft(x)/len(x))
# print(transformed[:1400])
print(transformed)
x = []
for x_in in range(1,len(transformed)+1):
    x.append(x_in*60/len(transformed))
# print(np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9)
x= np.array(x)
fig = plt.figure('v')
plt.plot(x,transformed,c='green')
# plt.xlim(0,20)

#     #输出最大值所在X坐标
transformed = list(transformed)
print('volume:' , transformed.index(max(transformed)) * 60 / len(transformed))
# plt.plot(transformed[:600])
plt.show()
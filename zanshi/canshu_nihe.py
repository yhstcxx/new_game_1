# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1, 17, 1)
# y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
# z1 = np.polyfit(x, y, 3)#用3次多项式拟合
# p1 = np.poly1d(z1)
# print(p1) #在屏幕上打印拟合多项式
# yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
# plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(x, yvals, 'r',label='polyfit values')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4)
# plt.title('polyfitting')
# plt.show()



# #
# from scipy import stats
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit
# import numpy as np
# x = np.arange(1, 17, 1)
# y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
# def func(x,a,b,c,i):
#     return a*np.exp(b/x)+c*x**2+i*x
# popt, pcov = curve_fit(func, x, y)
# print(popt)
# a=popt[0]#popt里面是拟合系数，读者可以自己help其用法
# b=popt[1]
# c=popt[2]
# i=popt[3]
# # print(a,b,c)
# # print(pcov)
#
# yvals=func(x,a,b,c,i)
#
# # x = np.arange(1, 17, 1)
# # y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
# # z1 = np.polyfit(x, y, 3)#用3次多项式拟合
# # p1 = np.poly1d(z1)
# # print(p1) #在屏幕上打印拟合多项式
# # yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
#
# slope,intercept, r_value, p_value, std_err = stats.linregress(y, yvals)
#
#
# # print(r_value**2)
#
#
# plot1=plt.plot(x, y, '*',label='original values')
# plot2=plt.plot(x, yvals, 'r',label='curve_fit values')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
# plt.title('curve_fit')
# # plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',
# #          fontsize=20)
# plt.text(12, 6, 'R2 = %d'%(r_value**2), fontsize=20)
# plt.show()
# plt.savefig('p2.png')

#B样条曲线拟合
# import bezier
# import matplotlib.pyplot as plt
# import numpy as np
# a = np.array([[1.0, 2.1, 3.0, 4.0, 5.0, 6.0], [0, 1.1, 2.1, 1.0, 0.2, 0]])
# curve = bezier.Curve(a, degree=5)
# # print(curve)
# s_vals = np.linspace(0.0, 1.0, 30)
#
# data = curve.evaluate_multi(s_vals)
# print(data)
# x33 = data[0]
# y33 = data[1]
# plt.plot(x33, y33, 'y', linewidth=2.0, linestyle="-", label="y2")
# plt.show()
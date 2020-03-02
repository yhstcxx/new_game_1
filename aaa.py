# import final_all
# # import threading
# # t2 = threading.Thread(target=final_all.begin_cal, args=(['4', '6', '9', '1920', '1200', '60', '300', '60', '-5', '5', '-4', '80', '-5', '5','10','1'],
# #               r"C:\Users\yhstc\Desktop\90"))
# # t2.setDaemon(True)  # 设置为守护线程，不会因主线程结束而中断
# # t2.start()
# # final_all.\
# #     begin_cal(['4', '6', '9', '1920', '1200', '60', '300', '60', '-5', '5', '-4', '80', '-5', '5','10','1'],
# #               r"C:\Users\yhstc\Desktop\90")
# from multiprocessing import Process
#
#
#
#
# if __name__ == '__main__':
#     p1=Process(target=final_all.begin_cal,args=(['4', '6', '9', '1920', '1200', '60', '300', '60', '-5', '5', '-4', '80', '-5', '5','10','1'],
#                   r"C:\Users\yhstc\Desktop\90")) #必须加,号
#     p1.daemon=False
#     p1.start()
import cv2
import numpy as np

img=cv2.imread(r'C:\Users\yhstc\Desktop\image_22.png')
img_trans=cv2.transpose(img)
img_flip0=cv2.flip(img_trans,0)
img_flip1=cv2.flip(img,1)
img_flip_1=cv2.flip(img,-1)


cv2.imshow('img',img)
# cv2.imshow('img_trans',img_trans)
cv2.imshow('img_flip0',img_flip0)
# cv2.imshow('img_flip1',img_flip1)
# cv2.imshow('img_flip_1',img_flip_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

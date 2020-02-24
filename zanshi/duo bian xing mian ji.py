# '''
# Created on 2018年4月15日
#
# @author: XiaoYW
# '''
#排序要顺时针或者逆时针
import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y


def GetAreaOfPolyGonbyVector(points):
    # 基于向量叉乘计算多边形面积
    area = 0
    if(len(points)<3):

         raise Exception("error")

    for i in range(0,len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]

        triArea = (p1.x*p2.y - p2.x*p1.y)/2
        area += triArea
    return abs(area)

def main():

    points = []

    # x = [107,342,338,99]
    # y = [522,527,670,665]

    x = [0,200,200,0]
    y = [0,0,200,200]
    for index in range(len(x)):
        points.append(Point(x[index],y[index]))

    area = GetAreaOfPolyGonbyVector(points)
    print(area)
    print(math.ceil(area))
    # assert math.ceil(area)==1

if __name__ == '__main__':
    main()
    print("OK")
#
# import cv2
# import numpy as np
#
# image = cv2.imread(r'G:\shiyan\fire_wirl\biaoding\1\Pic_2019_12_18_231714_blockId#21380.bmp')  # （这里读入的图的尺寸要大于你的多边形）
# # polygon = np.array([[[107, 522], [342, 527], [338, 670], [99, 665]]], dtype=np.int32)  # 这里是多边形的顶点坐标
# polygon = np.array([[[0, 0], [2, 0], [2, 2], [0, 2]]], dtype=np.int32)
# im = np.zeros(image.shape[:2], dtype="uint8")  # 获取图像的维度: (h,w)=iamge.shape[:2]
# polygon_mask = cv2.fillPoly(im, polygon, 255)
#
# area = np.sum(np.greater(polygon_mask, 0))
# print(area)


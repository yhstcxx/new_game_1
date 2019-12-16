
import os
import numpy as np
import re
objFilePath = r'surface.obj'

with open(objFilePath) as file:
    points = np.zeros(3)
    faces = np.zeros(3)
    while 1:
        line = file.readline()
        if not line:
            break
        strs = line.split(" ")
        if strs[0] == "v":
            points = np.row_stack((points, [float(strs[1]), float(strs[2]), float(strs[3])]))
        if strs[0] == "f":
            strs = re.split(' |//',line)
            faces = np.row_stack((faces, [int(strs[1]), int(strs[3]), int(strs[5])]))
            # face = np.row_stack((face, [int(strs[1]), int(strs[3]), float(int[5])]))

# 删除第一行元素,但是point第一行不用删，面对点索引从1开始
# points=np.delete(points, 0, axis=0)
faces=np.delete(faces, 0, axis=0)

# print(len(points))
# print(np.max(faces))
# points = np.array([[0,0,0],[0,2,0],[2,0,0]])
# faces =  np.array([[0,1,2]])
# print(np.linalg.norm([0,1,1]))
# exit()
S = 0

for face in faces:
    # print(int(face[0]))
    # exit()
    point_1 = points[int(face[0])]
    point_2 = points[int(face[1])]
    point_3 = points[int(face[2])]

    vector_1 = point_1 - point_2
    vector_2 = point_1 - point_3
    #三角形法线
    n = np.cross(vector_1,vector_2)/np.linalg.norm(np.cross(vector_1,vector_2))
    S += np.linalg.norm(np.cross(vector_1,vector_2))/2

    #质心
    # c = (point_1+point_2+point_3)/3
    # T = (x0,y0,z0)#目标物坐标
    # n2 = (x0,y0,z0)
    # r = (c-T)/np.linalg.norm(c-T)#质心到目标的单位向量
    # cos_c2T = r.dot(n)
    # cos_T2c = (-r).dot(n2)

print("面积为：",S)
#角系数和S都是要保存的量


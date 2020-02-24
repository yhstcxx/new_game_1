import pandas as pd
import numpy as np



a111 = pd.read_csv("a.csv", encoding='gbk')
#删除/选取某行含有特定数值的列
cols=[x for i,x in enumerate(a111.columns)]
print(cols)
# print(a111[1,2,3].get_loc[a111['#'].isin(['v'])])
col_v = [cols[1],cols[2],cols[3]]
col_f = [cols[1],cols[3],cols[5]]

faces= np.array(a111[col_f][a111['#'].isin(['f'])]).astype(int)
faces= pd.Series(faces.flatten())
points = np.row_stack(([0,0,0], np.array(a111[col_v][a111['#'].isin(['v'])]).astype(float)))
faces = pd.DataFrame(np.array(faces.map(lambda x:points[x])).reshape(-1,3))

cols_faces=[x for i,x in enumerate(faces.columns)]
vector_1 = faces[cols_faces[0]]-faces[cols_faces[1]]
vector_2 = faces[cols_faces[0]]-faces[cols_faces[2]]
for i in range(len(vector_1)):



    print(np.cross(vector_1[i], vector_2[i]))
    exit()
# print(points)
# print(points.shape)
# print(np.max(faces))
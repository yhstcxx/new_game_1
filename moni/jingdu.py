from moni import zu_dir
import numpy as np
#实验放的文件夹
# path = r"E:\shiyan"
path = r"C:\Users\yhstc\Desktop\shiyan"
#实验放的文件夹
zu_path = r"{}".format(path)
# zu_path = r"C:\Users\yhstc\Desktop\shiyan"
# print(zu_path)

# 实验   组  的路径和名字
zu_all, zu_name = zu_dir.fenzu(zu_path, "shiyan")
# print(zu_all,zu_name)
for num_zu in range(len(zu_all)):
    # point文件夹的轮径
    path_01 = r"{}\point".format(zu_all[num_zu])
    # print(path_01)

    # point   名字和路径
    point_add, point_name = zu_dir.fenzu(path_01, "*")

    array_x_y_z = np.array([[0, 0, 0]])

    #每个文件
    for add in point_add:
        # print(add)
        #
        #加载点
        point = np.load(add)



        #每个点
        for i in range(len(point)):
            #1.如果第四个是1，则加一行数组
            if point[i][3]==1:
                # print(point[i,:3])
                array_x_y_z=np.row_stack((array_x_y_z,point[i,:3]))

        np.save("x_y_z.npy",array_x_y_z)



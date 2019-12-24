import numpy as np
import pandas as pd
# filename = 'a.txt' # 内含中文
# f = open(filename, 'r', encoding='utf-8') # ‘r’可以省略，因为默认值就是r
def modify(path):
    f = path
    # a=np.loadtxt("obstract.csv",delimiter=",")
    a=pd.read_csv(f,encoding='gbk')
    # while 1:
    #     line = f.readline()
    #     if not line:
    #         break
    #     strs = line.split(" ")
    #     a.append(strs)
    a = np.array(a)
    # print(a.shape)
    # exit()
    # f.close
    num = 0
    #对数据进行筛选，让它更有规律（已知存在规律的情况下）
    while 1:
        for i in range(len(a)-2):
            if a[i][2]==a[i+2][2] and a[i][2]!=a[i+1][2]:
                a[i + 1][2]=a[i][2]
        for i in range(len(a)-5):
            if a[i][2]==a[i+5][2] and a[i+1][2]==a[i+4][2] and a[i+2][2]==a[i+3][2] and a[i+1][2]!=a[i+2][2]:
                a[i + 2][2] = a[i + 3][2] = a[i+1][2]
        for i in range(len(a)-8):
            if a[i][2] == a[i + 8][2] and a[i + 1][2] == a[i + 7][2] and a[i + 2][2] == a[i + 6][2] and a[i + 3][2] == a[i + 4][
                2]==a[i+5][2] and a[i + 3][2] !=a[i][2]:
                a[i + 3][2]=a[i+4][2]=a[i + 5][2]=a[i][2]
        for i in range(len(a)-9):
            if a[i][2] == a[i + 9][2] and a[i + 1][2] == a[i + 8][2] and a[i + 2][2] == a[i + 7][2] and a[i + 3][2] == a[i + 4][
                2]==a[i+5][2]==a[i+6][2] and a[i + 3][2] !=a[i][2]:
                a[i + 3][2] = a[i + 4][2] = a[i + 5][2] =a[i+6][2]= a[i][2]
        num+=1
        if num == 2:
            break
    # print(a[0][1]=='不存在')
    num_len = 0
    count_begin = False
    obstract_may=[]
    #计算存在的个数，对应的开始点
    for i in range(len(a)):
        if count_begin:
            if a[i][1] == '存在':
                num_len+=1
            else:
                count_begin=False
                obstract_may.append(num_len)
                num_len = 0
        else:
            if a[i][1] == '存在':
                count_begin = True
                num_len += 1
                #初始化字典
                obstract_may.append(a[i][0])
                obstract_may.append(a[i][1])
            else:
                pass
    obstract_may=np.array(obstract_may).reshape(-1,3)
    print(obstract_may)

    #验证准确性
    deta = []
    for i in range(len(obstract_may)):
        if 0<i<len(obstract_may)-1:
            deta.append(int(obstract_may[i+1][1])-int(obstract_may[i][1]))
    deta = np.array(deta).reshape(-1,1)

    obstract_may = np.column_stack((obstract_may, deta))

    obstract_may = pd.DataFrame(obstract_may)
    obstract_may.to_csv('obstract_may.csv',encoding='gbk')

    data1 = pd.DataFrame(a)
    data1.to_csv('obstract_modify.csv',encoding='gbk')

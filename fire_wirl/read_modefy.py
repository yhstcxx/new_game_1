import numpy as np
filename = 'a.txt' # 内含中文
f = open(filename, 'r', encoding='utf-8') # ‘r’可以省略，因为默认值就是r


a=[]
while 1:
    line = f.readline()
    if not line:
        break
    strs = line.split(" ")
    a.append(strs)

f.close

for i in range(len(a)-2):
    if a[i][1]==a[i+2][1] and a[i][1]!=a[i+1][1]:
        a[i + 1][1]=a[i][1]
for i in range(len(a)-5):
    if a[i][1]==a[i+5][1] and a[i+1][1]==a[i+4][1] and a[i+2][1]==a[i+3][1] and a[i+1][1]!=a[i+2][1]:
        a[i + 2][1] = a[i + 3][1] = a[i+1][1]
for i in range(len(a)-8):
    if a[i][1] == a[i + 8][1] and a[i + 1][1] == a[i + 7][1] and a[i + 2][1] == a[i + 6][1] and a[i + 3][1] == a[i + 4][
        1]==a[i+5][1] and a[i + 3][1] !=a[i][1]:
        a[i + 3][1]=a[i+4][1]=a[i + 5][1]=a[i][1]
for i in range(len(a)-2):
    if a[i][1]==a[i+2][1] and a[i][1]!=a[i+1][1]:
        a[i + 1][1]=a[i][1]
for i in range(len(a)-5):
    if a[i][1]==a[i+5][1] and a[i+1][1]==a[i+4][1] and a[i+2][1]==a[i+3][1] and a[i+1][1]!=a[i+2][1]:
        a[i + 2][1] = a[i + 3][1] = a[i+1][1]
a = np.array(a)
import pandas as pd
data1 = pd.DataFrame(a)
data1.to_csv('a.csv',encoding='gbk')
print(a)
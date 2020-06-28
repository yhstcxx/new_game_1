import os
import shutil
from moni import zu_dir
zu_path = r"C:\Users\yhstc\Desktop\1"
te_zheng = "_"
zu_all, zu_name = zu_dir.fenzu(zu_path, "%s" % te_zheng)
print(zu_all)
for i in zu_all:

# os.remove(path)  # 删除文件
# os.removedirs(path)  # 删除空文件夹
#
# os.rmdir(path)  # 删除空文件夹
#
    # shutil.rmtree(i+'//'+'point')  # 递归删除文件夹，即：删除非空文件夹
    dir = os.listdir(i)
    for j in dir:
        if j not in [ 'yuzhi_minrange_1.npy', 'yuzhi_minrange_2.npy', 'yuzhi_minrange_3.npy', 'yuzhi_minrange_4.npy', 'yuzhi_minrange_5.npy','1'
                      ,'2','3','4','5']:
            try:
                os.remove(i+'//'+j)
            except:
                shutil.rmtree(i + '//' +j)
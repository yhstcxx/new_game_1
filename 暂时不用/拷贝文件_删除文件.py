import os
import shutil
from moni import zu_dir
zu_path = r"C:\Users\yhstc\Desktop\11111"
te_zheng = "_"
zu_all, zu_name = zu_dir.fenzu(zu_path, "%s" % te_zheng)
print(zu_all)
#组名字C:\Users\yhstc\Desktop\1\1_
for i in range(len(zu_all)):

# os.remove(path)  # 删除文件
# os.removedirs(path)  # 删除空文件夹
#
# os.rmdir(path)  # 删除空文件夹
#
    # shutil.rmtree(i+'//'+'point')  # 递归删除文件夹，即：删除非空文件夹
    dir = os.listdir(zu_all[i])
    #文件名
    path = r"G:"+'//'+zu_name[i]
    try:
        os.mkdir(path)
    except:
        pass

    for j in dir:
        # if j not in [ 'yuzhi_minrange_1.npy', 'yuzhi_minrange_2.npy', 'yuzhi_minrange_3.npy', 'yuzhi_minrange_4.npy', 'yuzhi_minrange_5.npy','1'
        #               ,'2','3','4','5']:
        if j not in ['yuzhi_minrange_1.npy', 'yuzhi_minrange_2.npy', 'yuzhi_minrange_3.npy', 'yuzhi_minrange_4.npy',
                     'yuzhi_minrange_5.npy', '1'
            , '2', '3', '4', '5']:#改方向数以及方向数对应的npy
            #复制文件或者文件夹
            try:
                shutil.copyfile(zu_all[i]+'//'+j, path+'//'+j)
            except:
                shutil.copytree(zu_all[i] + '//' +j,path+'//'+j,ignore=shutil.ignore_patterns('*.npy'))

            #删除文件
            # try:
            #     os.remove(zu_all[i]+'//'+j)
            # except:
            #     shutil.rmtree(zu_all[i] + '//' +j)
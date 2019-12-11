import time, csv

def dakai(path, name):
    struct_time = time.localtime(time.time())
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    f1 = open(path + "\\" + name + ".csv", "a", newline='')
    f = csv.writer(f1)
    #体积对应帧序号
    # 第二行为pandas的数据类型，只要不是字符串就行，不然保存excel会出现问题
    # f.writerows([[now_time], ["index", name]])
    f.writerow(["index", name,now_time])
    return f,f1
def baocun_1(f,index,parameter):
    f.writerow([index, parameter])


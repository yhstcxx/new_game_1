path_4=r"E:\shiyan"
import time,csv

struct_time = time.localtime(time.time())
now_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
a=0

f_1 = open("volume_.csv","a")#,"a", newline='')
f_1 = csv.writer(f_1)
f = open(r'E:\shiyan\volume_.csv', "r").readlines()
f_1.writerows([[now_time], ["index", "volume"]])
for i in range(len(f)):
    if (i+1)%3==0:
        f_1.writerow(f[i])

# f1.close()

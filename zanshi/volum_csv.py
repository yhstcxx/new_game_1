import time,csv
struct_time = time.localtime(time.time())
now_time = time.strftime("%Y-%m-%d %H:%M:%S",struct_time)
f = open('volume_'+str(now_time)+".csv","a",newline='')
f = csv.write(f)
index = 0
f.writerows([[now_time],["index","volume"]])

f.writerow(volume)
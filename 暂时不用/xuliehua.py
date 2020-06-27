import json
import numpy as np
# 序列化：将Python对象转换成json字符串并存储到文件中
obj1 = np.array([1,2,3])
obj2 = np.array([4,5,6])
obj = [obj1,obj2]
try:
    a,b = np.load('test.npy')
    print(a)
except:
    np.save('test.npy',obj)
    print("aaa")

# json.dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
#
# # 反序列化：读取指定文件中的json字符串并转换成Python对象
# json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None)
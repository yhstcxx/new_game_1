# def DFS_file_range(dict_name):
#     import os
#     result = {}
#     temp_name1 = os.listdir(dict_name)[:] # list ["","",...]
#     for eve in temp_name1:
#         result[eval(eve)] = []
#         for pic in os.listdir(dict_name + "\\" + eve):
#             result[eval(eve)].append(dict_name + "\\" + eve+"\\"+pic)
#     return result
# print(DFS_file_range(r"C:\Users\yhstc\Desktop\wenjian\biaoding-uihou"))
def DFS_file_range(dict_name,num=3):
    import os
    result = {}
    temp_name1 = os.listdir(dict_name)[:num] # list ["","",...]
    for eve in temp_name1:
        result[eval(eve)] = []
        for pic in os.listdir(dict_name + "\\" + eve):
            result[eval(eve)].append(dict_name + "\\" + eve+"\\"+pic)
    return result
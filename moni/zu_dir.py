import os
import pandas as pd
import csv
import glob
def fenzu(path,name):
    all_files = glob.glob(os.path.join(path, "{}*".format(name)))
    # df_from_each_file = (pd.read_csv(f) for f in all_files)

    zu_list = []
    zu_name = []
    # for idx, df in enumerate(df_from_each_file):
    #     df.to_excel(writer, sheet_name='area{0}.csv'.format(idx+1))
    for f in all_files:
        zu_list.append(os.path.realpath(f))
        zu_name.append(os.path.basename(f))
    # print(zu_list)
    # print(all_files)
    return zu_list,zu_name
# zu_path=r"C:\Users\yhstc\Desktop\shiyan"
# #实验组的路径和名字
# zu_all,zu_name = fenzu(zu_path,"*")
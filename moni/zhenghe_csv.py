import os
import pandas as pd
import csv
import glob
def zhenghe(name,path):
    writer = pd.ExcelWriter(r'{0}/{1}.xlsx'.format(path,name),engin='openpyxl')


    all_files = glob.glob(os.path.join(path, "{0}*.csv".format(name)))
    # df_from_each_file = (pd.read_csv(f) for f in all_files)


    # for idx, df in enumerate(df_from_each_file):
    #     df.to_excel(writer, sheet_name='area{0}.csv'.format(idx+1))
    for f in all_files:
        df = pd.read_csv(f)
        print(df)
        df.to_excel(writer, sheet_name=os.path.basename(f),index=False)

    writer.save()
    writer.close()
    for infile in all_files:
        os.remove(infile)

# path = r"C:\Users\yhstc\Desktop\shiyan"
# zhenghe("area",path)
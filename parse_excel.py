import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import timedelta
import json
import numpy as np

name_of_pressed_button = "Расходные материалы для оргтехники (бумага)"
df = pd.read_excel('3.xlsx', sheet_name='1')
dict_for_json = {}
df.dropna(how='all')
print("Column headings:")
#print(df.columns)
for each in df.columns:
    if (each not in [4, 8, 12, 13]):
        df.drop(each, axis = 1, inplace = True)
i = 0
print(df[12])
for each in df[12]:
    temp_t = each
    while (((df[13][i] - temp_t).days) > 0):
        temp_t = (pd.to_datetime(temp_t) + timedelta(days=1))
        #curr_date = (pd.to_datetime(temp_t) - dt.datetime(1970,1,1))
        #curr_date = (df['date'] - dt.datetime(1970,1,1)).dt.total_seconds()
        curr_date = temp_t
       # curr_date = pd.to_datetime([curr_date]).astype(int) / 10**9
        #curr_date = curr_date.astype(int)
        curr_date = int(curr_date.timestamp())
        #print(int(curr_date))
        #curr_date = str(curr_date)
        #curr_date = int(curr_date)
        if curr_date in dict_for_json:
            dict_for_json[curr_date] += 1
        else:
            dict_for_json[curr_date] = 1
    i+=1
    print(i)
print("i am here")
dict_for_json = json.dumps(dict_for_json)
json_for_visual = json.loads(dict_for_json)
with open('year.json', 'w') as outfile:
    json.dump(json_for_visual, outfile)
#print((df[13][0] - df[12][0]).days)
#print(df[13][0])
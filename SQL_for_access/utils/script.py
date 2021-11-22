from natsort import index_natsorted
import numpy as np
import pandas as pd
import os

root_dir = os.path.dirname(os.path.dirname(__file__))
try:
    data = np.genfromtxt(os.path.join(root_dir, 'access.log'), dtype ='str', delimiter =' ', usecols = (0, 3, 4, 5, 6, 7, 8, 9))
except Exception as e:
    raise Exception(f'No file in directory {e}')

df = pd.DataFrame(data)
df.columns = ['IP', 'Time', 'Time_2', 'Request', 'URL', 'Protocol', 'Response', 'Size']
df["Time"] = df["Time"] + df["Time_2"]
df = df.drop(columns='Time_2')

# Общее количество запросов
total_requests = df.shape[0]

# Общее количество запросов по типу
request_by_type = df['Request'].value_counts()
indexes = request_by_type.index
new_index = {}
for i in range(request_by_type.shape[0]):
    new_index[indexes[i]] = indexes[i].replace('"','')

request_by_type = request_by_type.rename(index=new_index)

max_len_requests_by_type = 0
for i in range(request_by_type.shape[0]):
    if len(request_by_type.index[i]) > max_len_requests_by_type:
        max_len_requests_by_type = len(request_by_type.index[i])

# Топ 10 самых частых запросов
top_10_URL = df['URL'].value_counts().head(10)

max_len_top_10 = 0
for i in range(10):
    if len(top_10_URL.index[i]) > max_len_top_10:
        max_len_top_10 = len(top_10_URL.index[i])

# Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
df_4xx = df[df['Response'].str.contains(r"4\d\d")]
df_4xx_sort = df_4xx.sort_values(ascending=False,
   by="Size",
   key=lambda x: np.argsort(index_natsorted(df_4xx["Size"]))
)
top_5_4XX_error = df_4xx_sort[['URL', 'Response', 'Size', 'IP']].head(5)

max_len_URL_4XX = 0
for i in top_5_4XX_error.index:
    if len(top_5_4XX_error['URL'][i]) > max_len_URL_4XX:
        max_len_URL_4XX = len(top_5_4XX_error['URL'][i])

# Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
df_5xx = df[df['Response'].str.contains(r"5\d\d")]
top_5_5XX_error = df_5xx['IP'].value_counts().head(5)


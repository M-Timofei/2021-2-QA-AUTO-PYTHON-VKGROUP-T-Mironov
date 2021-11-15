import numpy as np
import pandas as pd
import os
import argparse
import json
from natsort import index_natsorted

parser = argparse.ArgumentParser(description="Create json")
parser.add_argument('--json', action='store_true')
args = parser.parse_args()

data = np.genfromtxt('access.log', dtype = 'str', delimiter = ' ', usecols = (0,3,4,5,6,7,8,9))
df = pd.DataFrame(data)
df.columns = ['IP', 'Time', 'Time_2', 'Request', 'URL', 'Protocol', 'Response', 'Size']
df["Time"] = df["Time"] + df["Time_2"]
df = df.drop(columns='Time_2')

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
python_file = open("data_python.txt", "w+")

# Общее количество запросов

data_all = 'Общее количество запросов:\n' + str(df.shape[0])

# Общее количество запросов по типу

data_request = df['Request'].value_counts()

if args.json:
    json_request = {}
    for i in range(len(data_request.index)):
        json_request.update({
            str(pd.DataFrame(data_request).index[i]).replace('"',''): str(data_request[i])
        })
    data_request_output = json.dumps(json_request, indent=4)
    data_request_output = 'Общее количество запросов по типу:\n' + data_request_output
else:
    data_request_output = 'Общее количество запросов по типу:\n' + data_request.to_string()

# Топ 10 самых частых запросов

data_biggest = df['URL'].value_counts().head(10)
if args.json:
    json_biggest = {}
    for i in range(10):
        json_biggest.update({
            str(pd.DataFrame(data_biggest).index[i]): str(data_biggest[i])
        })

    data_biggest_output = json.dumps(json_biggest, indent=4)
    data_biggest_output = 'Топ 10 самых частых запросов:\n' + data_biggest_output
else:
    data_biggest_output = 'Топ 10 самых частых запросов:\n' + data_biggest.to_string()

# Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой

df_4xx = df[df['Response'].str.contains("4\d\d")]
df_4xx_sort = df_4xx.sort_values(ascending=False,
   by="Size",
   key=lambda x: np.argsort(index_natsorted(df_4xx["Size"]))
)
index_4xx_biggest = df_4xx_sort[['URL', 'Response', 'Size', 'IP']].head(5)

if args.json:
    json_4xx = {}
    for i in index_4xx_biggest.index:
        json_4xx.update({
            str(index_4xx_biggest['URL'][i]): str([index_4xx_biggest['Response'][i],
                                                                index_4xx_biggest['Size'][i],
                                                                index_4xx_biggest['IP'][i],
                                                                ])
        })
    data_4xx_output = json.dumps(json_4xx, indent=4)
    data_4xx_output = 'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n' + data_4xx_output
else:
    data_4xx_output = 'Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой\n' \
           + index_4xx_biggest.to_string(index = False)

# Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой

df_5xx = df[df['Response'].str.contains("5\d\d")]
data_5xx = df_5xx['IP'].value_counts().head(5)

if args.json:
    json_5xx = {}
    for i in range(5):
        json_5xx.update({
            str(pd.DataFrame(data_5xx).index[i]): str(data_5xx[i])
        })

    data_5xx_output = json.dumps(json_5xx, indent=4)
    data_5xx_output = 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n' + data_5xx_output
else:
    data_5xx_output = 'Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n' + data_5xx.to_string()

with open(os.path.join(base_dir, "data_python.txt"), "w") as file:
    file.write(data_all + '\n')
    file.write('\n' + data_request_output.replace('"', '') + '\n')
    file.write('\n' + data_biggest_output + '\n')
    file.write('\n' + data_4xx_output + '\n')
    file.write('\n' + data_5xx_output + '\n')
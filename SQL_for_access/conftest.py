import pytest
import numpy as np
import pandas as pd
import os
from mysql_orm.client import MysqlORMClient

def pytest_addoption(parser):
    parser.addoption('--topurl', default=10)
    parser.addoption('--top4xx', default=5)
    parser.addoption('--top5xx', default=5)

@pytest.fixture(scope='session')
def config(request):
    topurl = request.config.getoption('--topurl')
    top4xx = request.config.getoption('--top4xx')
    top5xx = request.config.getoption('--top5xx')
    return {'topurl': topurl, 'top4xx': top4xx, 'top5xx': top5xx}

def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()

    config.mysql_orm_client = mysql_orm_client

def pytest_unconfigure(config):
    client = config.mysql_orm_client
    client.connection.close()

@pytest.fixture(scope='session')
def my_df():
    root_dir = os.path.dirname(__file__)
    print('root_dir', root_dir)
    try:
        data = np.genfromtxt(os.path.join(root_dir, 'access.log'), dtype='str', delimiter=' ',
                             usecols=(0, 3, 4, 5, 6, 7, 8, 9))
    except Exception as e:
        raise Exception(f'No file in directory {e}')

    df = pd.DataFrame(data)
    df.columns = ['IP', 'Time', 'Time_2', 'Request', 'URL', 'Protocol', 'Response', 'Size']
    df["Time"] = df["Time"] + df["Time_2"]
    df = df.drop(columns='Time_2')
    df = df.apply(lambda x: x.str.slice(0, 1000))
    return df
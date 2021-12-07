import pytest
import numpy as np
from natsort import index_natsorted
from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder

class MysqlBase:

    table_name = None

    def prepare(self):
        pass

    def create_table_for_test(self):
        self.mysql.create_table(self.table_name)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request, my_df):
        self.config = config
        self.mysql: MysqlORMClient = request.config.mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)
        self.create_table_for_test()
        self.my_df = my_df
        self.prepare()

    def get_data(self, table_name):
        self.mysql.session.commit()
        data = self.mysql.session.query(table_name)
        return data.all()

    def get_total_requests(self, my_df):
        return my_df.shape[0]

    def get_request_by_type(self, my_df):
        request_by_type = my_df['Request'].value_counts()
        indexes = request_by_type.index
        new_index = {}
        for i in range(request_by_type.shape[0]):
            new_index[indexes[i]] = indexes[i].replace('"', '')

        for key, value in new_index.items():
            if len(value) > 6:
                print(value)
                new_index[key] = "invalid request"

        request_by_type = request_by_type.rename(index=new_index)

        return request_by_type

    def get_top_URL(self, my_df):
        top_URL = my_df['URL'].value_counts().head(int(self.config['topurl']))

        return top_URL

    def get_df_4xx(self, my_df):
        df_4xx = my_df[my_df['Response'].str.contains(r"4\d\d")]
        df_4xx_sort = df_4xx.sort_values(ascending=False,
                                         by="Size",
                                         key=lambda x: np.argsort(index_natsorted(df_4xx["Size"]))
                                         )
        top_4XX_error = df_4xx_sort[['URL', 'Response', 'Size', 'IP']].head(int(self.config['top4xx']))

        return top_4XX_error

    def get_df_5xx(self, my_df):
        df_5xx = my_df[my_df['Response'].str.contains(r"5\d\d")]
        top_5XX_error = df_5xx['IP'].value_counts().head(int(self.config['top5xx']))

        return top_5XX_error
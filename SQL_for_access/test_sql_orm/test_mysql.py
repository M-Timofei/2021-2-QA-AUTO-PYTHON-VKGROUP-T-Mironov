from models.model import TotalRequests, RequestsByType, TopURL, Top_4XX, Top_5XX
from test_sql_orm.base import MysqlBase

# файл access.log должен находиться в директории SQL_for_access

class TestTotalRequests(MysqlBase):
    table_name = 'Total_requests'

    def prepare(self):
        total_requests = self.get_total_requests(self.my_df)
        self.mysql_builder.create_total_requests(Count=total_requests)

    def test_SQL_total_requests(self):
        # мы заранее знаем, что в этой таблице будет одна запись, и сравниваем с единицей
        assert len(self.get_data(TotalRequests)) == 1

class TestRequestsByType(MysqlBase):
    table_name = 'Requests_by_type'

    def prepare(self):
        request_by_type = self.get_request_by_type(self.my_df)
        for i in range(request_by_type.shape[0]):
            self.mysql_builder.create_requests_by_type(Request=request_by_type.index[i],
                                                       Count=request_by_type[i])

    def test_SQL_request_by_type(self):
        # здесь и далее мы сравниваем количество записей в таблице с количеством строк в исходных данных
        request_by_type = self.get_request_by_type(self.my_df)
        assert request_by_type.shape[0] == len(self.get_data(RequestsByType))

class TestTopURL(MysqlBase):
    table_name = 'Top_URL'

    def prepare(self):
        top_URL = self.get_top_URL(self.my_df)
        for i in range(int(self.config['topurl'])):
            self.mysql_builder.create_top_URL(URL=top_URL.index[i],
                                                 Count=top_URL[i])

    def test_SQL_top_requests(self):
        top_URL = self.get_top_URL(self.my_df)
        assert top_URL.shape[0] == len(self.get_data(TopURL))

class TestTop4XXError(MysqlBase):
    table_name = 'Top_4XX_errors'

    def prepare(self):
        top_4XX_error = self.get_df_4xx(self.my_df)
        for i in top_4XX_error.index:
            self.mysql_builder.create_top_4XX(URL = top_4XX_error['URL'][i],
                                                Response = top_4XX_error['Response'][i],
                                                Size = top_4XX_error['Size'][i],
                                                IP = top_4XX_error['IP'][i])

    def test_SQL_top_4xx_error(self):
        top_4XX_error = self.get_df_4xx(self.my_df)
        assert top_4XX_error.shape[0] == len(self.get_data(Top_4XX))

class TestTop5XXError(MysqlBase):
    table_name = 'Top_5XX_errors'

    def prepare(self):
        top_5XX_error = self.get_df_5xx(self.my_df)
        for i in range(int(self.config['top5xx'])):
            self.mysql_builder.create_top_5XX(IP=top_5XX_error.index[i],
                                                Count=top_5XX_error[i])

    def test_SQL_top_5xx_error(self):
        top_5XX_error = self.get_df_5xx(self.my_df)
        assert top_5XX_error.shape[0] == len(self.get_data(Top_5XX))
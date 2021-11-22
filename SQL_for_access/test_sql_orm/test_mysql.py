from models.model import TotalRequests, RequestsByType, Top10URL, Top5_4XX, Top5_5XX
from utils.script import total_requests, request_by_type, top_10_URL, top_5_4XX_error, top_5_5XX_error
from test_sql_orm.base import MysqlBase

# файл access.log должен находиться в директории SQL_for_access

class TestTotalRequests(MysqlBase):

    def prepare(self):
        self.mysql_builder.create_total_requests(Count=total_requests)

    def test_SQL_total_requests(self):
        # мы заранее знаем, что в этой таблице будет одна запись, и сравниваем с единицей
        assert len(self.get_data(TotalRequests)) == 1

class TestRequestsByType(MysqlBase):
    def prepare(self):
        for i in range(request_by_type.shape[0]):
            self.mysql_builder.create_requests_by_type(Request=request_by_type.index[i],
                                                       Count=request_by_type[i])

    def test_SQL_request_by_type(self):
        # здесь и далее мы сравниваем количество записей в таблице с количеством строк в исходных данных
        assert request_by_type.shape[0] == len(self.get_data(RequestsByType))

class TestTop10URL(MysqlBase):
    def prepare(self):
        for i in range(10):
            self.mysql_builder.create_top_10_URL(URL=top_10_URL.index[i],
                                                 Count=top_10_URL[i])

    def test_SQL_top_10_requests(self):
        assert top_10_URL.shape[0] == len(self.get_data(Top10URL))

class TestTop4XXError(MysqlBase):
    def prepare(self):
        for i in top_5_4XX_error.index:
            self.mysql_builder.create_top_5_4XX(URL = top_5_4XX_error['URL'][i],
                                                Response = top_5_4XX_error['Response'][i],
                                                Size = top_5_4XX_error['Size'][i],
                                                IP = top_5_4XX_error['IP'][i])

    def test_SQL_(self):
        assert top_5_4XX_error.shape[0] == len(self.get_data(Top5_4XX))

class TestTop5XXError(MysqlBase):
    def prepare(self):
        for i in range(5):
            self.mysql_builder.create_top_5_5XX(IP=top_5_5XX_error.index[i],
                                                Count=top_5_5XX_error[i])

    def test_SQL(self):
        assert top_5_5XX_error.shape[0] == len(self.get_data(Top5_5XX))
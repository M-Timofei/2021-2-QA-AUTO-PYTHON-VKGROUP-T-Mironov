import pytest

from mysql_orm.client import MysqlORMClient
from utils.builder_orm import MysqlORMBuilder

class MysqlBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlORMClient = mysql_orm_client
        self.mysql_builder: MysqlORMBuilder = MysqlORMBuilder(self.mysql)

        self.prepare()

    def get_data(self, table_name):
        self.mysql.session.commit()
        data = self.mysql.session.query(table_name)
        return data.all()
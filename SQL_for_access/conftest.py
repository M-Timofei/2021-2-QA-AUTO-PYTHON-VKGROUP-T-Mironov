import pytest

from mysql_orm.client import MysqlORMClient

def pytest_configure(config):
    mysql_orm_client = MysqlORMClient(user='root', password='pass', db_name='TEST_SQL')
    if not hasattr(config, 'workerinput'):
        mysql_orm_client.recreate_db()
        mysql_orm_client.create_total_requests()
        mysql_orm_client.create_requests_by_type()
        mysql_orm_client.create_top_10_URL()
        mysql_orm_client.create_top_5_4XX()
        mysql_orm_client.create_top_5_5XX()

    config.mysql_orm_client = mysql_orm_client

@pytest.fixture(scope='session')
def mysql_orm_client(request) -> MysqlORMClient:
    client = request.config.mysql_orm_client
    yield client
    client.connection.close()
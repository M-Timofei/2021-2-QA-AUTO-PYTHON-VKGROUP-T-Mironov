import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker

from models.model import Base

class MysqlORMClient:

    def __init__(self, user, password, db_name, host='127.0.0.1', port=3306):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}'

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        sm = sessionmaker(bind=self.connection.engine)
        self.session = sm()

    def recreate_db(self):
        self.connect(db_created=False)

        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)

        self.connection.close()
        self.connect(db_created=True)

    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def create_total_requests(self):
        if not inspect(self.engine).has_table('Total_requests'):
            Base.metadata.tables['Total_requests'].create(self.engine)

    def create_requests_by_type(self):
        if not inspect(self.engine).has_table('Requests_by_type'):
            Base.metadata.tables['Requests_by_type'].create(self.engine)

    def create_top_10_URL(self):
        if not inspect(self.engine).has_table('Top_10_URL'):
            Base.metadata.tables['Top_10_URL'].create(self.engine)

    def create_top_5_4XX(self):
        if not inspect(self.engine).has_table('Top_5_4XX_errors'):
            Base.metadata.tables['Top_5_4XX_errors'].create(self.engine)

    def create_top_5_5XX(self):
        if not inspect(self.engine).has_table('Top_5_5XX_errors'):
            Base.metadata.tables['Top_5_5XX_errors'].create(self.engine)
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from db.model import UserModel
import allure

class DBClient:

    def __init__(self, user, password, db_name, host, port):
        self.user = user
        self.password = password
        self.db_name = db_name

        self.host = host
        self.port = port

        self.engine = self.create_engine()
        self.connection = self.create_connection()
        self.session = self.create_session()

    def create_engine(self):
        url = f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'
        engine = sqlalchemy.create_engine(url, encoding='utf8')
        return engine

    def create_connection(self):
        connection = self.engine.connect()
        return connection

    def create_session(self):
        sm = sessionmaker(bind=self.connection.engine)
        return sm()

    @allure.step('Создание пользователя в БД')
    def create_user_in_db(self, user):
        self.session.add(user)
        self.session.commit()

    @allure.step('Получение данных о пользователе {username} из БД')
    def get_user_from_db_by_name(self, username):
        self.session.commit()
        user = self.session.query(UserModel).filter(UserModel.username == username).first()
        return user

    @allure.step('Наличие {username} в БД')
    def check_user_in_db_by_name(self, username):
        user = self.get_user_from_db_by_name(username)
        return True if user is not None else False

    @allure.step('Получение данных о пользователе по email {email} из БД')
    def get_user_from_db_by_email(self, email):
        self.session.commit()
        user_by_email = self.session.query(UserModel).filter(UserModel.email == email).first()
        return user_by_email

    @allure.step('Наличие {email} в БД')
    def check_user_in_db_by_email(self, email):
        user_by_email = self.get_user_from_db_by_email(email)
        return True if user_by_email is not None else False

    @allure.step('Проверка {username} на блокировку в БД')
    def check_block_user(self, username):
        user = self.get_user_from_db_by_name(username)
        return user.access

    @allure.step('Проверка {username} на активность в БД')
    def check_user_active(self, username):
        user = self.get_user_from_db_by_name(username)
        return user.active

    @allure.step('Проверка начала активности {username} в БД')
    def check_user_start_active_time(self, username):
        user = self.get_user_from_db_by_name(username)
        return user.start_active_time

    @allure.step('Блокировка пользователя {username} в БД')
    def block_user(self, username):
        user = self.get_user_from_db_by_name(username)
        user.access = 0
        self.session.commit()
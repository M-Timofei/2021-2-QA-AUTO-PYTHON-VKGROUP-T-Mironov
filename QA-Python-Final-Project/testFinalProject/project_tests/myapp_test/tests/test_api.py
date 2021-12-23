import datetime
import allure
import pytest
from cases.api.base import BaseCaseAPI

@allure.epic('API')
@allure.feature('Проверка статуса приложения')
class TestStatus(BaseCaseAPI):
    def test_check_status(self):
        res = self.api_client.get_check_status()
        assert res.json()['status'] == 'ok', 'Приложение не запущено'

@allure.epic('API')
@allure.feature('Позитивные тесты на добавление пользователя')
class TestAddUserPositive(BaseCaseAPI):

    @allure.story('Добавление пользователя')
    def test_add_user(self, user_data):
        res = self.api_client.post_add_user(username=user_data['username'],
                                            password=user_data['password'],
                                            email=user_data['email'])
        assert self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь не добавлен в БД'
        assert res.status_code == 201, 'Неверный код ответа'
        assert res.text == 'User was added!', 'Неверный текст ответа'

    @allure.story('Добавление пользователя дважды')
    def test_add_user_again(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        res = self.api_client.post_add_user(username=user_data['username'],
                                            password=user_data['password'],
                                            email=user_data['email'])
        assert res.status_code == 304, 'Неверный код ответа'
        assert not res.text == '', 'Пустой текст ответа'

@allure.epic('API')
@allure.feature('Негативные тесты на добавление пользователя')
class TestAddUserNegative(BaseCaseAPI):

    @allure.story('Добавление пользователя с некорректным именем')
    @pytest.mark.parametrize('invalid_username', ['', 'q' * 17, None])
    def test_add_user_incorrect_username(self, user_data, invalid_username):
        res = self.api_client.post_add_user(username='',
                                            password=user_data['password'],
                                            email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(''), 'Пользователь добавлен в БД'
        assert res.status_code == 400, 'Неверный код ответа'
        assert not res.text == 'User was added!', 'Неверный текст ответа'
        assert not res.text == '', 'Пустой текст ответа'

    @allure.story('Добавление пользователя с некорректным паролем')
    @pytest.mark.parametrize('invalid_password', ['', 'q' * 256, None])
    def test_add_user_incorrect_password(self, user_data, invalid_password):
        res = self.api_client.post_add_user(username=user_data['username'],
                                            password=invalid_password,
                                            email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь добавлен в БД'
        assert res.status_code == 400, 'Неверный код ответа'
        assert not res.text == 'User was added!', 'Неверный текст ответа'
        assert not res.text == '', 'Пустой текст ответа'

    @allure.story('Добавление пользователя с некорректной почтой')
    @pytest.mark.parametrize('invalid_email', ['', 'invalid_email', 'q'*65, None])
    def test_add_user_incorrect_email(self, user_data, invalid_email):
        res = self.api_client.post_add_user(username=user_data['username'],
                                            password=user_data['password'],
                                            email=invalid_email)
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь добавлен в БД'
        assert res.status_code == 400, 'Неверный код ответа'
        assert not res.text == 'User was added!', 'Неверный текст ответа'
        assert not res.text == '', 'Пустой текст ответа'

@allure.epic('API')
@allure.feature('Позитивные тесты на удаление пользователя')
class TestDeleteUserPositive(BaseCaseAPI):

    @allure.story('Удаление пользователя')
    def test_delete_user(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        res = self.api_client.get_del_user(user_data['username'])
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь не удален из БД'
        assert res.status_code == 204, 'Неверный код ответа'
        assert not res.text == '', 'Пустой текст ответа'

@allure.epic('API')
@allure.feature('Негативные тесты на удаление пользователя')
class TestDeleteUserNegative(BaseCaseAPI):

    @allure.story('Удаление несуществующего пользователя')
    def test_delete_user_negative(self):
        res = self.api_client.get_del_user(username='invalid_name')
        assert res.status_code == 404, 'Неверный код ответа'
        assert res.text == 'User does not exist!', 'Неверный текст ответа'

@allure.epic('API')
@allure.feature('Позитивные тесты на блокировку пользователя')
class TestBlockUserPositive(BaseCaseAPI):

    @allure.story('Блокировка пользователя')
    def test_block_user(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        res = self.api_client.get_block_user(username=user_data['username'])
        assert not self.bd_client.check_block_user(user_data['username']), 'Пользователь не заблокирован в в БД'
        assert res.status_code == 200, 'Неверный код ответа'
        assert res.text == 'User was blocked!', 'Неверный текст ответа'

    @allure.story('Повторная блокировка пользователя')
    def test_block_user_again(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        self.api_client.get_block_user(username=user_data['username'])
        res = self.api_client.get_block_user(username=user_data['username'])
        assert res.status_code == 304, 'Неверный код ответа'
        assert not res.text == '', 'Пустой текст ответа'

@allure.epic('API')
@allure.feature('Негативные тесты на блокировку пользователя')
class TestBlockUserNegative(BaseCaseAPI):

    @allure.story('Блокировка несуществующего пользователя')
    def test_block_user_negative(self):
        res = self.api_client.get_block_user(username='invalid_name')
        assert res.status_code == 404, 'Неверный код ответа'
        assert res.text == 'User does not exist!', 'Неверный текст ответа'

@allure.epic('API')
@allure.feature('Позитивные тесты на разблокировку')
class TestAcceptUserPositive(BaseCaseAPI):

    @allure.story('Разблокировка заблокированного пользователя')
    def test_accept_user(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        self.api_client.get_block_user(username=user_data['username'])
        res = self.api_client.get_accept_user(username=user_data['username'])
        assert self.bd_client.check_block_user(username=user_data['username']), 'Пользователь заблокирован в в БД'
        assert res.status_code == 200, 'Неверный код ответа'
        assert res.text == 'User access granted!', 'Неверный текст ответа'

    @allure.story('Разблокировка незаблокированного пользователя')
    def test_accept_unblock_user(self, user_data):
        self.api_client.post_add_user(username=user_data['username'],
                                      password=user_data['password'],
                                      email=user_data['email'])
        res = self.api_client.get_accept_user(username=user_data['username'])
        assert self.bd_client.check_block_user(username=user_data['username']), 'Пользователь заблокирован в в БД'
        assert res.status_code == 304, 'Неверный код ответа'
        assert not res.text == '', 'Пустой текст ответа'

@allure.epic('API')
@allure.feature('Негативные тесты на разблокировку')
class TestAcceptUserNegative(BaseCaseAPI):

    @allure.story('Разблокировка несуществующего пользователя')
    def test_accept_user_negative(self):
        res = self.api_client.get_accept_user(username='invalid_name')
        assert res.status_code == 404, 'Неверный код ответа'
        assert res.text == 'User does not exist!', 'Неверный текст ответа'

@allure.epic('API')
@allure.feature('Проверка активности пользователя')
class TestActiveUser(BaseCaseAPI):

    @allure.story('Проверка активности залогиненного пользователя')
    def test_active_user(self):
        assert self.bd_client.check_user_active(username=self.api_client.username), 'Пользователь не активен'

    @allure.story('Проверка активности разлогиненного пользователя')
    def test_inactive_user(self):
        res = self.api_client.get_logout_user()
        assert not self.bd_client.check_user_active(username=self.api_client.username), 'Пользователь активен'
        assert not res.text == '<!DOCTYPE html>', 'Ответ содержит <!DOCTYPE html>'

@allure.epic('API')
@allure.feature('Проверка начала времени активности пользователя')
class TestActiveTimeUser(BaseCaseAPI):

    def test_active_time(self):
        '''Совершаем логаут, запоминаем текущее время, логинимся и смотрим время старта активности юзера.
            Разница двух времен не должа превышать 5 секунд с учетом погрешности'''
        self.api_client.get_logout_user()
        now_time = datetime.datetime.now(tz=None).replace(microsecond=0)
        self.api_client.authorization()
        start_active_time = self.bd_client.check_user_start_active_time(username=self.api_client.username)
        assert (now_time-start_active_time).seconds < 5, 'Неверное время начала активности пользователя'

@allure.epic('API')
@allure.feature('Проверка невозможности отправить зепрос не root пользователю')
class TestNoRootUser(BaseCaseAPI):

    @allure.story('Запрос на добавление пользователя')
    def test_add_user_no_root(self):
        res = self.api_client_no_root.post_add_user(username='username',
                                                   password='password',
                                                   email='email')
        assert res.status_code == 401, 'Неверный код ответа'
        assert res.json()['error'] == 'session lifetime expires', 'Неверный текст ошибки'

    @allure.story('Запрос на удаление пользователя')
    def test_delete_user_no_root(self):
        res = self.api_client_no_root.get_del_user('username')
        assert res.status_code == 401, 'Неверный код ответа'
        assert res.json()['error'] == 'session lifetime expires', 'Неверный текст ошибки'

    @allure.story('Запрос на блокировку пользователя')
    def test_block_user_no_root(self):
        res = self.api_client_no_root.get_block_user('username')
        assert res.status_code == 401, 'Неверный код ответа'
        assert res.json()['error'] == 'session lifetime expires', 'Неверный текст ошибки'

    @allure.story('Запрос на разблокировку пользователя')
    def test_accept_user_no_root(self):
        res = self.api_client_no_root.get_accept_user('username')
        assert res.status_code == 401, 'Неверный код ответа'
        assert res.json()['error'] == 'session lifetime expires', 'Неверный текст ошибки'
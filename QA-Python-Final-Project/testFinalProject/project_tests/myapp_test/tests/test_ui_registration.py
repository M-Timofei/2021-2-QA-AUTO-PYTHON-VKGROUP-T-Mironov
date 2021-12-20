import allure
import pytest

from cases.ui.base import BaseCaseUI

@allure.epic('UI_registration')
@allure.feature('Позитивный тест на регистрацию')
class TestRegistrationPositive(BaseCaseUI):

    @allure.story('Регистрация пользователя с валидными данными')
    def test_registration(self, user_data):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         email=user_data['email'])

        assert self.main_page.check_user_login() == f"Logged as {user_data['username']}"

@allure.epic('UI_registration')
@allure.feature('Негативные тесту на регистрацию')
class TestRegistrationNegative(BaseCaseUI):

    @allure.story('Регистрация пользователя с невалидной длиной имени')
    @pytest.mark.parametrize('invalid_username', ['q', 'q' * 17])
    def test_registration_negative_length_username(self, user_data, invalid_username):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=invalid_username,
                                         password=user_data['password'],
                                         email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(invalid_username), 'Пользователь добавлен в БД'
        assert registration_page.error_massage() == 'Incorrect username length', 'Неверное сообщение об ошибке'

    @allure.story('Регистрация пользователя с невведенной почтой')
    def test_registration_negative_without_email(self, user_data):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         email='')
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь добавлен в БД'
        assert not registration_page.error_massage() == 'Incorrect email length',\
            'Должна появляться подсказка о необходимости ввести почту, а не выводиться ошибка'

    @allure.story('Регистрация пользователя с невалидной длиной почты')
    @pytest.mark.parametrize('invalid_email', ['q', 'q' * 65])
    def test_registration_negative_length_email(self, user_data, invalid_email):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         email=invalid_email)
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь добавлен в БД'
        assert registration_page.error_massage() == 'Incorrect email length', 'Неверное сообщение об ошибке'

    @allure.story('Регистрация пользователя с невалидной длиной пароля')
    @pytest.mark.parametrize('invalid_password', ['q', 'q' * 256])
    def test_registration_negative_length_password(self, user_data, invalid_password):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=invalid_password,
                                         email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(user_data['username']), 'Пользователь добавлен в БД'
        assert registration_page.error_massage() == 'Incorrect password length', 'Неверное сообщение об ошибке'

    @allure.story('Регистрация пользователя с невалидной почтой')
    def test_registration_negative_invalid_email(self, user_data):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         email='invalid_email')

        assert not self.bd_client.check_user_in_db_by_name(user_data['username'])
        assert registration_page.error_massage() == 'Invalid email address', 'Неверное сообщение об ошибке'

    @allure.story('Регистрация пользователя с невалидным подтверждением пароля')
    def test_registration_negative_invalid_second_password(self, user_data):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         second_password='invalid_password',
                                         email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(user_data['username'])
        assert registration_page.error_massage() == 'Passwords must match', 'Неверное сообщение об ошибке'

    @allure.story('Регистрация пользователя с невведенным паролем')
    def test_registration_negative_without_second_password(self, user_data):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=user_data['username'],
                                         password=user_data['password'],
                                         second_password='',
                                         email=user_data['email'])
        assert not self.bd_client.check_user_in_db_by_name(user_data['username'])
        assert not registration_page.error_massage() == 'Passwords must match', \
            'Должна появляться подсказка о необходимости ввести почту, а не выводиться ошибка'

    @allure.story('Повторная регистрация пользователей с одним и тем же именем')
    def test_registration_negative_same_username(self, create_user):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=create_user.username,
                                         password=create_user.password,
                                         email='again_' + create_user.email)
        assert not self.bd_client.check_user_in_db_by_email('again_' + create_user.email)
        assert registration_page.error_massage() == 'User already exist', 'Неверное сообщение об ошибке'

    @allure.story('Повторная регистрация пользователей с одной и той же почтой')
    def test_registration_negative_same_email(self, create_user):
        registration_page = self.login_page.go_to_registration()
        registration_page.create_account(username=create_user.username+'_again',
                                         password=create_user.password,
                                         email=create_user.email)
        assert not self.bd_client.check_user_in_db_by_name(create_user.username+'_again')
        assert registration_page.error_massage() == 'Email already exist', 'Неверное сообщение об ошибке'

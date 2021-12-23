import pytest
import allure
from cases.ui.base import BaseCaseUI

@allure.epic('UI_authorization')
@allure.feature('Позитивные тесты на авторизацию')
class TestAuthorizationPositive(BaseCaseUI):

    @allure.story('Авторизация пользователя с валидными данными')
    def test_authorization(self, create_user):
        self.login_page.authorization(create_user.username, create_user.password)
        assert self.main_page.check_user_login() == f"Logged as {create_user.username}", 'Невалидная информация о текущем пользователе'

    @allure.story('Авторизация заблокированного пользователя')
    def test_authorization_without_access(self, create_user):
        self.bd_client.block_user(create_user.username)
        self.login_page.authorization(create_user.username, create_user.password)
        assert self.login_page.error_massage() == 'Your account has been blocked', 'Неверное сообщение об ошибке, должно быть на английском'

@allure.epic('UI_authorization')
@allure.feature('Негативные тесты на авторизацию')
class TestAuthorizationNegative(BaseCaseUI):

    @allure.story('Авторизация с невалидной длиной имени')
    @pytest.mark.parametrize('invalid_username', ['q', 'q' * 17])
    def test_authorization_negative_length_username(self, invalid_username):
        self.login_page.authorization(invalid_username, 'MyPass345')
        assert self.login_page.error_massage() == f"Incorrect username length", 'Неверное сообщение об ошибке'

    @allure.story('Авторизация с невалидным именем')
    def test_authorization_negative_invalid_username(self, create_user):
        self.login_page.authorization('invalid_username', create_user.password)
        assert self.login_page.error_massage() == f"Invalid username or password", 'Неверное сообщение об ошибке'

    @allure.story('Авторизация с невалидным паролем')
    def test_authorization_negative_invalid_password(self, create_user):
        self.login_page.authorization(create_user.username, 'invalid_password')
        assert self.login_page.error_massage() == f"Invalid username or password", 'Неверное сообщение об ошибке'

    @allure.story('Авторизация с невалидным именем и паролем')
    def test_authorization_negative_invalid_password_and_username(self):
        self.login_page.authorization('invalid_username', 'invalid_password')
        assert self.login_page.error_massage() == f"Invalid username or password", 'Неверное сообщение об ошибке'
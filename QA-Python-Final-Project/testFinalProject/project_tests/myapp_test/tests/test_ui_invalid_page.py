from cases.ui.base import BaseCaseUI
import allure

@allure.epic('UI_404_page')
@allure.feature('Invalid 404 page')
class TestInvalidPage(BaseCaseUI):

    @allure.story('Проверка текста ошибки на несуществующей странице')
    def test_404_page(self):
        invalid_page = self.login_page.go_to_invalid_page()
        assert invalid_page.check_error() == 'Page Not Found', 'Неверное сообщение об ошибке'
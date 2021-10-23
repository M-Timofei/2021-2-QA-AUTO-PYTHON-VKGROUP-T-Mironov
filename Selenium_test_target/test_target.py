from base import BaseCase
import pytest
from ui import urls
from ui.locators.target_locators import BasePageLocators

class TestsForTarget(BaseCase):

    @pytest.mark.UI
    def test_log_in(self):
        # логинимся и проверяем, что оказались на нужной странице
        self.login_page.log_in()
        self.base_page.check_url(urls.URL_DASHBOARD)

    @pytest.mark.UI
    def test_log_out(self):
        # логинимся, затем выходим и проверяем, что оказались на стартовой странице
        self.login_page.log_in()
        self.dashboard_page.log_out()
        self.base_page.check_url(urls.URL_BASE)

    @pytest.mark.UI
    def test_editing_contact_information(self):
        # логинимся, изменяем контактную информацию, обновляем страницу и проверяем, что изменения сохранились
        self.login_page.log_in()
        self.profile_page.editing_contact_information()

    @pytest.mark.parametrize(
        'bar_locator, bar_url',
        [
            pytest.param(BasePageLocators.STATISTICS_BUTTON_LOCATOR, urls.URL_STATISTICS),
            pytest.param(BasePageLocators.TOOLS_BUTTON_LOCATOR, urls.URL_TOOLS)
        ]
    )
    @pytest.mark.UI
    def test_navbar_going(self, bar_locator, bar_url):
        # логинимся и пробуем перейти на соответствующие вкладки
        self.login_page.log_in()
        self.base_page.go_to_bar(bar_locator, bar_url)
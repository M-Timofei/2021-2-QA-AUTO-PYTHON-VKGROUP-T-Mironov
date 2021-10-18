from base import BaseCase
import pytest
from ui import urls

class TestsForTarget(BaseCase):

    @pytest.mark.UI
    # логинимся и проверяем, что оказались на нужной странице
    def test_log_in(self):
        self.login_page.log_in()
        self.base_page.check_url(urls.url_dashboard)

    @pytest.mark.UI
    # логинимся, затем выходим и проверяем, что оказались на стартовой странице
    def test_log_out(self):
        self.login_page.log_in()
        self.dashboard_page.log_out()
        self.base_page.check_url(urls.url_base)

    @pytest.mark.UI
    # логинимся, изменяем контактную информацию, обновляем страницу и проверяем, что изменения сохранились
    def test_editing_contact_information(self):
        self.login_page.log_in()
        self.profile_page.editing_contact_information()

    # логинимся и пробуем перейти на соответствующие вкладки
    @pytest.mark.parametrize(
        'bar',
        [
            pytest.param('Статистика'),
            pytest.param('Инструменты')
        ]
    )
    @pytest.mark.UI
    def test_navbar_going(self, bar):
        self.login_page.log_in()
        self.navbar_page.go_to_bar(bar)
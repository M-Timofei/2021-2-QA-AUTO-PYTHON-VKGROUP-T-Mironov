import pytest
from base import BaseCase

class TestAndroid(BaseCase):

    @pytest.mark.AndroidUI
    def test_russia_population(self):
        search_page = self.main_page.skip_windows()
        search_page.check_population()

    @pytest.mark.AndroidUI
    def test_calculator(self):
        search_page = self.main_page.skip_windows()
        search_page.check_calculator_result()

    @pytest.mark.AndroidUI
    def test_news(self):
        search_page = self.main_page.skip_windows()
        menu_page = search_page.go_to_menu_page()
        news_page = menu_page.go_to_news()
        news_page.select_news()
        search_page.check_news()

    @pytest.mark.AndroidUI
    def test_version(self):
        search_page = self.main_page.skip_windows()
        menu_page = search_page.go_to_menu_page()
        about_page = menu_page.go_to_about()
        about_page.check_about()
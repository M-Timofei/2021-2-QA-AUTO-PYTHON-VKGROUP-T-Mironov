import allure
import pytest
from base import BaseCase

class TestsForTargetNegative(BaseCase):
    authorize = False

    @allure.epic('Tests for target')
    @allure.feature('Negative tests')
    @allure.story('Invalid password')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.UI
    def test_invalid_password(self):
        self.login_page.check_invalid_password()

    @allure.epic('Tests for target')
    @allure.feature('Negative tests')
    @allure.story('Invalid login')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.UI
    def test_invalid_login(self):
        self.login_page.check_invalid_login()

class TestsForTargetPositive(BaseCase):
    authorize = True

    @allure.epic('Tests for target')
    @allure.feature('Positive tests')
    @allure.story('Create new company')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('Each image is randomly generated')
    @pytest.mark.UI
    def test_create_company(self, image_path):
        campaign_page = self.dashboard_page.go_to_create_company()
        campaign_page.create_new_company(image_path)

    @allure.epic('Tests for target')
    @allure.feature('Positive tests')
    @allure.story('Create new segment')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.UI
    def test_create_segment(self):
        segments_page = self.dashboard_page.go_to_create_segment()
        segments_page.check_create_segment()

    @allure.epic('Tests for target')
    @allure.feature('Positive tests')
    @allure.story('Delete segment')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.UI
    def test_delete_segment(self):
        segments_page = self.dashboard_page.go_to_create_segment()
        segments_page.check_create_segment()
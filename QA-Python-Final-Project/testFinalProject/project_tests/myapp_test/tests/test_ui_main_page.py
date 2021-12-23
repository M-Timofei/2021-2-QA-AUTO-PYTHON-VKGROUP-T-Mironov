import allure
import random
from cases import urls
from cases.ui.base import BaseCaseUI
from cases.ui.python_zen import python_zen

@allure.epic('UI_main_page')
@allure.feature('Доступ главной страницы неавторизированным пользователям')
class TestMainPageWithoutAuthorization(BaseCaseUI):

    def test_main_page_without_authorization(self):
        self.driver.get(urls.WELCOME_PAGE)
        assert self.login_page.error_massage() == 'This page is available only to authorized users', 'Неверное сообщение об ошибке'

@allure.epic('UI_main_page')
@allure.feature('Тесты на mock и vk id')
class TestMockID(BaseCaseUI):

    @allure.story('Проверка наличия vk_id пользователя')
    def test_vk_id(self, create_user):
        vk_id = random.randint(1, 10000)
        self.mock_client.add_user(create_user.username, vk_id)
        self.login_page.authorization(create_user.username, create_user.password)
        assert self.main_page.check_user_id() == f'VK ID: {vk_id}', 'Неверный или отсутствующий vk id'

    @allure.story('Проверка отсутствия vk_id пользователя')
    def test_vk_id_negative(self, create_user):
        self.login_page.authorization(create_user.username, create_user.password)
        assert self.main_page.check_user_id() == 'No vk_id for user', 'vk id для данного пользователя не должно быть'

@allure.epic('UI_main_page')
@allure.feature('Проверка логаут')
class TestLogout(BaseCaseUI):
    authorize = True

    @allure.feature('Логаут пользователя')
    def test_logout(self):
        self.main_page.logout()
        assert self.driver.current_url == urls.LOGIN_PAGE, 'Неверная ссылка после логаута'

@allure.epic('UI_main_page')
@allure.feature('Проверка цитаты Python')
class TestPythonZen(BaseCaseUI):
    authorize = True

    @allure.story('Проверка цитаты Python')
    def test_python_zen(self):
        assert self.main_page.python_zen() in python_zen, 'Неверная цитата Python'

@allure.epic('UI_main_page')
@allure.feature('Элементы navbar открывают страницы в новой вкладке')
class TestNavbar(BaseCaseUI):
    authorize = True

    @allure.story('Логотип ведет на страницу welcome')
    def test_brand(self):
        self.main_page.click_brand()
        assert self.driver.current_url == urls.WELCOME_PAGE, 'Открыт неверный URL'
#
    @allure.story('Home ведет на страницу welcome')
    def test_home(self):
        self.main_page.click_home()
        assert self.driver.current_url == urls.WELCOME_PAGE, 'Открыт неверный URL'

    @allure.story('Python ведет на страницу python.org')
    def test_python(self):
        self.main_page.click_python()
        self.go_to_next_tab()
        assert 'python.org' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Python history открывает статью об истории python')
    def test_python_history(self):
        self.main_page.click_python_history()
        self.go_to_next_tab()
        assert 'History_of_Python' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Python flask открывает статью о flask')
    def test_python_flask(self):
        self.main_page.click_python_flask()
        self.go_to_next_tab()
        assert 'flask' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Linux открывает статью о linux')
    def test_linux(self):
        self.main_page.click_linus()
        self.go_to_next_tab()
        assert 'linux' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Centos7 открывает статью о Centos7')
    def test_linux_centos(self):
        self.main_page.click_linus_centos()
        self.go_to_next_tab()
        assert 'Centos7' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Network открывает статью о сетях')
    def test_network(self):
        self.main_page.click_network()
        self.go_to_next_tab()
        assert 'network' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Wireshark news открывает новости о Wireshark')
    def test_network_news(self):
        self.main_page.click_network_news()
        self.go_to_next_tab()
        assert 'news' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Wireshark download открывает сайт, где можно скачать Wireshark')
    def test_network_download(self):
        self.main_page.click_network_download()
        self.go_to_next_tab()
        assert 'download' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Tcpdump examples открывает соответствующий сайт')
    def test_network_examples(self):
        self.main_page.click_network_examples()
        self.go_to_next_tab()
        assert 'examples' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('What is an API открывает статью об API')
    def test_what_is_an_api(self):
        self.main_page.click_what_is_an_api()
        self.go_to_next_tab()
        assert 'API' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Future of internet открывает соответствующую статью')
    def test_future_of_internet(self):
        self.main_page.click_future_of_internet()
        self.go_to_next_tab()
        assert 'future-of-the-internet' in self.driver.current_url, 'Открыт неверный URL'

    @allure.story('Lets talk about SMTP открывает статью о SMTP')
    def test_smtp(self):
        self.main_page.click_smtp()
        self.go_to_next_tab()
        assert 'SMTP' in self.driver.current_url, 'Открыт неверный URL'
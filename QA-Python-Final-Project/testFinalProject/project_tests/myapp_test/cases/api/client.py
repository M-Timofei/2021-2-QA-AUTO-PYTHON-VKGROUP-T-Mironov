import requests
import allure
from urllib.parse import urljoin

class ResponseStatusCodeException(Exception):
    pass

class ApiClient:

    def __init__(self, base_url, username=None, password=None, root_user=True):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        if root_user:
            self.authorization()

    def _request(self, method, location, headers=None, data=None, json=None):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers, data=data, json=json)
        self.create_allure(method, url, headers, data, json, response)
        return response

    def create_allure(self, method, url, headers, data, json, response):
        '''Если в response.text приходит <!DOCTYPE html>, то оставляем соответствующую запись,
           чтобы не перегружать отчет, иначе записываем текст ответа'''
        response_text = '<!DOCTYPE html>' if '<!DOCTYPE html>' in response.text else response.text
        allure.attach(body=f'Request:, {method},\n \
                             URL: {url},\n \
                             Request headers: {headers},\n \
                             Request data: {data},\n \
                             Request json: {json},\n \
                             Response Code: {response.status_code},\n \
                             Response headers: {response.headers},\n \
                             Response text: {response_text}',
                             attachment_type=allure.attachment_type.TEXT)

    @allure.step('POST запрос на вторизацию root пользователя')
    def authorization(self):
        data ={
            'username': f'{self.username}',
            'password': f'{self.password}',
            'submit': "Login"
                }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
                    }
        self._request('POST', location='/login', headers=headers, data=data)

    @allure.step(f'GET запрос на проверку статуса приложения')
    def get_check_status(self):
        return self._request('GET', location='/status')

    @allure.step('POST запрос на добавление пользователя {username}')
    def post_add_user(self, username, password, email):
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            "username": username,
            "password": password,
            "email": email
            }
        return self._request('POST', location='/api/add_user', json=body, headers=headers)

    @allure.step('GET запрос на удаление пользователя {username}')
    def get_del_user(self, username):
        return self._request('GET', location=f'/api/del_user/{username}')

    @allure.step('GET запрос на блокировку пользователя {username}')
    def get_block_user(self, username):
        return self._request('GET', location=f'/api/block_user/{username}')

    @allure.step('GET запрос на разблокировку пользователя {username}')
    def get_accept_user(self, username):
        return self._request('GET', location=f'/api/accept_user/{username}')

    @allure.step('GET запрос на логаут root пользователя')
    def get_logout_user(self):
        return self._request('GET', location=f'/logout')
import os
from urllib.parse import urljoin

import requests
from api import data_for_request as data
from api import urls
from api.exceptions import ResponseStatusCodeException
from utils.images import CreateImg


class ApiClient:

    def __init__(self, base_url, user, password):
        self.base_url = base_url
        self.user = user
        self.password = password
        self.session = requests.Session()
        self.header_csrf = None

    def _request(self, method, location, headers=None, data=None, params=None, files=None, expected_status=200):
        url = urljoin(self.base_url, location)
        response = self.session.request(method, url, headers=headers, data=data, params=params, files=files)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')
        return response

    def post_create_segment(self, segment_name):

        response = self._request('POST', urls.URL_NEW_SEGMENT, headers=self.header_csrf, data=data.data_create_segment(segment_name))
        segment_id = response.json()['id']
        return segment_id

    def get_segment_data(self):
        params = {
            'limit': 100
        }
        segments = self._request('GET', urls.URL_NEW_SEGMENT, params=params)
        items = [i for i in segments.json()['items']]
        ids = [i['id'] for i in items]
        names = [i['name'] for i in items]
        return items, ids, names

    def post_delete_segment(self, segment_id):
        self._request('POST', urls.URL_DELETE_SEGMENT, headers=self.header_csrf, data=data.data_delete_segment(segment_id))

    def post_create_company(self, image_path, company_name):
        img_name = CreateImg.create_img(image_path, company_name)
        file = {
            'file': open(os.path.join(image_path, img_name), 'rb')
        }

        response = self._request('POST', urls.URL_POST_IMAGE, headers=self.header_csrf, files=file)
        img_id = response.json()['id']

        params = {
            'url': 'http://vk.com/'
        }
        response = self._request('GET', urls.URL_GET_ID, headers=self.header_csrf, params=params)

        primary_id = response.json()['id']

        response = self._request('POST', urls.URL_COMPANY, headers=self.header_csrf,
                                 data=data.data_create_company(company_name, primary_id, img_id))
        company_id = response.json()['id']
        return company_id

    def get_company_data(self):
        response = self._request('GET', 'https://target.my.com/profile/contacts')
        answer = response.content.decode('utf-8')
        user_id = int(answer.split('data-ga-userid="')[1].split('"')[0])
        companies = self._request('GET', urls.URL_COMPANY, params=data.data_check_company(user_id))
        items = [i for i in companies.json()['items']]
        names = [i['name'] for i in items]
        ids = [i['id'] for i in items]
        return items, names, ids

    def post_delete_company(self, company_id):

        self._request('POST', urls.URL_DELETE_COMPANY, headers = self.header_csrf,
                      data = data.data_delete_company(company_id), expected_status=204)

    def post_login(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }
        my_data = {
            'email': self.user,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email'
        }
        cookies = self.session.post(urls.URL_AUTH, data=my_data, headers=headers, allow_redirects=True).cookies
        req = self.session.get(urljoin(self.base_url, urls.URL_CSRF), cookies=cookies, allow_redirects=True)

        self.header_csrf = {
            'X-CSRFToken': req.cookies.values()[0],
        }
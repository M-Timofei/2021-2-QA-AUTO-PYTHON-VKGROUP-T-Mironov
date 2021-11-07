import json
import requests
from requests.cookies import cookiejar_from_dict
from api import urls
import numpy
from PIL import Image
import os
from utils.decorators import wait

class ResponseErrorException(Exception):
    pass

class ResponseStatusCodeException(Exception):
    pass

class ApiClient:

    def __init__(self, user, password):
        self.user = user
        self.password = password

        self.session = requests.Session()

        self.z = None
        self.mc = None
        self.mrcu = None
        self.sdc = None
        self.csrftoken = None

    def _request(self, method, location, headers=None, data=None, params=None, files = None, expected_status=200):
        url = location
        response = self.session.request(method, url, headers=headers, data=data, params=params, files=files)
        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.request} for URL "{url}"')
        return response

    def post_create_segment(self, segment_name):
        headers = {
            'X-CSRFToken': self.csrftoken,
        }
        data = {
            "name": segment_name,
            "pass_condition": 1,
         "relations": [{"object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}}],
         "logicType": "or"
        }
        dumpdata = json.dumps(data)

        response = self._request('POST', urls.URL_NEW_SEGMENT, headers=headers, data=dumpdata)
        segment_id = response.json()['id']
        return segment_id

    def get_check_segment(self, segment_id, segment_name, check_delete):
        params = {
            'limit': 100
        }
        segments = self._request('GET', urls.URL_NEW_SEGMENT, params=params)
        items = [i for i in segments.json()['items']]
        ids = [i['id'] for i in items]
        names = [i['name'] for i in items]
        """в зависимости от значения check_delete проверяем либо то, что имя и id сегмент 
         присутствуют в соответствующих списках после создания, либо то, что их там нет после удаления"""
        assert (segment_id in ids) is not check_delete
        assert (segment_name in names) is not check_delete
        """при тесте на создание сегмента проверяем, что id и название сегмента принадлежат одной сущности,
        а также то, что сегмент с таким id единственный"""
        if not check_delete:
            assert (ids.index(segment_id) == names.index(segment_name))
            segment = [i for i in items if i['id'] == segment_id]
            assert len(segment) == 1

    def post_delete_segment(self, segment_id):
        headers = {
            'X-CSRFToken': self.csrftoken
        }
        data = [
            {
                "source_id": segment_id,
                 "source_type":"segment"
            }
                ]
        dumpdata = json.dumps(data)
        self._request('POST', urls.URL_DELETE_SEGMENT, headers=headers, data=dumpdata)

    def check_img_saved(self, dir, img_name):
        if img_name in os.listdir(dir):
            return True
        else:
            return False

    def create_img(self, image_path, company_name):
        img_name = company_name + '.png'
        imarray = numpy.random.rand(400, 240, 3) * 255
        im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
        im.save(os.path.join(image_path, img_name))
        wait(self.check_img_saved, error=AssertionError, check=True, dir=image_path, img_name=img_name)
        return img_name

    def post_create_company(self, image_path, company_name):
        headers = {
            'X-CSRFToken': self.csrftoken
        }
        img_name = self.create_img(image_path, company_name)
        file = {
            'file': open(os.path.join(image_path, img_name), 'rb')
        }
        data = {
            "width": 0,
            "height": 0
        }
        response = self._request('POST', urls.URL_POST_IMAGE, headers=headers, data=data, files=file)
        img_id = response.json()['id']

        response = self._request('GET', urls.URL_GET_ID, headers=headers)
        primary_id = response.json()['items'][1]['id']

        data = {"name": company_name,
                "objective": "traffic",
                "budget_limit_day": "100",
                "budget_limit": "100",
                "package_id": 961,
                "banners": [
                    {
                    "urls": {"primary": {"id": primary_id}},
                    "content": {"image_240x400": {"id": img_id}}
                    }
                            ]
                }

        dumpdata = json.dumps(data)
        response = self._request('POST', urls.URL_CREATE_COMPANY, headers=headers, data=dumpdata)
        company_id = response.json()['id']
        return company_id

    def check_company(self,company_id, company_name):
        companies = self._request('GET', urls.URL_CHECK_COMPANY)
        items = [i for i in companies.json()['items']]
        names = [i['name'] for i in items]
        ids = [i['id'] for i in items]
        # проверяем, что название компании и ее id присутствуют в соответствующих списках
        assert company_id in ids
        assert company_name in names

        # проверяем, что id и название компании принадлежат одной сущности
        assert (ids.index(company_id) == names.index(company_name))

        # проверяем, что компания с таким id единственная
        company = [i for i in items if i['id'] == company_id]
        assert len(company) == 1

    def post_delete_company(self, company_id):
        headers = {
            'X-CSRFToken': self.csrftoken
        }
        data = [
            {
                "id": company_id, "status": "deleted"
            }
        ]
        dumpdata = json.dumps(data)
        self._request('POST', urls.URL_DELETE_COMPANY, headers = headers, data = dumpdata, expected_status=204)

    def post_login(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://target.my.com/'
        }
        my_data = {
            'email': self.user,
            'password': self.password,
        }

        resp = requests.post(urls.URL_AUTH, data=my_data, headers=headers, allow_redirects=False)
        response = resp.headers['Set-Cookie'].split(';')
        self.mc = [c for c in response if 'mc' in c][0].split('=')[-1]
        self.mrcu = [c for c in response if 'mrcu' in c][0].split('=')[-1]
        self.ssdc = [c for c in response if 'ssdc' in c][0].split('=')[-1]

        headers = {
            'Cookie': f'mc={self.mc}, ssdc={self.ssdc}, mrcu={self.mrcu}'
        }
        params = {
            'from': urls.URL_PARAMS_FROM
        }
        resp = requests.post(urls.URL_FOR_LOCATION, headers=headers, params=params, allow_redirects=False)
        response = resp.headers['Location']
        location = response
        resp = requests.post(urls.URL_FOR_Z, allow_redirects=False)
        response = resp.headers['Set-Cookie'].split(';')
        self.z = [c for c in response if 'z' in c][0].split('=')[-1]

        token_for_sdc = location.split('=')[-1]
        params = {
            'token': token_for_sdc
        }
        headers = {
            'Cookie': f'z={self.z}, mc={self.mc}, mrcu={self.mrcu}'
        }
        resp = requests.post(urls.URL_FOR_SDC, headers=headers, params=params, allow_redirects=False)
        response = resp.headers['Set-Cookie'].split(';')
        self.sdc = [c for c in response if 'sdc' in c][0].split('=')[-1]

        headers = {
            'Cookie': f'z={self.z}, mc={self.mc}, mrcu={self.mrcu}, sdc={self.sdc}',
        }
        resp = requests.get(urls.URL_CSRF, headers=headers, allow_redirects=False)
        response_cookies = resp.headers['set-cookie'].split(';')
        self.csrftoken = [c for c in response_cookies if 'csrftoken' in c][0].split('=')[-1]

        self.session.cookies = cookiejar_from_dict({
            'z': self.z,
            'mc': self.mc,
            'mrcu': self.mrcu,
            'sdc': self.sdc,
            'csrftoken': self.csrftoken
        })



import pytest
import os
import shutil
from api.client import ApiClient

@pytest.fixture(scope='session')
def cookies(api_client):
    api_client.post_login()
    cookies_list = []
    for cookie in api_client.session.cookies:
        cookie_dict = {'domain': cookie.domain,
                       'name': cookie.name,
                       'value': cookie.value,
                       'secure': cookie.secure
                       }
        cookies_list.append(cookie_dict)
    return cookies_list

@pytest.fixture(scope='session')
def api_client():
    return ApiClient('mironov.timofei@mail.ru', 'MyStrongPassword1')

@pytest.fixture(scope='session')
def config():
    pass

def pytest_configure(config):
    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))

    img_dir = os.path.join(repo_root, 'images')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(img_dir):
            shutil.rmtree(img_dir)
        os.makedirs(img_dir)
    config.img_temp_dir = img_dir

@pytest.fixture(scope='function')
def image_path(request):
    image_path = os.path.join(request.config.img_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(image_path)
    return image_path
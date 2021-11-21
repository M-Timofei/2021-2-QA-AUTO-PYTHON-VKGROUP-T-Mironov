import os
import shutil

from api import urls
from api.client import ApiClient
from api.fixtures import *

@pytest.fixture(scope='session')
def api_client():
    return ApiClient(urls.URL_BASE, 'mironov.timofei@mail.ru', 'MyStrongPassword1')

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
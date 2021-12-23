import shutil
import os

from cases.api.client import ApiClient
from cases.ui.fixtures import *
from db.db_client import DBClient
from mock.mock_client import MockClient
from utils.builder import UserBuilder

def pytest_configure(config):

    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))
    base_dir = os.path.join(repo_root, 'tests_log')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)
    config.base_temp_dir = base_dir

def pytest_unconfigure():
    os.system("cd /tmp; chmod -R 777 allure/")

@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')[0:200])
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='session')
def mock_client():
    return MockClient()

@pytest.fixture(scope='session')
def bd_client():
    return DBClient(user='test_qa', password='qa_test', db_name='PROJECT_DB', host='db', port='3306')

@pytest.fixture(scope='session')
def api_client(create_root_user):
    return ApiClient(base_url=urls.BASE_URL, username=create_root_user.username, password=create_root_user.password)

@pytest.fixture(scope='session')
def api_client_no_root():
    return ApiClient(base_url=urls.BASE_URL, root_user=False)

@pytest.fixture(scope='session')
def create_root_user(bd_client):
    username, password, email = UserBuilder.user()
    root_user = UserModel(
        username='root_' + username,
        password=password,
        email=email,
        active=True,
        access=True,
        start_active_time=datetime.now()
    )
    bd_client.create_user_in_db(root_user)
    return root_user

@pytest.fixture(scope='function')
def create_user(bd_client, user_data):
    user = UserModel(
        username=user_data['username'],
        password=user_data['password'],
        email=user_data['email'],
        active=True,
        access=True,
        start_active_time=datetime.now()
    )
    bd_client.create_user_in_db(user)
    return user

@pytest.fixture(scope='function')
def user_data():
    username, password, email = UserBuilder.user()
    user_data = {'username': username,
                 'password': password,
                 'email': email}
    return user_data



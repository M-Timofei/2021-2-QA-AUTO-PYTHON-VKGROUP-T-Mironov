import shutil
import os
from ui.fixtures import *

def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--debug_log', action='store_true')

@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    debug_log = request.config.getoption('--debug_log')
    return {'browser': browser, 'debug_log': debug_log}

@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG if config['debug_log'] else logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()

    with open(log_file, 'r') as f:
        allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)

@pytest.fixture(scope='session')
def cookies():
    driver = get_driver()
    driver.get(urls.URL_BASE)
    login_page = LoginPage(driver)
    login_page.log_in('mironov.timofei@mail.ru', 'MyStrongPassword1')
    cookies = driver.get_cookies()
    driver.quit()
    return cookies

def pytest_configure(config):
    repo_root = os.path.abspath(os.path.join(__file__, os.path.pardir))

    base_dir = os.path.join(repo_root, 'tests_log')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)
    config.base_temp_dir = base_dir

    img_dir = os.path.join(repo_root, 'images')
    if not hasattr(config, 'workerinput'):
        if os.path.exists(img_dir):
            shutil.rmtree(img_dir)
        os.makedirs(img_dir)
    config.img_temp_dir = img_dir

@pytest.fixture(scope='function')
def temp_dir(request):
    test_dir = os.path.join(request.config.base_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir

@pytest.fixture(scope='function')
def image_path(request):
    image_path = os.path.join(request.config.img_temp_dir, request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(image_path)
    return image_path
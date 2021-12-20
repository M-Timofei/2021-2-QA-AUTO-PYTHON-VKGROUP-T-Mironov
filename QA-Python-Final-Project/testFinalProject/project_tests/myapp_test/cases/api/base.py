import pytest

class BaseCaseAPI:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, bd_client, api_client_no_root):
        self.bd_client = bd_client
        self.api_client = api_client
        self.api_client_no_root = api_client_no_root
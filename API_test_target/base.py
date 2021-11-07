import pytest
from utils.builder import Builder

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client
        self.builder = Builder()

        if self.authorize:
            self.api_client.post_login()

    def create_segment(self, check_delete):
        segment_name = Builder.mynames().segment
        segment_id = self.api_client.post_create_segment(segment_name)
        if not check_delete:
            self.api_client.get_check_segment(segment_id, segment_name, check_delete)
        self.api_client.post_delete_segment(segment_id)
        if check_delete:
            self.api_client.get_check_segment(segment_id, segment_name, check_delete)

    def create_company(self, image_path):
        company_name = Builder.mynames().company
        company_id = self.api_client.post_create_company(image_path, company_name)
        self.api_client.check_company(company_id, company_name)
        self.api_client.post_delete_company(company_id)
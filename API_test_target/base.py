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

    def create_segment(self):
        segment_id = self.api_client.post_create_segment(segment_name=Builder.mynames().segment)
        return segment_id

    def delete_segment(self, segment_id):
        self.api_client.post_delete_segment(segment_id)
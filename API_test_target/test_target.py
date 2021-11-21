import pytest
from base import BaseCase

class TestSegment(BaseCase):

    @pytest.mark.API
    def test_create_segment(self):
        segment_id = self.create_segment()
        ids = self.api_client.get_segment_ids()
        assert segment_id in ids
        self.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        segment_id = self.create_segment()
        self.delete_segment(segment_id)
        ids = self.api_client.get_segment_ids()
        assert (segment_id in ids) is False

class TestCreateCompany(BaseCase):

    @pytest.mark.API
    def test_create_company(self, create_company_fixture):
        company_id = create_company_fixture
        ids = self.api_client.get_company_ids()
        assert company_id in ids
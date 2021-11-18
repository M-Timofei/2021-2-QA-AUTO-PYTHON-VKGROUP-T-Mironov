import pytest
from base import BaseCase

class TestSegment(BaseCase):

    @pytest.mark.API
    def test_create_segment(self):
        segment_id, segment_name = self.create_segment()
        self.check_segment_created(segment_id, segment_name)
        self.delete_segment(segment_id)

    @pytest.mark.API
    def test_delete_segment(self):
        segment_id, segment_name = self.create_segment()
        self.delete_segment(segment_id)
        self.check_segment_deleted(segment_id, segment_name)

class TestCreateCompany(BaseCase):

    @pytest.mark.API
    def test_create_company(self, create_company_fixture):
        company_id, company_name = create_company_fixture
        self.check_company(company_id, company_name)
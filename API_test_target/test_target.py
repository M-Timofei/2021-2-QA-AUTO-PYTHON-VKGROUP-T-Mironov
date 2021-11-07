import pytest
from base import BaseCase

class TestCreateSegment(BaseCase):
    # если check_delete = False - проверяем создание компании, иначе проверяем, что компания удалена
    check_delete = False

    @pytest.mark.API
    def test_create_segment(self):
        self.create_segment(self.check_delete)

class TestDeleteSegment(TestCreateSegment):
    check_delete = True

class TestCreateCompany(BaseCase):

    @pytest.mark.API
    def test_create_company(self, image_path):
        self.create_company(image_path)
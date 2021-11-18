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
        segment_name = Builder.mynames().segment
        segment_id = self.api_client.post_create_segment(segment_name)
        return segment_id, segment_name

    def delete_segment(self, segment_id):
        self.api_client.post_delete_segment(segment_id)

    def check_segment_created(self, segment_id, segment_name):
        items, ids, names = self.api_client.get_segment_data()
        # проверяем, что название сегмента и его id присутствуют в соответствующих списках
        assert segment_id in ids
        assert segment_name in names
        # проверяем, что id и название сегмента принадлежат одной сущности
        assert (ids.index(segment_id) == names.index(segment_name))
        segment = [i for i in items if i['id'] == segment_id]
        # проверяем, что сегмент с таким id единственный
        assert len(segment) == 1

    def check_segment_deleted(self, segment_id, segment_name):
        items, ids, names = self.api_client.get_segment_data()
        # проверяем, что название сегмента и его id отсутствуют в соответствующих списках
        assert (segment_id in ids) is False
        assert (segment_name in names) is False

    def check_company(self, company_id, company_name):
        items, names, ids = self.api_client.get_company_data()
        # проверяем, что название компании и ее id присутствуют в соответствующих списках
        assert company_id in ids
        assert company_name in names
        # проверяем, что id и название компании принадлежат одной сущности
        assert (ids.index(company_id) == names.index(company_name))
        # проверяем, что компания с таким id единственная
        company = [i for i in items if i['id'] == company_id]
        assert len(company) == 1
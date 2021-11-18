import pytest
from utils.builder import Builder

@pytest.fixture(scope='function')
def create_company_fixture(image_path, api_client):
    company_name = Builder.mynames().company
    company_id = api_client.post_create_company(image_path=image_path, company_name=company_name)
    yield company_id, company_name
    api_client.post_delete_company(company_id)
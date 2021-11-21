import pytest
from utils.builder import Builder

@pytest.fixture(scope='function')
def create_company_fixture(image_path, api_client):
    company_id = api_client.post_create_company(image_path=image_path, company_name=Builder.mynames().company)
    yield company_id
    api_client.post_delete_company(company_id)
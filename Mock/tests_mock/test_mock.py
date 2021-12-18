import pytest
import json
from tests_mock.base import SocketBase

class TestPOST(SocketBase):

    @pytest.mark.Mock
    def test_post_positive(self):
        user_data = self.create_user()
        data = self.add_user(name=user_data['name'], id=user_data['user_id'])
        assert (json.loads(data[-1])['user_id']) == user_data['user_id']

    @pytest.mark.Mock
    def test_post_negative(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.add_user(name=user_data['name'], id=user_data['user_id'])
        assert '400 BAD REQUEST' in data[0]

class TestGET(SocketBase):

    @pytest.mark.Mock
    def test_get_positive(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.job_for_user(name=user_data['name'], job=user_data['job'])
        assert json.loads(data[-1])['job'] == user_data['job']

    @pytest.mark.Mock
    def test_get_negative_no_name(self):
        user_data = self.create_user()
        invalid_name = '12345'
        data = self.job_for_user(name=invalid_name, job=user_data['job'])
        assert f'User_name {invalid_name} not found' in data[-1]

    @pytest.mark.Mock
    def test_get_negative_no_job(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.job_for_user(name=user_data['name'], job=None)
        assert f'Job for user_name {user_data["name"]} not found' in data[-1]

class TestPUT(SocketBase):

    @pytest.mark.Mock
    def test_put_positive(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.change_job_for_user(name=user_data['name'], last_job=user_data['job'], new_job=user_data['new_job'])
        assert json.loads(data[-1]).get('job') == user_data['new_job']

    @pytest.mark.Mock
    def test_put_negative_no_name(self):
        user_data = self.create_user()
        invalid_name = '12345'
        data = self.change_job_for_user(name=invalid_name, last_job=user_data['job'], new_job=user_data['new_job'])
        assert f'User_name {invalid_name} not found' in data[-1]

    @pytest.mark.Mock
    def test_put_negative_no_last_job(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.change_job_for_user(name=user_data['name'], last_job=None, new_job=user_data['new_job'])
        assert f'Last job for user_name {user_data["name"]} not found' in data[-1]

class TestDELETE(SocketBase):

    @pytest.mark.Mock
    def test_delete_positive(self):
        user_data = self.create_user()
        self.add_user(name=user_data['name'], id=user_data['user_id'])
        data = self.delete_user(name=user_data['name'])
        assert json.loads(data[-1]).get(user_data['name']) is None

    @pytest.mark.Mock
    def test_delete_negative(self):
        invalid_name = '12345'
        data = self.delete_user(name=invalid_name)
        assert f'User_name {invalid_name} not found' in data[-1]
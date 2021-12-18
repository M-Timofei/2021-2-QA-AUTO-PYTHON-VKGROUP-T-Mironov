import json

import pytest

from mock.flask_mock import JOB_DATA, ID_DATA
from utils.builder import MockBuilder

class SocketBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, socket_client, logger):
        self.builder = MockBuilder()
        self.socket_client = socket_client
        self.logger = logger

    def create_user(self):
        new_data = self.builder.user()
        user_id = new_data.user_id
        name = new_data.name.replace(' ', '_')
        job = new_data.job.replace(' ', '_')
        new_job = new_data.new_job.replace(' ', '_')
        user_data = {
            'user_id': user_id,
            'name': name,
            'job': job,
            'new_job': new_job
        }
        return user_data

    def add_user(self, name, id):
        ID_DATA[name] = id
        data = self.socket_client.post_request(name=name)
        self.logger.info(json.dumps(self.create_log(data=data, response='POST'), indent=4))
        return data

    def job_for_user(self, name, job):
        JOB_DATA[name] = job
        data = self.socket_client.get_request(name=name)
        self.logger.info(json.dumps(self.create_log(data=data, response='GET'), indent=4))
        return data

    def change_job_for_user(self, name, last_job, new_job):
        JOB_DATA[name] = last_job
        data = self.socket_client.put_request(name=name, new_job=new_job)
        self.logger.info(json.dumps(self.create_log(data=data, response='PUT'), indent=4))
        return data

    def delete_user(self, name):
        data = self.socket_client.delete_request(name=name)
        self.logger.info(json.dumps(self.create_log(data=data, response='DELETE'), indent=4))
        return data

    def create_log(self, data, response):
        data_log = {}
        data_log.update({'Response': response})
        data_log.update({'Response Code': data[0].split(' ', maxsplit=1)[1]})
        for i in range(1, len(data)-2):
            data_log.update({
                data[i].split(':')[0]: data[i].split(':')[1]
            })
        data_log.update({
            'Response Body': json.loads(data[-1])
        })
        return data_log
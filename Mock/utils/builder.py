from faker import Faker
from dataclasses import dataclass

fake = Faker()
user_id_seq = 1

class MockBuilder:

    @staticmethod
    def user(user_id=None, name=None, job=None, new_job=None):
        global user_id_seq

        @dataclass
        class User:
            user_id: int = None
            name: str = None
            job: str = None
            new_job: str = None

        if user_id is None:
            user_id = user_id_seq
            user_id_seq += 1

        if name is None:
            name = fake.name()

        if job is None:
            job = fake.job()

        if new_job is None:
            new_job = fake.job()

        return User(user_id=user_id, name=name, job=job, new_job=new_job)
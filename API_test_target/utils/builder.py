from dataclasses import dataclass

from faker import Faker

fake = Faker()

class Builder:

    @staticmethod
    def mynames(segment=None, company=None):

        @dataclass
        class mynames:
            segment: str = None
            company: str = None

        if segment is None:
            segment = fake.bothify(text='Сегмент ##### ?????????? ## ??????????')

        if company is None:
            company = fake.bothify(text='Кампания ##### ?????????? ## ??????????')

        return mynames(segment=segment, company=company)
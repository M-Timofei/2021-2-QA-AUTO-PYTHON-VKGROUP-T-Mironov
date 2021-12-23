from faker import Faker

fake = Faker()

class UserBuilder:

    @staticmethod
    def user():
        username = fake.bothify(text='???????')
        password = fake.bothify(text='?#?#?#?#?#')
        email = username + '@vk.ru'

        return username, password, email


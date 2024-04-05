from faker import Faker

from data.data import Contact

faker_en = Faker('En')
Faker.seed()


def create_contact():
    first_name = faker_en.first_name()
    last_name = faker_en.last_name()
    title = faker_en.sentence(nb_words=3, variable_nb_words=True)
    email = faker_en.email()
    yield Contact(first_name=first_name, last_name=last_name, title=title, email=email)

from faker import Faker
import random
from datetime import datetime
from data.data import Contact

faker_en = Faker('En')
Faker.seed()


def create_contact():
    first_name = faker_en.first_name()
    last_name = faker_en.last_name()
    title = faker_en.sentence(nb_words=3, variable_nb_words=True)
    email = faker_en.email()
    note = faker_en.sentence(nb_words=10, variable_nb_words=True)
    yield Contact(first_name=first_name, last_name=last_name, title=title, email=email, note=note)


def random_datetime() -> str:
    """Generate a random datetime between default start and end."""
    start_date = datetime(2024, 4, 1)
    end_date = datetime(2025, 4, 10, 13, 35, 30, 666000)
    start = datetime.timestamp(start_date)
    end = datetime.timestamp(end_date)
    random_second = random.uniform(start, end)
    random_date = datetime.fromtimestamp(random_second)
    return random_date.isoformat()

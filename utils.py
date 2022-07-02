import random
import string
from faker import Faker
import requests
# import csv
import pandas as pd

def get_password(length: int = 10) -> str:
    """
    generate password
    """

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)

    return password


def get_requirements() -> str:
    """
    read file requirements.txt
    """

    file_name = 'requirements.txt'

    f = open(file_name, "r")
    file_content = f.read()
    f.close()

    return file_content


def get_users(count: int = 100) -> str:
    """
    return 100 randomly generated users (mail + name) 'Dmytro aasdasda@mail.com'
    + parameter that controls the number of users
    """

    faker = Faker()
    users = ''

    for _ in range(count):
        users += faker.first_name() + ' ' + faker.email() + '; '

    return users


def get_astronauts() -> str:
    """
    return the number of astronauts at the moment (http://api.open-notify.org/astros.json)
    """

    api_name = 'http://api.open-notify.org/astros.json'

    r = requests.get(api_name)
    astronauts = str(r.json()["number"])

    return astronauts

def get_mean() -> str:
    """
    Read hw.csv file and calculate average height, average weight in cm and kg respectively
    """

    def inches_to_sm(value: float) -> float:
        k = 2.54
        return value * k


    def pounds_to_kg(value: float) -> float:
        k = 0.453592
        return value * k

    file_name = 'hw.csv'

    #f = open(file_name, "r")
    #for x in f:
    #    data.append()
    #f.close()


    #with open(file_name) as f:
    #    reader = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC)
    #    for row in reader:
    #        height += str(row['Index']), str(row['Height(Inches)'])

    height = ''
    weight = ''

    data = pd.read_csv(file_name)
    #data['Height(Inches)'] = pd.to_numeric()
    return data.to_string()

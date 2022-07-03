from faker import Faker
import requests
import pandas as pd


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

    file_name = 'hw.csv'
    number_of_decimals = 2

    # function convert inches to sm
    def inches_to_sm(value: float) -> float:
        k = 2.54
        return value * k

    # function convert pounds to kg
    def pounds_to_kg(value: float) -> float:
        k = 0.453592
        return value * k

    # create pandas data frame
    df = pd.read_csv(file_name)

    # get mean of Height $ Weight
    height_mean = df[' "Height(Inches)"'].mean()
    weight_mean = df[' "Weight(Pounds)"'].mean()

    # convert Height to sm $ Weight to kg and round values
    height_sm = round(inches_to_sm(height_mean), number_of_decimals)
    weight_kg = round(pounds_to_kg(weight_mean), number_of_decimals)

    result = 'Height_mean_sm: ' + str(height_sm) + ', ' + 'Weight_mean_kg: ' + str(weight_kg)

    return result

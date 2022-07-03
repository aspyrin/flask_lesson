from flask import Flask, request
from utils import get_requirements, get_users, get_astronauts, get_mean

app = Flask(__name__)


@app.route('/requirements/')
def requirements():
    """
    Task #1
    open requirements.txt file and return its contents
    """
    result = get_requirements()
    return result


@app.route('/generate-users/')
def generate_users():
    """
    Task #2
    return 100 randomly generated users (mail + name) 'Dmytro aasdasda@mail.com'
    + parameter that controls the number of users
    """

    count = request.args.get('count') or '100'

    if count.isdigit():
        count = int(count)
        max_count = 200

        if count > max_count:
            return f'Max count should be less that {max_count}.'
    else:
        return f'Invalid parameter count {count}. Integer is expected.'

    result = get_users(count)
    return result


@app.route('/space/')
def space():
    """
    Task #3
    return the number of astronauts at the moment (http://api.open-notify.org/astros.json)
    """

    result = get_astronauts()
    return result


@app.route('/mean/')
def mean():
    """
    Task #4
    Read hw.csv file and calculate average height, average weight in cm and kg respectively
    """
    result = get_mean()
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

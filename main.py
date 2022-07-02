from flask import Flask, request
from utils import get_password, get_requirements, get_users, get_astronauts, get_mean

app = Flask(__name__)


@app.route('/password/')
def password():
    """
    generates and returns a password
    the number of characters in the password is equal to the parameter "length" in "request.args"
    """

    length = request.args.get('length') or '10'

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f'Max length should be less that {max_length}.'
    else:
        return f'Invalid parameter length {length}. Integer is expected.'

    result = get_password(length)
    return result


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

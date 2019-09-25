import re
from logging import log, INFO

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/minutes/<int:count>', methods=['GET'])
def minutes(count):
    last_digit = count % 10
    if last_digit == 1:
        ending = 'минуту'
    elif last_digit in range(2, 5):
        ending = 'минуты'
    else:
        ending = 'минут'
    return f'Вы ввели: {count} {ending}'


@app.route('/check_ident', methods=['POST'])
def check_ident():
    if not request.is_json:
        return 'Content Type is not json', 415
    log(INFO, request.json)
    if 'ident' in request.json:
        ident = request.json['ident']
    else:
        return 'Content Type is not json', 400
    if not re.match('^\d{5}-\d{5} \d$', ident):
        return 'Invalid format', 400
    positions = range(10, 1, -1)
    pairs = zip(positions, [int(char) for char in ident.replace('-', '').replace(' ', '')])
    check_sum = sum([pow(value, 2, position) for position, value in pairs])
    if check_sum > 10:
        check_sum %= 10
    log(INFO, check_sum)
    return jsonify(result=check_sum == int(ident[-1:])), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

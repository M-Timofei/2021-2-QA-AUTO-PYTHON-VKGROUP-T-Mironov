#!/usr/bin/env python3.8
import json
import signal
from flask import Flask, jsonify, request

app = Flask(__name__)

user_data_id = {}

class ServerTerminationError(Exception):
    pass

def exit_gracefully(signum, frame):
    raise ServerTerminationError()

signal.signal(signal.SIGINT, exit_gracefully)  # gracefully exit on -2

signal.signal(signal.SIGTERM, exit_gracefully)  # gracefully exit on -15

@app.route('/vk_id/add_user', methods=['POST'])
def add_user():
    username = json.loads(request.data)['username']
    vk_id = json.loads(request.data)['vk_id']
    if username not in user_data_id:
        user_data_id[username] = vk_id
        return jsonify({'user_id': user_data_id[username]}), 201
    else:
        return jsonify(f'User {username} already exists: id: {user_data_id[username]}'), 400

@app.route('/vk_id/<username>', methods=['GET'])
def get_vk_id(username):
    if user_id := user_data_id.get(username):
        data = {'vk_id': str(user_id)}
        return jsonify(data), 200
    else:
        return jsonify({}), 404

if __name__ == '__main__':
    try:
        MOCK_HOST = 'my_vk_mock'
        MOCK_PORT = '5000'
        app.run(MOCK_HOST, int(MOCK_PORT))
    except ServerTerminationError:
        pass
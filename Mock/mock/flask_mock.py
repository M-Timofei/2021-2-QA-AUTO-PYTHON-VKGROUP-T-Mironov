#!/usr/bin/env python3.8
import json
import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

user_data_id = {}
ID_DATA = {}
JOB_DATA = {}

@app.route('/add_user', methods=['POST'])
def create_user():
    user_name = json.loads(request.data)['name']
    if user_name not in user_data_id:
        user_data_id[user_name] = ID_DATA[user_name]
        return jsonify({'user_id': user_data_id[user_name]}), 201
    else:
        return jsonify(f'User_name {user_name} already exists: id: {user_data_id[user_name]}'), 400

@app.route('/get_user/<name>', methods=['GET'])
def get_user(name):
    if user_id := user_data_id.get(name):
        if job := JOB_DATA.get(name):
            data = {'user_id': user_id,
                    'name': name,
                    'job': job
                    }
            return jsonify(data), 200
        else:
            return jsonify(f'Job for user_name {name} not found'), 404
    else:
        return jsonify(f'User_name {name} not found'), 404

@app.route('/change_user_by_name/<name>', methods=['PUT'])
def change_user_job(name):
    new_job = json.loads(request.data)['new_job']
    if user_id := user_data_id.get(name):
        if job := JOB_DATA.get(name):
            JOB_DATA[name] = new_job
            data = {'user_id': user_id,
                    'name': name,
                    'job': JOB_DATA[name]
                    }
            return jsonify(data), 200
        else:
            return jsonify(f'Last job for user_name {name} not found'), 404
    else:
        return jsonify(f'User_name {name} not found'), 404

@app.route('/delete_user_by_name/<name>', methods=['DELETE'])
def delete_user(name):
    if name in user_data_id:
        try:
            del JOB_DATA[name]
        except:
            pass
        del user_data_id[name]
        return jsonify(user_data_id), 200
    else:
        return jsonify(f'User_name {name} not found'), 404

def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()

@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200

def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server
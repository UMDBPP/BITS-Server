# BITS-Server bits.py
# 
# Copyright (c) 2018 University of Maryland Space Systems Lab Balloon Payload Program
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
The landing page for BITS-Server.
Flask implementation (pip install Flask) running WebSocket protocol (pip install flask-socketio && pip install eventlet)
"""

import os
import requests
import json
from flask import request
from bits import flask_instance

debug = False
log_dir = 'logs'
log_path = os.path.join(log_dir, 'log.json')


def insert_record(record):
    with open(log_path, 'a') as logfile:
        logfile.write(record)


# respond to requests for / with an "under construction" page
@flask_instance.route('/')
def under_construction():
    return flask_instance.send_static_file('under_construction.html')


# handle POST from the Iridium servers (originating from the payload) and log it
@flask_instance.route('/incoming', methods=['POST'])
def from_payload():
    imei = request.form['imei']  # IMEI of RockBlock hardware
    momsn = request.form['momsn']  # message sequence number
    transmit_time = request.form['transmit_time']
    iridium_latitude = request.form['iridium_latitude']
    iridium_longitude = request.form['iridium_longitude']
    iridium_cep = request.form['iridium_cep']  # in km
    data = request.form['data']

    form_json = request.json

    insert_record(form_json)

    if debug:
        return form_json
    else:
        # return HTTP status 200
        return 200


# forward POST from the ground station to the Iridium servers for transfer to the payload
@flask_instance.route('/outgoing', methods=['POST'])
def to_payload():
    outgoing_dict = {'imei': request.form['imei'],  # IMEI of RockBlock hardware
                     'username': request.form['username'],
                     'password': request.form['password'],
                     'data': request.form['data']
                     }

    # send data to RockBlock using POST
    post_reponse = requests.post('https://core.rock7.com/rockblock/MT', json=outgoing_dict)

    error_code, description = post_reponse.text.split(',')

    if error_code == 'OK':
        # do nothing
        pass
    elif error_code == '10':
        # Invalid login credentials
        pass
    elif error_code == '11':
        # No RockBLOCK with this IMEI found on your account
        pass
    elif error_code == '12':
        # RockBLOCK has no line rental
        pass
    elif error_code == '13':
        # Your account has insufficient credit
        pass
    elif error_code == '14':
        # Could not decode hex data
        pass
    elif error_code == '15':
        # Data too long
        pass
    elif error_code == '16':
        # No data
        pass
    elif error_code == '99':
        # System Error
        pass

    # return response
    return post_reponse.text


# handle GET request from the ground station for stored payload messages
@flask_instance.route('/', methods=['GET'])
def to_ground():
    with open(log_path, 'r') as logfile:
        outgoing_json = json.loads(logfile.read())

    # return data
    return outgoing_json


if __name__ == "__main__":
    flask_instance.run()

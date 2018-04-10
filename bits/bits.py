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

# import flask and web socket libraries, as well as special functions and JSON library
from flask import Flask, request

# create the application instance
flask_instance = Flask(__name__)

# load config from this file
# flask_instance.config.from_object(__name__)

# override configuration settings
flask_instance.config.update(dict(
    SECRET_KEY='secret!',
    USERNAME='admin',
    PASSWORD='default'
))

# respond to requests for / with an "under construction" page
@flask_instance.route('/')
def under_construction():
    flask_instance.send_static_file('under_construction.html')
    return 'under_construction'

# handle POST to the server from elsewhere
@flask_instance.route('/', methods=['POST'])
def parse_POST_request():
    imei = request.form['imei']  # IMEI of RockBlock hardware
    momsn = request.form['momsn']  # message sequence number
    transmit_time = request.form['transmit_time']
    iridium_latitude = request.form['iridium_latitude']
    iridium_longitude = request.form['iridium_longitude']
    iridium_cep = request.form['iridium_cep']  # in km
    data = request.form['data']

    # TODO store data

    # return HTTP status 200
    return 200

# handle GET to the server from elsewhere
@flask_instance.route('/', methods=['GET'])
def parse_GET_request():
    # TODO retrieve data

    # return HTTP status 200
    return 200

if __name__ == "__main__":
    flask_instance.run()

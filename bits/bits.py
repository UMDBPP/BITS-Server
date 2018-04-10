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
from flask_socketio import SocketIO, send, emit, Namespace

## application setup
__name__ = "__main__"

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

socketio_instance = SocketIO(flask_instance)


## main program

# respond to requests for / with an "under construction" page
@flask_instance.route('/')
def under_construction():
    return 'under contruction'
    # return flask_instance.send_static_file('under_construction.html')


# handle POST to the server from elsewhere
@flask_instance.route('/', methods=['POST'])
def parse_request():
    imei = request.form['imei'] # IMEI of RockBlock hardware
    momsn = request.form['momsn'] # message sequence number
    transmit_time = request.form['transmit_time']
    iridium_latitude = request.form['iridium_latitude']
    iridium_longitude = request.form['iridium_longitude']
    iridium_cep = request.form['iridium_cep'] # in km
    data = request.form['data']

    # TODO return HTTP 200


# create BITS namespace class
class bits(Namespace):
    def on_connect(self):
        print('Client connected to bits')

    def on_disconnect(self):
        print('Client disconnected from bits')

    def on_my_event(self, data):
        emit('my_response', data)


# define instance to namespace (instantiate object)
socketio_instance.on_namespace(bits('/test'))


# define error handler
@socketio_instance.on_error('/bits')  # handles the '/bits' namespace
def error_handler_bits(e):
    pass


# upon receiving a JSON message via web socket, broadcast the received JSON over the namespace
@socketio_instance.on('json')
def handle_json(json):
    input_json = json.loads(json)
    print('received json: ' + str(input_json))
    send(input_json, json=True, broadcast=True)


# use gunicorn server?
if __name__ == '__main__':
    socketio_instance.run(flask_instance, debug=True)

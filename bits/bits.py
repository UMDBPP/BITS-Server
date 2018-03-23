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
from bits import flask_instance, socketio_instance as socketio
from flask_socketio import send, emit, Namespace

import json

# respond to requests for / with an "under construction" page
@flask_instance.route('/')
def under_construction():
    return flask_instance.send_static_file('under_construction.html')

class bits(Namespace):
    def on_connect(self):
        print('Client connected to bits')

    def on_disconnect(self):
        print('Client disconnected to bits')

    def on_my_event(self, data):
        emit('my_response', data)

socketio.on_namespace(bits('/test'))

@socketio.on_error('/bits') # handles the '/bits' namespace
def error_handler_bits(e):
    pass

@socketio.on('json')
def handle_json(json):
    input_json = json.loads(json)
    print('received json: ' + str(input_json))
    send(input_json, json=True)
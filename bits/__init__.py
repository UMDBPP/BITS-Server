from flask import Flask
from flask_socketio import SocketIO

__name__ = "bits"

# create the application instance
flask_instance = Flask(__name__)

# load config from this file
flask_instance.config.from_object(__name__)

# default configuration settings
flask_instance.config.update(dict(
    SECRET_KEY='secret!',
    USERNAME='admin',
    PASSWORD='default'
))

import bits.bits

#if __name__ == '__main__':
#    socketio.run(flask_instance)

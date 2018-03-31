from flask import Flask
from flask_socketio import SocketIO

__name__ = "bits"

# create the application instance
flask_instance = Flask(__name__)

# load config from this file
#flask_instance.config.from_object(__name__)

# override configuration settings
flask_instance.config.update(dict(
    SECRET_KEY='secret!',
    USERNAME='admin',
    PASSWORD='default'
))

socketio_instance = SocketIO(flask_instance)


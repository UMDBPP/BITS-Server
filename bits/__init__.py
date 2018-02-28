from flask import Flask
from flask_socketio import SocketIO

__name__ = "bits"

flask_instance = Flask(__name__)
flask_instance.config['SECRET_KEY'] = 'secret!'
socketio_instance = SocketIO(flask_instance)

import bits.landingpage


#if __name__ == '__main__':
#    socketio.run(flask_instance)

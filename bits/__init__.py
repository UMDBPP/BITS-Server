from flask import Flask
from flask_socketio import SocketIO

flask_instance = Flask(__name__)
flask_instance.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(flask_instance)

if __name__ == '__main__':
    socketio.run(flask_instance)
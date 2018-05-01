from flask import Flask

# create the application instance
flask_instance = Flask(__name__, static_url_path='')

# load config from this file
# flask_instance.config.from_object(__name__)

# override configuration settings
#flask_instance.config.update(dict(
#    SECRET_KEY='secret!',
#    USERNAME='admin',
#    PASSWORD='default'
#))

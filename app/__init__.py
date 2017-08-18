from flask import Flask
from flask_script import Manager


def createApp(config_name):
    app = Flask(__name__)
    from .index import app as index
    app.register_blueprint(index, url_prefix='/index')
    return app

# coding:utf8
from flask import Flask

def create_app():
    app = Flask('jelly')
    #register_blueprints(app)
    return app

def register_blueprints(app):
    from jelly import api
    app.register_blueprint(api.blueprint, url_prefix='')
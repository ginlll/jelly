# coding:utf8
from flask import Flask
from flask_script import Manager,Server

from jelly import create_app, register_blueprints

app = create_app()
manager = Manager(app)

@manager.option('-H', '--host',   dest='host',   help='Host address', default='0.0.0.0')
@manager.option('-p', '--port',   dest='port',   help='Application port', default=9098)
def runserver(host, port):
    register_blueprints(app)
    app.run(host=host, port=int(port))

if __name__ == "__main__":
    manager.run()

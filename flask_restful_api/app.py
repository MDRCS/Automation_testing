import os

from flask import Flask
from flask_restful import Api

from flask_restful_api.resources.item import Item, ItemList

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)

api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    from flask_restful_api.db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)

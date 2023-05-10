from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import db
from flask_migrate import Migrate
from resource.create_log import LogDataResource
from resource.get_curr import LastLogDataResource


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    app.app_context().push()
    #Create the databases
    db.create_all() 

    api.add_resource(LogDataResource, '/log_data')
    api.add_resource(LastLogDataResource, '/last-log/<device_id>')
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, Blueprint		#blueprint api version #flask create instance
from flask_restx import Api	#rest api	
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from authz.config import Config			#import application	config

db = SQLAlchemy()
mg = Migrate()

#api = Api()
apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)		#create API for /api/v1 endpoint

from authz import resource

def create_app():
	app = Flask(__name__)	#create application instance
	app.config.from_object(Config)	#set application configuration
	#app.init_app(api)
	db.init_app(app)
	mg.init_app(app,db)
	app.register_blueprint(apiv1_bp)	#register /api/v1 to application
	return app	#return application instance to callers
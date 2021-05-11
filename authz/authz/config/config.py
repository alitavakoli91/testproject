from os import environ

class Config:
	DEBUG = bool(environ.get("AUTHZ_DEBUG", False))
	ENV = environ.get("AUTHZ_ENV", "production")
	TESTING = bool(environ.get("AUTHZ_TESTING", False))
	SQLALCHEMY_DATABASE_URI = environ.get("AUTHZ_DATABASE_URI", None)
	SQLALCHEMY_ECHO = DEBUG
	SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
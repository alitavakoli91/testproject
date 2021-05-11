from shared import uuidgen
from authz import db

class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=uuidgen)
    username = db.Column(db.String(128), unique=True, index=True, nullable=Flase)
    password = db.Column(db.String(128), nullable=Fale)
	
	
	
	
	
	
#User = [
#	{
#		"username": "test1"
#	},
#	{
#		"username": "test2"
#	}
#]


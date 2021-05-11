from flask_restx import Resource
from authz.controller.apiv1 import UserController

class UserResource(Resource):
	def get(self, user_id=None):
		"""
		GET /users ---> Get user collection
		GET /users/<user_id> ---> Get single user
		"""
		if user_id == None:
			return UserController.get_users()		#get user collection
		else:
			return UserController.get_users(user_id)	#get user single

	def post(self):
	    """
		POST /users --> Create new user.
		"""
		return UserController.create_user()
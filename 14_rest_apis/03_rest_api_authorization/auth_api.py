from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt import JWT, jwt_required

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
api = Api(app)

jwt = JWT(app, authenticate, identity)

puppies = []

class PuppyNames(Resource):

	# Get method
	def get(self, name):
		print(puppies)
		for pup in puppies:
			if pup["name"] == name:
				return pup
		return {"name": None}, 404

	# Post method
	def post(self, name):
		pup = {"name": name}
		puppies.append(pup)
		print(puppies)
		return pup
	
	# Delete method
	def delete(self, name):
		for ind,pup in enumerate(puppies):
			if pup["name"] == name:
				delted_pup = puppies.pop(ind)
				return {"note": "delete successful"}

# Get all puppies
class AllNames(Resource):
	@jwt_required()
	def get(self):
		return {"puppies": puppies}

# Register the rss to the end-point
api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

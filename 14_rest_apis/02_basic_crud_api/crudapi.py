from flask import Flask, request
from flask_restful import Resource, Api

# Instanciate app and API
app = Flask(__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):
	
	# GET method
	def get(self, name):
		print(puppies)
		for pup in puppies:
			if pup["name"] == name:
				return pup
		return {"name": None}, 404

	# POST method	
	def post(self, name):
		pup = {"name": name}
		puppies.append(pup)
		print(puppies)
		return pup

	# DELETE method
	def delete(self, name):
		for ind, pup in enumerate(puppies):
			if pup["name"] == name:
				delted_pup = puppies.pop(ind)
				return {"note": "delete successful"}


# Get method for getting all pup names
class AllNames(Resource):
	def get(self):
		return {"puppies": puppies}

# Add resources to endpoints
api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

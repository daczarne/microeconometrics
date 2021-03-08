from flask import Flask
from flask_restful import Resource, Api

# Instanciate the app and the API
app = Flask(__name__)
api = Api(app)

# Create a resource
class HelloWorld(Resource):
	# Define the get method
	def get(self):
		return {"hello": "world"}

# Add resource to an endpoint
api.add_resource(HelloWorld, "/")

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

from flask import Flask
from flask import request

# Instanciate the app
app = Flask(__name__)

# Index
@app.route("/")
def index():
	return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>"

# Puppy Latin route
@app.route("/puppy_latin/<name>")
def puppylatin(name):
	pupname = ""
	if name[-1] == "y":
		pupname = name[:-1] + "iful"
	else:
		pupname = name + "y"
	return f"<h1>Hi {name}! Your puppylatin name is {pupname}</h1>"

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

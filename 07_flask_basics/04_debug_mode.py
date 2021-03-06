from flask import Flask

# Instanciate the app
app = Flask(__name__)

# Index route
@app.route("/")
def index():
  return "<h1>Hello Puppy!</h1>"

# Info route
@app.route("/information")
def info():
  return "<h1>Puppis are cute!</h1>"

# Puppy profile
@app.route("/puppy/<name>")
def puppy(name):
  return f"<h1>This is a page for {name}</h1>"

# Run the app
if __name__ == "__main__":
  app.run(debug = True)

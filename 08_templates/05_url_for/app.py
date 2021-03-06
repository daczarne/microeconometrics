from flask import Flask, render_template

# Instaciate the app
app = Flask(__name__)

# Build the home page
@app.route("/")
def index():
  return render_template("home.html")

# Build the pup page
@app.route("/puppy/<name>")
def pup_name(name):
  return render_template("puppy.html", name = name)

# Run the app
if __name__ == "__main__":
  app.run(debug = True)

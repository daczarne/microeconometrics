from flask import Flask, render_template

# Instaciate the app
app = Flask(__name__)

# Build the index route
@app.route("/")
def index():
  name = "John"
  letters = list(name)
  pups = {"pup_name": "Sammy"}
  return render_template(
    "basic.html",
    name = name,
    letters = letters,
    pups = pups
  )

# Run the app
if __name__ == "__main__":
  app.run(debug = True)

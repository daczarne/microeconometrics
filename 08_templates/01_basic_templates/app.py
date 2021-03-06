from flask import Flask, render_template

# Instaciate the app
app = Flask(__name__)

# Build the index route
@app.route("/")
def index():
  return render_template("basic.html")

# Run the app
if __name__ == "__main__":
  app.run(debug = True)

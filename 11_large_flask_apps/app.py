from myproject import app
from flask import render_template

# Index
@app.route("/")
def index():
	return render_template("home.html")

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

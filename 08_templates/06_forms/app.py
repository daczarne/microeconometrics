# Note we imported request!
from flask import Flask, render_template, request

# Instanciate the app
app = Flask(__name__)

# Index
@app.route("/")
def index():
	return render_template("index.html")

# Signup form
@app.route("/signup_form")
def signup_form():
	return render_template("sign-up.html")

# Thank you page
@app.route("/thankyou")
def thank_you():
	first = request.args.get("first")
	last = request.args.get("last")
	return render_template("thankyou.html", first = first, last = last)

# 404 page
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

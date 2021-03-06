# Note we imported request!
from flask import Flask, render_template, request

# Instanciate the app
app = Flask(__name__)

# Index
@app.route("/")
def index():
	return render_template("index.html")

# Report
@app.route("/report")
def report():
	# Iniciate variables
	lower_letter = False
	upper_letter = False
	num_end = False
	# Get the user name
	username = request.args.get("username")
	# Check conditions
	lower_letter = any(c.islower() for c in username)
	upper_letter = any(c.isupper() for c in username)
	num_end = username[-1].isdigit()
	# Validate
	report = lower_letter and upper_letter and num_end
	# Return template
	return render_template(
		"report.html",
		report = report,
		lower = lower_letter,
		upper = upper_letter,
		num_end = num_end
	)

# Run the app
if __name__ == "__main__":
	app.run(debug = True)

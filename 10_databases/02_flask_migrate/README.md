# Flask Migrate

Sometimes, after creating a Model for a DB table we'll need to make adjustments to the model. For example, we might need to a add a new column. After making these changes, we'll need to *migrate* them in order to update the database table. We can do this with `flask-migrate`.

In order to perfom the migration, there are four basic command-line commands that we'll need to use:

1. Set up the Flask App environment variable by running: `set FLASK_APP=<app_name.py>` (use `export` for MacOS or Linux). Make sure to `cd` into the directory where the app is located.

1. Set up the migrations directory with `flask db init`

1. Set up the migration file with `flask db migrate -m "Message goes here"`

1. Update the DB with the migration with `flask db upgrade`.

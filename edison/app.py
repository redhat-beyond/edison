import edison
import edison.models

from flask import render_template
from flask_migrate import Migrate


app = edison.app
db = edison.db
migrate = Migrate(app, db)

# Creates all tables defined in the database models and the only ones that are not created yet.
# If there's any change in the database models you should perform a migration to apply this change in the database itself.
# More about database migrations can be found in /edison/migrations/README.
db.create_all()

@app.route("/policy")
def policy():
	return render_template('policy.html')

@app.route("/")
def home():
	return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

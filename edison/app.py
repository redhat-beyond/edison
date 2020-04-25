import edison

from flask import render_template


# API description in swagger - https://app.swaggerhub.com/apis/DoRTaL94/UserManagment/1.0.0

app = edison.app

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

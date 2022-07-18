# main.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
	return render_template("home.html")

@app.route("/dashboard")
def dashboard():
	return "nic's dashboard"


if __name__ == "__name__":
	app.run(host="127.0.0.1", port=8080, debug=True)
from flask import Flask, request, render_template
import datetime as dt

app = Flask(__name__, template_folder="templates")

@app.route("/user_form", methods=['POST'])
def user_form():

	print(request.form)

	return "<a href='http://127.0.0.1:5000/'>back</a>"


@app.route("/")
def index():
	return render_template("user_form.html")

if __name__=="__main__":
	app.run(debug=True)
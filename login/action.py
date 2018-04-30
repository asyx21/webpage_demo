from flask import Flask, request, render_template
import datetime as dt


# credential tests
login_cred = [{"name": "julien", "passwd": "admin"}, {"name": "aaa", "passwd": "aaaaa"}]

app = Flask(__name__, template_folder="templates")

@app.route("/login_form", methods=['POST'])
def login_form():

	print(request.form)
	print(request.form['f_name'])

	for dic in login_cred:
		if(request.form['f_name'] in dic['name']):
			if(request.form['f_passwd'] in dic['passwd']):
				# login success
				return "Hello "+str(request.form['f_name'])+"<br><a href='http://127.0.0.1:5000/'>back</a>"

	# fail to login
	return render_template("login_form.html", msg="ERROR: I dont know this account")


@app.route("/new_account", methods=['POST'])
def new_account():
	# page to create new account
	return render_template("create_account.html")


@app.route("/create_account", methods=['POST'])
def create_account():

	print(request.form)

	return "Hello<br>"+str(request.form['f_name'])+"<br>"+str(request.form['f_email'])+"<br><a href='http://127.0.0.1:5000/'>back</a>"


@app.route("/")
def index():
	return render_template("login_form.html")

if __name__=="__main__":
	app.run(debug=True)
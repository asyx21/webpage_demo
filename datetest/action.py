from flask import Flask, request, render_template
import datetime as dt


app = Flask(__name__, template_folder="templates")

# injects variable to all templates
@app.context_processor
def inject_today():
    today = dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d")
    return dict(today=today)


# method 
@app.route("/date_form", methods=['POST'])
def date_form():
	print(request.form)

	# optional if javascript handles error in the first place
	t1 = dt.datetime.strptime(request.form['f_date1'], "%Y-%m-%d")
	t2 = dt.datetime.strptime(request.form['f_date2'], "%Y-%m-%d")


	if(t1 < t2):
		return "init date: "+str(request.form['f_date1'])+\
		"<br>end date: "+str(request.form['f_date2']\
			+"<br><a href='http://127.0.0.1:5000/'>back</a>")
	else:
		return render_template("date_form.html", msg="ERROR: select chronological dates!")


@app.route("/")
def index():
	return render_template("date_form.html")

if __name__=="__main__":
	app.run(debug=True)
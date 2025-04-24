from flask import Flask,render_template,jsonify

app = Flask(__name__)

DATA = None

SEM = []

YEAR = [1,2,3,4]

@app.route("/")
def hello_world():
  return render_template('home.html', years = YEAR,department = 'Electrical' )

@app.route("/year1")


def year_1():
 
  return render_template('year1.html')






@app.route("/year2")
def year_2():
  return render_template('year2.html') 

@app.route("/year3")
def year_3():
  return render_template('year3.html')

@app.route("/year4")
def year_4():
  return render_template('year4.html')


@app.route("/api/SEM")
def list_sem():
    return(jsonify(SEM))
  
if __name__ == "__main__":
  app.run(host='0.0.0.0' , debug = True)
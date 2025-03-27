from flask import Flask,render_template,jsonify

app = Flask(__name__)

SEM = [{'sem': 1,
      'title': 'Sem 1',
       'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
        'labs':['BEE Lab','Workshop Lab','PPS Lab']
       },
       {'sem': 2,
         'title': 'Sem 2',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 3,
        'title': 'Sem 3',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 4,
        'title': 'Sem 4',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 5,
        'title': 'Sem 5',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 6,
        'title': 'Sem 6',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 7,
        'title': 'Sem 7',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          },
       {'sem': 8,
        'title': 'Sem 8',
          'subjects':['Physics','BEE','Maths1','Workshop','PPS'],
           'labs':['BEE Lab','Workshop Lab','PPS Lab']
          }
      
      
      ]

YEAR = [1,2,3,4]

@app.route("/")
def hello_world():
  return render_template('home.html',sems = SEM, years = YEAR,department = 'Electrical' )

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
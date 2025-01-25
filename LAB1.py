from flask import Flask, request, jsonify
import json
import string
app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
   return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

#exercise 1
@app.route('/stats')
def get_stats():
    chicken = 0
    fish = 0
    vege = 0
    csm = 0
    css = 0
    itm = 0
    its = 0

    for student in data:
        if student['pref'] == "Chicken":
            chicken += 1
        elif student['pref'] == "Fish":
            fish += 1
        else: 
            vege += 1

    for stu in data:
        if stu['programme'] == "Computer Science (Major)":
            csm += 1
        elif stu['programme'] == "Computer Science (Special)":
            css += 1
        elif stu['programme'] == "Information Technology (Major)": 
            itm += 1
        elif stu['programme'] == "Information Technology (Special)": 
            its += 1

    stats = {
        "Chicken" : chicken,
        "Fish" : fish,
        "Vegetatrian" : vege,
        "Computer Science (Special)" : css,
        "Computer Science (Major)" : csm,
        "Information Technology (Special)" : its,
        "Information Technology (Major)" : itm
    }

    return stats

#exercise 2
@app.route('/add/<a>/<b>')
def get_result1(a,b):
    sum = int(a) + int(b)
    return str(sum)

@app.route('/subtract/<a>/<b>')
def get_result2(a,b):
    sum = int(a) - int(b)
    return str(sum)

@app.route('/multiply/<a>/<b>')
def get_result3(a,b):
    sum = int(a) * int(b)
    return str(sum)

@app.route('/divide/<a>/<b>')
def get_result4(a,b):
    sum = int(a) / int(b)
    return str(sum)

app.run(host='0.0.0.0', port=8080, debug=True)
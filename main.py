from flask import Flask, render_template, request
import datetime
import re
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  result1 = 0
  with open("INFO.txt") as file:
    for line in file:
      if "y1" in line:
        result1 += 1
  result2 = 0
  with open("INFO.txt") as file:
    for line in file:
      if "y2" in line:
        result2 += 1
  currenttime = datetime.datetime.now()
  stringy = currenttime.isoformat()
  print(stringy[-15:])
  if stringy == "00:00:00.000000":
    f = open('file.txt', 'r+')
    f.truncate(0)
  if request.method == 'GET':
    return render_template('home.html', result1=result1, result2=result2)

@app.route('/attendance', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('attendance.html')
  else:
    todaysdate = datetime.date.today()
    currentdate = todaysdate.isoformat()
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    breakfast = request.form.get('breakfast')
    dinner = request.form.get('dinner')
    pattern = re.compile("^[8-9][0-9]{7}$")
    if pattern.match(mobile):
      fout = open("INFO.txt", 'a')
      fout.write(name + ',' + mobile + ',' + breakfast + ',' + dinner + ',' + currentdate + '\n')
      fout.close()  
      return render_template("attendance.html")
    else:
      return render_template("secret.html")

@app.route('/delete', methods=['GET', 'POST'])
def secret():
  return render_template("delete.html")

app.run(host='0.0.0.0', port=8080)